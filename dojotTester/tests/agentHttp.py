import datetime
import time
import logging

from common.testutils import *
from common.certUtils import *
from common.base_test import BaseTest
from iotAgentHttp.httpClient import HTTPSClient


@group('manual')
class HTTPPublicationCertExpiredManual(BaseTest):
    """
    Simple publication using expired certificate.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id = "b34794"

        # waiting for update the certificate list
        time.sleep(2)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"temperature": 1000, 'humidity': 60}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, timestamp="2021-10-03T09:30:01.683000Z")
        self.assertTrue(rc == 403,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 1000)
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")


@group('manual')
class HTTPPublicationWithRevokedCertManual(BaseTest):
    """
    Publication using a revoked certificate.
    WARNING: It is needed to change the default CRL update time
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, fingerprint = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)
        rc, _ = Api.delete_certificate(self.jwt, fingerprint)
        self.assertTrue(rc == 204, "** FAILED ASSERTION: Error on revoke certificate")

        # waiting for CRL update
        time.sleep(200)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"temperature": 1000, 'humidity': 60}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, timestamp="2021-10-03T09:30:01.683000Z")
        self.assertTrue(rc == 403,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 1000)
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value")

        rc, response = get_history_last_attr(self, self.jwt, self.device_id, "temperature")
        self.logger.info('history for device is:' + str(response))
        self.assertTrue(rc == 200, "** FAILED ASSERTION: Unexpected result code: " + str(rc))
        self.assertTrue(response["ts"] == "2021-10-03T09:30:01.683000Z", "** FAILED ASSERTION: "
                                                                         "Unexpected timestamp value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


@group('manual')
class HTTPPublicationExternalCertificateManual(BaseTest):
    """
    Simple publication using a certificate issued by an external CA.

    This test is manual due to updating time lag of the CA bundle
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, self.crt_bundle_path, self.private_key_path = \
            create_a_device_and_its_external_certificate(self, self.jwt)

        # self.device_id = 'bb3b2c'
        # self.crt_bundle_path = ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + self.device_id + "_client-bundle.crt"
        # self.private_key_path = ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + self.device_id +"_client.key"

        self.logger.info("device id is: " + self.device_id)
        self.assertTrue(self.device_id is not None, "** FAILED ASSERTION: device id is None")
        retrieve_dojot_ca_chain(self.jwt)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        # waiting to process
        time.sleep(200)
        dev1 = HTTPSClient(self.device_id, self.crt_bundle_path, self.private_key_path)

        payload = {"temperature": 90, 'humidity': 60}
        publish_date = datetime.datetime.utcnow().isoformat() + "Z"

        dev1.publish(payload)

        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 90)
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value")

        rc, response = get_history_last_attr(self, self.jwt, self.device_id, attr="temperature")
        self.assertTrue(rc == 204, "** FAILED ASSERTION: Unexpected result code: " + str(rc))
        self.assertTrue(response["ts"] > publish_date, "** FAILED ASSERTION: "
                                                       "Unexpected timestamp:" + str(
            response["ts"]) + " <= " + publish_date)

    # def tearDown(self):
    #     """
    #     This method will only be called if the setUp() succeeds.
    #      This method is called immediately after the test method has been called and the result recorded.
    #      This is called even if the test method raised an exception.
    #      """
    #     rc, _ = Api.delete_device(self.jwt, self.device_id)
    #     self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
    #                     ") while deleting the device " + str(self.device_id))
    #     self.logger.info('Teardown executed!')
    #     super().tearDown()


class HTTPPublicationWithTimestamp(BaseTest):
    """
    Simple publication with timestamp included.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"temperature": 1000, 'humidity': 60}
        self.logger.debug('https client publishing...')

        now = datetime.datetime.now()
        timestamp = now - datetime.timedelta(minutes=40)

        timestamp_isoformat = timestamp.isoformat() + "Z"

        rc, res = dev1.publish(payload, timestamp=timestamp_isoformat)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 1000)
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value")

        rc, response = get_history_last_attr(self, self.jwt, self.device_id, "temperature")
        self.logger.info('history for device is:' + str(response))
        self.assertTrue(rc == 200, "** FAILED ASSERTION: Unexpected result code: " + str(rc))

        self.assertTrue(compare_timestamp(self, response["ts"],  timestamp), "** FAILED ASSERTION: "
                                                                         "Unexpected timestamp value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationWithUnixTimestamp(BaseTest):
    """
    Simple publication using unix timestamp.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)

        # publication using unix timestamp in seconds
        self.logger.info('publication using unix timestamp in seconds')
        now = datetime.datetime.now()
        timestamp = now - datetime.timedelta(minutes=30)
        timestamp = int(timestamp.timestamp())

        timestamp_isoformat = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        payload = {"temperature": 100, 'humidity': 60}
        rc, res = dev1.publish(payload, timestamp=timestamp)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(5)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 100)
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value: " + str(count))

        rc, response = get_history_last_attr(self, self.jwt, self.device_id, attr="temperature")
        self.assertTrue(rc == 200, "** FAILED ASSERTION: Unexpected result code: " + str(rc))
        publication_time = response["ts"]
        self.assertTrue(match_iso8601(self, publication_time) is not None, "... ISO 8601 format error")
        self.assertTrue(compare_timestamp(self, publication_time, timestamp),
                        "** FAILED ASSERTION: Unexpected timestamp:" +
                        str(response["ts"]) + " instead of " + timestamp_isoformat)

        # publication using unix timestamp in milliseconds
        self.logger.info('publication using unix timestamp in milliseconds')
        timestamp = now - datetime.timedelta(days=3, minutes=45)
        timestamp = int(timestamp.timestamp()*1000)  # multiplied by 1000 to get timestamp in milliseconds
        timestamp_isoformat = datetime.datetime.fromtimestamp(timestamp/1000, tz=datetime.timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        payload = {"temperature": 100, 'humidity': 60}
        rc, res = dev1.publish(payload, timestamp=timestamp)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(5)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 100)
        self.assertTrue(count == 2, "** FAILED ASSERTION: Unexpected count value: " + str(count))

        rc, response = get_history_first_attr(self, self.jwt, self.device_id, attr="temperature")
        self.assertTrue(rc == 200, "** FAILED ASSERTION: Unexpected result code: " + str(rc))
        publication_time = response["ts"]
        self.assertTrue(match_iso8601(self, publication_time) is not None, "... ISO 8601 format error")
        self.assertTrue(compare_timestamp(self, publication_time, timestamp),
                        "** FAILED ASSERTION: Unexpected timestamp:" + publication_time +
                        " instead of " + timestamp_isoformat)

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationWithoutTimestamp(BaseTest):
    """
    Simple publication without timestamp.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)

        payload = {"temperature": 90, 'humidity': 60}
        publish_date = datetime.datetime.utcnow().isoformat() + "Z"
        rc, res = dev1.publish(payload)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(5)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 90)
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value")

        rc, response = get_history_last_attr(self, self.jwt, self.device_id, attr="temperature")
        self.assertTrue(rc == 200, "** FAILED ASSERTION: Unexpected result code: " + str(rc))
        self.assertTrue(response["ts"] > publish_date, "** FAILED ASSERTION: "
                                                       "Unexpected timestamp:" + str(
            response["ts"]) + " <= " + publish_date)

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()





class HTTPPublicationInvalidFieldData(BaseTest):
    """
    Publication using an invalid field (dados).
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"dados": {"temperature": 16, "humidity": 60}}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, send_as_is=True)
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationWithoutDataField(BaseTest):
    """
    Publication using an without data field.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, send_as_is=True)
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        self.logger.debug(f'result code: {rc}. Body: {res}')
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationInvalidFieldTimestampString(BaseTest):
    """
    Publication using an invalid field (ts).
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"data": {"temperature": 16, "humidity": 60}}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, timestamp="hoje")
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationInvalidFieldTimestampDay(BaseTest):
    """
    Publication using an invalid field (ts).
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"data": {"temperature": 16, "humidity": 60}}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, timestamp="2021-11-35T09:30:01.683000Z")
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationInvalidFieldTimestampMonth(BaseTest):
    """
    Publication using an invalid field (ts).
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"data": {"temperature": 16, "humidity": 60}}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, timestamp="2021-13-15T09:30:01.683000Z")
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationWithTimestampVerbose(BaseTest):
    """
    Publication using an invalid field (ts).
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"data": {"temperature": 16, "humidity": 60}}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, timestamp="Thursday, December 23, 2021 9:15:17 AM")
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCertNotAssociated(BaseTest):
    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, fingerprint = create_a_device_and_its_certificate(self, self.jwt)
        rc, res = Api.disassociate_certificate(self.jwt, fingerprint)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))

        retrieve_dojot_ca_chain(self.jwt)
        time.sleep(5)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)

        payload = {"temperature": 90, 'humidity': 60}
        rc, res = dev1.publish(payload, timestamp="2021-10-03T09:30:01.683000Z")
        self.assertTrue(rc == 403,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(5)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 90)
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")


class HTTPPublicationWithInvalidTimestamp(BaseTest):
    """
    Simple publication with timestamp included.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"temperature": 1000, 'humidity': 60}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, timestamp="hoje")
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 1000)
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationWithAdditionalFields(BaseTest):
    """
    Simple publication with additional fields included.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = {"ts_gmt": 99999999,
                   "data": {"temperature": 16, "humidity": 60},
                   "dados": {"temperature": 16, "humidity": 60}}
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish(payload, send_as_is=True)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 16)
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCreateManyWithTimestamp(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')

        payload = [
            {
                "ts": "2021-10-03T10:30:01.000000Z",
                "data": {
                    "temperature": 37.8
                }
            },
            {
                "ts": "2021-10-03T10:42:02.000000Z",
                "data": {
                    "temperature": 21.0
                }
            },
            {
                "ts": "2021-10-03T10:50:00.000000Z",
                "data": {
                    "temperature": 10.0
                }
            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 3, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCreateManyUnixTimestamp(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        timestamps_iso_format = []

        now = datetime.datetime.now()
        timestamp1 = now - datetime.timedelta(minutes=30)
        timestamp1 = int(timestamp1.timestamp())
        timestamps_iso_format.append(datetime.datetime.fromtimestamp(timestamp1, tz=datetime.timezone.utc).replace(
            tzinfo=None).isoformat() + "Z")

        timestamp2 = now - datetime.timedelta(minutes=45)
        timestamp2 = int(timestamp2.timestamp())
        timestamps_iso_format.append(datetime.datetime.fromtimestamp(timestamp2, tz=datetime.timezone.utc).replace(
            tzinfo=None).isoformat() + "Z")

        timestamp3 = now - datetime.timedelta(minutes=52)
        timestamp3 = int(timestamp3.timestamp())
        timestamps_iso_format.append(datetime.datetime.fromtimestamp(timestamp3, tz=datetime.timezone.utc).replace(
            tzinfo=None).isoformat() + "Z")

        payload = [
            {
                "ts": timestamp1,
                "data": {
                    "temperature": 17.5
                }
            },
            {
                "ts": timestamp2,
                "data": {
                    "temperature": 31.0
                }
            },
            {
                "ts": timestamp3,
                "data": {
                    "temperature": 12.0
                }
            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 3, "** FAILED ASSERTION: Unexpected count value")

        rc, response = Api.get_history_device(self.jwt, self.device_id, "temperature")
        self.assertTrue(rc == 200, "** FAILED ASSERTION: Unexpected result code: " + str(rc))
        self.logger.info('Tamanho: ' + str(len(response)) + str(response[0]['ts']) + str(response[1]['ts']) + str(response[2]['ts']))
        for history_data in response:
            self.assertTrue(match_iso8601(self, history_data['ts']) is not None, "... ISO 8601 format error")
            for published_data in timestamps_iso_format:
                if compare_timestamp(self, published_data, str(history_data['ts'])):
                    timestamps_iso_format.remove(published_data)
                    break
        self.assertTrue(len(timestamps_iso_format) == 0, "** FAILED ASSERTION: timestamp not found." +
                        "missing timestamp: " + str(timestamps_iso_format) +
                        "history for device is:" + str(response))

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCreateManyWithoutTimestamp(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = [
            {
                "data": {
                    "temperature": 22.8
                }
            },
            {
                "data": {
                    "temperature": 31.0
                }
            },
            {
                "data": {
                    "temperature": 20.0
                }
            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


@group('manual')
class HTTPPublicationCreateManyCertExpiradoManual(BaseTest):
    """
    Simple publication with timestamp included.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id = "b34794"

        # waiting for update the certificate list
        time.sleep(2)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = [
            {
                "ts": "2021-10-03T10:30:01.000000Z",
                "data": {
                    "temperature": 37.8
                }
            },
            {
                "ts": "2021-10-03T10:42:02.000000Z",
                "data": {
                    "temperature": 21.0
                }
            },
            {
                "ts": "2021-10-03T10:50:00.000000Z",
                "data": {
                    "temperature": 10.0
                }
            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 403,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 1000)
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")


class HTTPPublicationCreateManyCertNotAssociated(BaseTest):
    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, fingerprint = create_a_device_and_its_certificate(self, self.jwt)
        rc, res = Api.disassociate_certificate(self.jwt, fingerprint)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))

        retrieve_dojot_ca_chain(self.jwt)
        time.sleep(5)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)

        payload = [
            {
                "ts": "2021-10-03T10:30:01.000000Z",
                "data": {
                    "temperature": 37.8
                }
            },
            {
                "ts": "2021-10-03T10:42:02.000000Z",
                "data": {
                    "temperature": 21.0
                }
            },
            {
                "ts": "2021-10-03T10:50:00.000000Z",
                "data": {
                    "temperature": 10.0
                }
            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 403,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(5)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr_value(self, self.jwt, self.device_id, "temperature", 90)
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")


class HTTPPublicationCreateManyWithoutDataFieldAll(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = [
            {
                "ts": "2021-10-03T10:30:01.000000Z"

            },
            {
                "ts": "2021-10-03T10:42:02.000000Z"

            },
            {
                "ts": "2021-10-03T10:50:00.000000Z"

            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCreateManyInvalidSchema(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        now = datetime.datetime.now()
        timestamp1 = now - datetime.timedelta(minutes=20)
        timestamp1_isoformat = timestamp1.isoformat() + "Z"
        timestamp2 = now - datetime.timedelta(minutes=35)
        timestamp2_isoformat = timestamp2.isoformat() + "Z"
        timestamp3 = now - datetime.timedelta(minutes=40)
        timestamp3_isoformat = timestamp3.isoformat() + "Z"

        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        payload = [
            {
                "ts": timestamp1_isoformat,
                "data": {"temperature": 31.0}
            },
            {
                "ts": timestamp2_isoformat

            },
            {
                "ts": timestamp3_isoformat,
                "data": {"temperature": 36.0}

            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        self.logger.debug(f'result code: {rc} and body: {res}')
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value: " + str(count))

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCreateManyEmptyDataField(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        now = datetime.datetime.now()
        timestamp1 = now - datetime.timedelta(minutes=20)
        timestamp1_isoformat = timestamp1.isoformat() + "Z"
        timestamp2 = now - datetime.timedelta(minutes=35)
        timestamp2_isoformat = timestamp2.isoformat() + "Z"
        timestamp3 = now - datetime.timedelta(minutes=40)
        timestamp3_isoformat = timestamp3.isoformat() + "Z"
        payload = [
            {
                "ts": timestamp1_isoformat,
                "data": {}
            },
            {
                "ts": timestamp2_isoformat,
                "data": {}

            },
            {
                "ts": timestamp3_isoformat,
                "data": {}

            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        self.logger.debug(f'result code: {rc} and body: {res}')
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCreateManyInvalidSchema2(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        now = datetime.datetime.now()
        timestamp1 = now - datetime.timedelta(minutes=20)
        timestamp1_isoformat = timestamp1.isoformat() + "Z"
        timestamp2 = now - datetime.timedelta(minutes=35)
        timestamp2_isoformat = timestamp2.isoformat() + "Z"
        timestamp3 = now - datetime.timedelta(minutes=40)
        timestamp3_isoformat = timestamp3.isoformat() + "Z"
        payload = [
            {
                "ts": timestamp1_isoformat,
                "dados": {"temperature": 31.0}
            },
            {
                "ts": timestamp2_isoformat,
                "data": {"temperature": 32.0}

            },
            {
                "ts": timestamp3_isoformat,
                "data": {"temperature": 33.0}

            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        self.logger.debug(f'result code: {rc} and body: {res}')
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value: " + str(count))

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()


class HTTPPublicationCreateManyInvalidTimestamp(BaseTest):
    """
    Simple Publication using create-many endpoint.
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.device_id, _ = create_a_device_and_its_certificate(self, self.jwt)

        # waiting for update the certificate list
        time.sleep(2)

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        dev1 = HTTPSClient(self.device_id)
        self.logger.debug('https client instance created...')
        now = datetime.datetime.now()
        timestamp1 = now - datetime.timedelta(minutes=20)
        timestamp1_isoformat = timestamp1.isoformat() + "Z"
        timestamp2 = now - datetime.timedelta(minutes=35)
        timestamp2_isoformat = timestamp2.isoformat() + "Z"
        payload = [
            {
                "ts": timestamp1_isoformat,
                "data": {"temperature": 31.0}
            },
            {
                "ts": "hoje",
                "data": {"temperature": 32.0}

            },
            {
                "ts": timestamp2_isoformat,
                "data": {"temperature": 33.0}

            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        self.logger.debug(f'result code: {rc} and body: {res}')
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 2, "** FAILED ASSERTION: Unexpected count value: " + str(count))

        # All timestamp is invalid
        payload = [
            {
                "ts": "string",
                "data": {"temperature": 31.0}
            },
            {
                "ts": "two days ago",
                "data": {"temperature": 32.0}

            },
            {
                "ts": "last",
                "data": {"temperature": 33.0}

            }
        ]
        self.logger.debug('https client publishing...')
        rc, res = dev1.publish_many(payload)
        self.assertTrue(rc == 400,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        self.logger.debug(f'result code: {rc} and body: {res}')
        # waiting to process
        time.sleep(2)
        self.logger.info('Checking history for publication')
        rc, count = get_history_count_attr(self, self.jwt, self.device_id, "temperature")
        self.assertTrue(count == 2, "** FAILED ASSERTION: Unexpected count value")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        rc, _ = Api.delete_device(self.jwt, self.device_id)
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting the device " + str(self.device_id))
        self.logger.info('Teardown executed!')
        super().tearDown()
