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

        device_id = add_a_simple_device(self)
        self.logger.info("device id is: " + device_id)
        self.assertTrue(device_id is not None, "** FAILED ASSERTION: device id is None")


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
