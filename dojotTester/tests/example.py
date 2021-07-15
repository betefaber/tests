import time
import random

from common.testutils import *
from common.base_test import BaseTest
from mqtt.mqttClient import MQTTClient


class DummyTest(BaseTest):
    """
    Dummy description.
    """
    def setUp(self):
        super().setUp()
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Dummy test executed')

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
         This method is called immediately after the test method has been called and the result recorded.
         This is called even if the test method raised an exception.
         """
        self.logger.info('Teardown executed!')
        super().tearDown()


class RegistryASimpleDevice(BaseTest):
    """
    API Registry a Simple Device.
    """

    def runTest(self):
        jwt = Api.get_jwt()
        self.logger.info("JWT = " + jwt)
        self.assertTrue(jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        device_id = add_a_simple_device(self, jwt)
        self.logger.info("device id is: " + device_id)
        self.assertTrue(device_id is not None, "** FAILED ASSERTION: device id is None")

class GetHistoryExample(BaseTest):
    """
    Shows how to get some history data
    """
    def runTest(self):
        self.logger.info('Executing GetHistoryExample test...')
        jwt = Api.get_jwt()
        self.logger.info("JWT = " + jwt)
        self.assertTrue(jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        # add a device
        device_id = add_a_simple_device(self, jwt)
        self.logger.info("device id is: " + device_id)
        self.assertTrue(device_id is not None, "** FAILED ASSERTION: device id is None")

        # count - publication with a specific attribute/value
        rc, count = get_history_count_attr_value(self, jwt, device_id, "temperature", 12)
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

        # count - publication with a specific attribute
        rc, count = get_history_count_attr(self, jwt, device_id, "temperature")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

        # publish some data
        device_topic = "admin:" + device_id + "/attrs"
        device_client = MQTTClient(device_id)
        self.logger.info("publicando com dispositivo: " + device_id)
        device_client.publish(device_topic, {"temperature": 12})

        # count - publication with a specific attribute/value
        time.sleep(2)
        rc, count = get_history_count_attr_value(self, jwt, device_id, "temperature", 12)
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value: " + str(count))

        # count - publication with a specific attribute
        rc, count = get_history_count_attr(self, jwt, device_id, "temperature")
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value")

        rc, count = get_history_count_attr(self, jwt, device_id, "humidity")
        self.assertTrue(count == 0, "** FAILED ASSERTION: Unexpected count value")

        # Do 5 publication
        for temperature in random.sample(range(15, 40), 5):
            device_client.publish(device_topic, {"temperature": temperature})
            time.sleep(1.2)

        rc, count = get_history_count_attr(self, jwt, device_id, "temperature")
        self.assertTrue(count == 6, "** FAILED ASSERTION: Unexpected count value")

        # Print all device history data
        rc, response = Api.get_history_device(jwt, device_id, attrs="temperature")
        self.assertTrue(rc == 200, "** FAILED ASSERTION: Unexpected result code: " + str(rc))
        self.logger.info("History data: " + str(response))


class ApiDummyTest(BaseTest):
    """
    API dummy example.
    """

    def runTest(self):
        self.logger.info('Executing Api dummy test...')
        jwt = Api.get_jwt()
        self.logger.info("JWT = " + jwt)
        self.assertTrue(jwt is not None, "JWT is None")


class ApiErrorDummyTest(BaseTest):
    """
    Dojot API error handling example.
    """

    def runTest(self):

        jwt = Api.get_jwt()
        self.logger.info("JWT = " + jwt)
        self.assertTrue(jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        template1 = {
            "labe": "SensorModel",
            "attrs": [
                {
                    "label": "temperature",
                    "type": "dynamic",
                    "value_type": "float"
                },
                {
                    "label": "model-id",
                    "type": "static",
                    "value_type": "string",
                    "static_value": "model-001"
                }
            ]
        }
        rc, response = Api.create_template(jwt, template1)
        self.logger.info(f"result code is {rc}")
        self.logger.info(f"response is {response}")
        self.assertTrue(rc == 400, "** FAILED ASSERTION: received an unexpected result code **")


class MqttDummyTest(BaseTest):
    """
    MQTT example test.
    """

    def runTest(self):
        self.logger.info('Executing MQTT dummy test...')
        dev1 = MQTTClient("123456")

        payload = "{\"temperature\": 10}"
        dev1.publish("admin:123456/attrs", payload)
