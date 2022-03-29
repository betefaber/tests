import datetime
import logging

from common.certUtils import CA, TrustedClientCertificate, get_csr, generatePrivateKey
from common.utils import save_file
from config import CONFIG
from dojot.api import DojotAPI as Api
from dojotTester import ROOT_DIR
import re

dojot_ca_chain_file = ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + "root_ca.crt"


def add_a_simple_device(self, jwt: str, template=None, label="SimpleDevice"):
    if template is None:
        template = add_a_simple_template(self, jwt)

    rc, res = Api.create_device(jwt, template, label)
    self.assertTrue(rc == 200, f"** FAILED ASSERTION: failure to add device {label}**")

    return res["devices"][0]["id"]


def add_a_simple_template(self, jwt: str, label="SimpleTemplate"):
    template1 = {
        "label": label,
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
    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to create template **")
    return response["template"]["id"]


def get_history_count_attr_value(self, jwt: str, dev_id: str, attr: str, value: str) -> tuple:
    rc, res = Api.get_history_device(jwt, dev_id, attr)
    self.logger.info("history: " + str(res))

    # No data for the given attribute
    if rc == 404 and res["description"] == "No data for the given attribute could be found":
        return rc, 0

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to get history from device " + dev_id + " **")

    counter = 0
    for publication_data in res:
        if publication_data["value"] == value:
            counter = counter + 1

    return rc, counter


def get_history_count_attr(self, jwt: str, dev_id: str, attr: str) -> tuple:
    rc, res = Api.get_history_device(jwt, dev_id, attr)
    self.logger.info("history: " + str(res))

    # No data for the given attribute
    if rc == 404 and res["description"] == "No data for the given attribute could be found":
        return rc, 0

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to get history from device" + dev_id + " **")

    return rc, len(res)


def get_history_first_attr(self, jwt: str, dev_id: str, attr: str) -> tuple:
    rc, res = Api.get_history_device(jwt, dev_id, attr, firstn=1)

    # No data for the given attribute
    if rc == 404 and res["description"] == "No data for the given attribute could be found":
        return rc, None

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to get history from device" + dev_id + " **")

    return rc, res[0]


def get_history_last_attr(self, jwt: str, dev_id: str, attr: str) -> tuple:
    rc, res = Api.get_history_device(jwt, dev_id, attr, lastn=1)

    # No data for the given attribute
    if rc == 404 and res["description"] == "No data for the given attribute could be found":
        return rc, None

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to get history from device" + dev_id + " **")

    return rc, res[0]

def get_history_count_notifications(self, jwt: str) -> tuple:
    rc, res = Api.get_history_notifications(jwt)
    self.logger.info("Retrieving notifications: " + str(res))

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to retrieve notifications **")

    response = res["notifications"]
    self.logger.info("notifications: " + str(response))

    return rc, len(response)

def get_count_users(self, jwt: str) -> tuple:
    rc, res = Api.get_users(jwt)
    self.logger.info("Retrieving users: " + str(res))

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to retrieve notifications **")

    response = res["users"]
    self.logger.info("users: " + str(response))

    return rc, len(response)

def get_count_profiles(self, jwt: str) -> tuple:
    rc, res = Api.get_profiles(jwt)
    self.logger.info("Retrieving profiles: " + str(res))

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to retrieve notifications **")

    response = res["groups"]
    self.logger.info("profiles: " + str(response))

    return rc, len(response)

def get_retriever_count_attr(self, jwt: str, dev_id: str, attr: str) -> tuple:
    rc, res = Api.get_retriever_device_attr(jwt, dev_id, attr)

    # return empty if no data for the given attribute
    response = res["data"]

    self.logger.info("response: " + str(response))
    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to get history from device" + dev_id + " **")

    return rc, len(response)

def create_a_device_and_its_certificate(self, jwt: str):

    device_id = add_a_simple_device(self, jwt)
    self.logger.info("device id is: " + device_id)
    self.assertTrue(device_id is not None, "** FAILED ASSERTION: device id is None")

    # generateKeys
    generate_keys(device_id, 2048)
    # dns = ["dns.com.br"]
    dns = []
    ip = []
    cname = "admin:" + device_id
    # generateCSR(device_id, cname, True, dns, ip)
    fingerprint = ask_cert_sign(jwt, device_id, cname, dns, ip)
    Api.associate_certificate(jwt, fingerprint, device_id)
    retrieve_dojot_ca_chain(jwt)
    return device_id, fingerprint


def create_a_device_and_its_external_certificate(self, jwt: str):

    device_id = add_a_simple_device(self, jwt)
    self.logger.info("device id is: " + device_id)
    self.assertTrue(device_id is not None, "** FAILED ASSERTION: device id is None")

    ca = CA()
    ca.save_crt_file(ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + "_ca.crt")
    ca.save_key_file(ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + "_ca.key")

    cert = TrustedClientCertificate(ca)
    cert.save_crt_file(ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + "_client.crt")
    private_key_path = ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + "_client.key"
    cert.save_key_file(private_key_path)

    rc, res = Api.register_trusted_ca(jwt, ca.get_crt_pem(), False)
    self.assertTrue(rc == 201, "** FAILED ASSERTION: device id is None")
    ca_fingerprint = res["caFingerprint"]

    rc, fingerprint = Api.register_external_certificate(jwt, ca_fingerprint, cert.get_crt_pem(), device_id)
    self.assertTrue(rc == 201, "** FAILED ASSERTION: device id is None")

    # generating bundle
    bundle_path = ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + "_client-bundle.crt"
    with open(bundle_path, "wt") as f:
        f.write(cert.get_crt_pem() + ca.get_crt_pem())

    return device_id, bundle_path, private_key_path


def match_iso8601(self, iso_time):
    match = re.compile(
        '^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$').match
    return match(iso_time)


def compare_timestamp(self, ts1: str or int or datetime.datetime, ts2: str or int or datetime.datetime) -> bool:
    """
    Compare two timestamps using resolution 0:0:0.001
    """
    if isinstance(ts1, str):
        ts1 = ts1.replace('Z', '')
        ts1 = datetime.datetime.fromisoformat(ts1)

    if isinstance(ts2, str):
        ts2 = ts2.replace('Z', '')
        ts2 = datetime.datetime.fromisoformat(ts2)

    if isinstance(ts1, int):
        if ts1.bit_length() > 31:
            ts1 = ts1 // 1000
        ts1 = datetime.datetime.fromtimestamp(ts1, tz=datetime.timezone.utc).replace(tzinfo=None)

    if isinstance(ts2, int):
        self.logger.debug("original ts2: " + str(ts2))
        # support unix timestamp in milliseconds
        microsecond = None
        if ts2.bit_length() > 31:
            microsecond = int(str(ts2)[-3::])*1000
            self.logger.debug('microseconds is: ' + str(microsecond))
            ts2 = ts2 // 1000
        self.logger.debug("updated ts2: " + str(ts2))
        ts2 = datetime.datetime.fromtimestamp(ts2, tz=datetime.timezone.utc).replace(tzinfo=None)
        if microsecond is not None:
            ts2 = ts2.replace(microsecond=microsecond)
            self.logger.debug('microseconds updated')
        self.logger.debug("updated again ts2: " + str(ts2))

    timestamp1 = ts1.replace(microsecond=(ts1.microsecond // 1000)*1000)
    timestamp2 = ts2.replace(microsecond=(ts2.microsecond // 1000)*1000)
    self.logger.debug("comparing ts1: " + str(timestamp1) + " to " + "ts2: " + str(timestamp2))

    return timestamp1 == timestamp2


def retrieve_dojot_ca_chain(jwt):
    """
    Obtains the CA of the dojot platform used to sign the device certificates and save it to a file
    """
    rc, response = Api.get_ca(jwt)
    filename = dojot_ca_chain_file
    save_file(filename, response["caPem"])

    return rc


def ask_cert_sign(jwt, device_id, cname, dns, ip):
    filename = ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + ".crt"
    csr = get_csr(device_id, cname, dns, ip)
    rc, cert = Api.create_certificate(jwt, csr)
    # assert (rc == 201, f'** FAILED ASSERTION: unexpected result code: {rc}')
    save_file(filename, cert["certificatePem"])
    logging.info(device_id + " certificate signed. Avaliable at " + filename + "FingerPrint: " + cert[
        "certificateFingerprint"])
    return cert["certificateFingerprint"]


def generate_keys(devname, length):
    filename = ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + devname + ".key"
    generatePrivateKey(filename, length)


# decorators to test cases
def disabled(cls):
    """
    testcase decorator that marks the test as being disabled.
    """
    cls._disabled = True
    return cls


def group(name):
    """
        testcase decorator that adds the test to a group.
    """
    def fn(cls):
        if not hasattr(cls, "_groups"):
            cls._groups = []
        cls._groups.append(name)
        return cls
    return fn
