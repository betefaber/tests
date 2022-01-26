import logging
import os
import time

import requests
import json

from common.utils import Utils
from config import CONFIG
import dojotTester

logger = Utils.create_logger("http_client")


class HTTPSClient:
    """
    HTTPS client to Dojot MQTT IoTAgent.
    """

    def __init__(self,
                 device_id: str,
                 client_cert_path: str = None,
                 client_key_path: str = None
                 ):
        """
        HTTPS client constructor.

        Args:
            device_id: device identifier
        """
        logger.debug("initiating https client device " + device_id)
        self.device_id = device_id
        self.session = requests.Session()
        if client_cert_path is None:
            client_cert_path = dojotTester.ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + ".crt"

        if client_key_path is None:
            client_key_path = dojotTester.ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + ".key"
        self.session.cert = (client_cert_path, client_key_path)
        logger.debug("CA file exists: " + str(os.path.exists(dojotTester.ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/root_ca.crt")))
        logger.debug("private key file exists: " + str(os.path.exists(client_key_path)))
        logger.debug("client cert file exists: " + str(os.path.exists(client_cert_path)))
        self.session.verify = False  # dojotTester.ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/root_ca.crt"
        time.sleep(5)

    def post(self, *args, **kwargs):
        res = self.session.post(
                            headers={'Content-Type': 'application/json'}, *args, **kwargs)
        return res.status_code, res.json() if res.status_code != 204 else None

    def publish(self, payload=None, data=None, timestamp=None, send_as_is=False):
        logger.info("init publishing...")
        body = {}
        if not send_as_is:
            if timestamp is not None:
                body['ts'] = timestamp
            if "data" in payload.keys():
                body['data'] = payload['data']
            else:
                body['data'] = payload
        else:
            body = payload
        logger.info("publishing:" + str(json.dumps(body)))
        rc, res = self.post(f"https://{CONFIG['http']['host']}:{CONFIG['http']['port']}/http-agent/v1/incoming-messages", json.dumps(body))
        return rc, res

    def publish_many(self, payload, send_as_is=False):
        logger.info("init publishing...")
        body = payload

        logger.info("publishing:" + str(json.dumps(body)))
        rc, res = self.post(f"https://{CONFIG['http']['host']}:{CONFIG['http']['port']}/http-agent/v1/incoming-messages/create-many", json.dumps(body))
        return rc, res
