"""
API calls to Dojot.
"""
import json
import time
from typing import Callable, List
import requests
import gevent

from config import CONFIG
from common.utils import Utils

LOGGER = Utils.create_logger("api")


class APICallError(Exception):
    """
    Error when trying to call Dojot API.
    """


class DojotAPI:
    """
    Utility class with API calls to Dojot.
    """

    @staticmethod
    def get_jwt() -> str:
        """
        Request a JWT token.
        """
        LOGGER.debug("Retrieving JWT...")

        args = {
            "url": "{0}/auth".format(CONFIG['dojot']['url']),
            "data": json.dumps({
                "username": CONFIG['dojot']['user'],
                "passwd": CONFIG['dojot']['passwd'],
            }),
            "headers": {
                "Content-Type": "application/json"
            },
        }

        rc, res = DojotAPI.call_api(requests.post, args)
        if rc == 429:
            time.sleep(15)
            rc, res = DojotAPI.call_api(requests.post, args)
        LOGGER.debug(".. retrieved JWT. Result code: " + str(rc))
        return res["jwt"]

    @staticmethod
    def create_devices(jwt: str, template_id: str, total: int, batch: int) -> None:
        """
        Create the devices.

        Parameters:
            jwt: Dojot JWT token
            template_id: template ID to be used by the devices
            total: total number of devices to be created
            batch: number of devices to be created in each iteration
        """
        LOGGER.debug("Creating devices...")

        args = {
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
        }

        loads = DojotAPI.divide_loads(total, batch)

        for i, load in enumerate(loads):
            args["data"] = json.dumps({
                "templates": [template_id],
                "attrs": {},
                "label": "CargoContainer_{0}".format(i)
            })
            args["url"] = "{0}/device?count={1}&verbose=false".format(CONFIG['dojot']['url'], load)

            DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... created the devices")

    @staticmethod
    def create_template(jwt: str, data=None or dict) -> tuple:
        """
        Create the default template for test devices.

        Returns the created template ID or a error message.
        """
        LOGGER.debug("Creating template...")
        if data is None:
            data = json.dumps({
                "label": "dummy template",
                "attrs": [
                    {
                        "label": "timestamp",
                        "type": "dynamic",
                        "value_type": "integer"
                    },
                ]
            })
        if isinstance(data, dict):
            data = json.dumps(data)

        args = {
            "url": "{0}/template".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... created the template")
        return result_code, res

    @staticmethod
    def create_device(jwt: str, template_id: str or list = None, label: str = None, data: str = None, count: int = None,
                      verbose: bool = None) -> tuple:
        """
        Create a device in Dojot.

        Parameters:
            jwt: JWT authorization.
            template_id: template to be used by the device.
            label: name for the device in Dojot.
            data: request body. if provided template_id and label is ignored.
            count: amount of devices registries
            verbose: Set to True if full device description is to be returned.

        Returns the created device ID or a error message.
        """
        LOGGER.debug("Creating device...")
        if data is None:
            if template_id is None or label is None:
                raise APICallError("ERROR: must either provide body field or template_id and label fields")

        if not isinstance(template_id, list):
            template_id = [template_id]

        # setting url
        url = "{0}/device".format(CONFIG['dojot']['url'])
        if count is not None:
            url = url + "?count=" + str(count)
            if verbose is not None:
                url = url + "&verbose=" + str(verbose)
        else:
            if verbose is not None:
                url = url + "?verbose=" + str(verbose)

        # setting args
        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
        }
        if data is None:
            args["data"] = json.dumps({
                "templates": template_id,
                "attrs": {},
                "label": label,
            })
        else:
            args["data"] = data

        LOGGER.debug("sending request...")
        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("...done ")
        return result_code, res

    @staticmethod
    def create_flow(jwt: str, flow: str) -> tuple:
        """
        Create a flow in Dojot.

        Parameters:
            jwt: JWT authorization.
            flow: flow definition.


        Returns the created flow ID.
        """
        LOGGER.debug("Creating flow...")

        args = {
            "url": "{0}/flows/v1/flow".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": json.dumps(flow),
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... flow created")
        return result_code, res

    @staticmethod
    def create_group(jwt: str, group: str) -> tuple:
        """
        Create a group in Dojot.

        Parameters:
            jwt: JWT authorization.
            group: group definition.


        Returns the created group ID.
        """
        LOGGER.debug("Creating group...")

        args = {
            "url": "{0}/auth/pap/group".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": json.dumps(group),
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... group created")

        return result_code, res

    @staticmethod
    def add_permission(jwt: str, group: str, permission: str) -> tuple:
        """
        Add permission a group in Dojot.

        Parameters:
            jwt: JWT authorization.
            group: group receiving permission
            permission: permission definition


        Returns the created group ID.
        """
        LOGGER.debug("Adding permission...")

        args = {
            "url": "{0}/auth/pap/grouppermissions/{1}/{2}".format(CONFIG['dojot']['url'], group, permission),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... permission added")
        return result_code, res

    @staticmethod
    def create_user(jwt: str, user: str) -> tuple:
        """
        Create a user in Dojot.

        Parameters:
            jwt: JWT authorization.
            user: user data.


        Returns the created user ID.
        """
        LOGGER.debug("Creating user...")

        args = {
            "url": "{0}/auth/user".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": json.dumps(user),
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... user created")
        return result_code, res

    @staticmethod
    def get_deviceid_by_label(jwt: str, label: str) -> str or None:
        """
        Retrieves the devices from Dojot.

        Parameters:
            jwt: Dojot JWT token
            label: Dojot device label

        Returns device ID or None.
        """
        LOGGER.debug("Retrieving devices...")

        args = {
            "url": "{0}/device?idsOnly=true&label={1}".format(CONFIG['dojot']['url'], label),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        devices_id = res[0] if rc == 200 else None

        LOGGER.debug("... retrieved the devices")

        return devices_id

    @staticmethod
    def update_template(jwt: str, template_id: int, data: str) -> tuple:
        """

        Returns the updated template ID or a error message.
        """
        LOGGER.debug("Updating template...")

        if isinstance(data, dict):
            data = json.dumps(data)
        args = {
            "url": "{0}/template/{1}".format(CONFIG['dojot']['url'], template_id),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.put, args)

        LOGGER.debug("... updated the template")
        return result_code, res

    @staticmethod
    def delete_devices(jwt: str) -> tuple:
        """
        Delete all devices.
        """
        LOGGER.debug("Deleting devices...")

        args = {
            "url": "{0}/device".format(CONFIG['dojot']['url']),
            "headers": {
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... deleted devices")
        return rc, res

    @staticmethod
    def delete_device(jwt: str, device_id: str) -> tuple:
        """
        Delete device.
        """
        LOGGER.debug("Deleting device...")

        args = {
            "url": "{0}/device/{1}".format(CONFIG['dojot']['url'], device_id),
            "headers": {
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... deleted device")
        return rc, res

    @staticmethod
    def delete_templates(jwt: str) -> tuple:
        """
        Delete all templates.
        """
        LOGGER.debug("Deleting templates...")

        args = {
            "url": "{0}/template".format(CONFIG['dojot']['url']),
            "headers": {
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... deleted templates")

        return rc, res

    @staticmethod
    def delete_template(jwt: str, template_id: int) -> tuple:
        """
        Delete specific template.
        """

        LOGGER.debug("Deleting template...")

        args = {
            "url": "{0}/template/{1}".format(CONFIG['dojot']['url'], str(template_id)),
            "headers": {
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... deleted template")
        return rc, res

    @staticmethod
    def get_devices(jwt: str) -> List:
        """
        Retrieves the devices from Dojot.

        Parameters:
            jwt: Dojot JWT token

        Returns a list of IDs.
        """
        LOGGER.debug("Retrieving devices...")

        args = {
            "url": "{0}/device".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        _, res = DojotAPI.call_api(requests.get, args)

        devices_ids = [device['id'] for device in res['devices']]

        LOGGER.debug("... retrieved the devices")

        return devices_ids

    @staticmethod
    def get_templates(jwt: str) -> tuple:
        """
        Retrieves all templates.

        Parameters:
            jwt: Dojot JWT token

            """
        LOGGER.debug("Retrieving templates...")

        args = {
            "url": "{0}/template".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved all templates")

        return rc, res

    @staticmethod
    def get_templates_with_parameters(jwt: str, attrs: str) -> tuple:
        """
        Retrieves all templates.

        Parameters:
            jwt: Dojot JWT token
            attrs: optional parameters

            """
        LOGGER.debug("Retrieving templates...")

        args = {
            "url": "{0}/template?{1}".format(CONFIG['dojot']['url'], attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved all templates")

        return rc, res

    @staticmethod
    def get_template(jwt: str, template_id: int) -> tuple:
        """
        Retrieves all information from a specific template

        Parameters:
            jwt: Dojot JWT token
            template_id: template id
            """
        LOGGER.debug("Retrieving information from a specific template...")

        args = {
            "url": "{0}/template/{1}".format(CONFIG['dojot']['url'], str(template_id)),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved information from a specific template")

        return rc, res

    @staticmethod
    def get_template_with_parameters(jwt: str, template_id: int, attrs: str) -> tuple:
        """
        Retrieves template info.

        Parameters:
            jwt: Dojot JWT token
            template_id: template id
            attrs: optional parameters
            """
        LOGGER.debug("Retrieving template...")

        args = {
            "url": "{0}/template/{1}?{2}".format(CONFIG['dojot']['url'], str(template_id), attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved template")

        return rc, res

    @staticmethod
    def create_devices_with_parameters(jwt: str, template_id: str or list, label: str, attrs: str) -> tuple:
        """
        Create a device in Dojot.

        Parameters:
            jwt: JWT authorization.
            template_id: template to be used by the device.
            label: name for the device in Dojot.
            attrs: optional parameters

        Returns the created device ID or a error message.
        """
        LOGGER.debug("Creating multiple devices...")

        if type(template_id) != list:
            template_id = [template_id]

        args = {
            "url": "{0}/device?{1}".format(CONFIG['dojot']['url'], attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": json.dumps({
                "templates": template_id,
                "attrs": {},
                "label": label,
            }),
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... devices created ")
        return result_code, res

    @staticmethod
    def get_all_devices(jwt: str) -> tuple:
        """
        Retrieves all devices in Dojot.

        Parameters:
            jwt: JWT authorization.

        Returns the created device ID or a error message.
        """
        LOGGER.debug("Listing all devices...")

        args = {
            "url": "{0}/device".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... devices created ")
        return result_code, res

    @staticmethod
    def get_single_device(jwt: str, device_id: str) -> tuple:
        """
        Retrieves a device in Dojot.

        Parameters:
            jwt: JWT authorization.
            device_id: device id
        Returns the created device ID or a error message.
        """
        LOGGER.debug("Listing device info...")

        args = {
            "url": "{0}/device/{1}".format(CONFIG['dojot']['url'], device_id),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... device retrieved ")
        return result_code, res

    @staticmethod
    def get_devices_with_parameters(jwt: str, attrs: str) -> tuple:
        """
        Retrieves all templates.

        Parameters:
            jwt: Dojot JWT token
            attrs: optional parameters

            """
        LOGGER.debug("Retrieving devices...")

        args = {
            "url": "{0}/device{1}".format(CONFIG['dojot']['url'], attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("...devices retrieved")

        return rc, res

    @staticmethod
    def update_device(jwt: str, device_id: str, data: str or dict) -> tuple:
        """

        Returns the updated device ID or a error message.
        """
        LOGGER.debug("Updating device...")

        if isinstance(data, dict):
            data = json.dumps(data)
        args = {
            "url": "{0}/device/{1}".format(CONFIG['dojot']['url'], device_id),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.put, args)

        LOGGER.debug("... updated the device")
        return result_code, res

    @staticmethod
    def get_history_device(jwt: str, label: str, attrs: str or list = None, datefrom: str = None, dateto: str = None,
                           lastn: int = None, firstn: int = None) -> tuple:
        """
        Retrieves device attributes data from Dojot.

        Parameters:
            jwt: Dojot JWT token
            label: Dojot device label
            attrs: Device attribute to be requested. If not used, returns all attributes.
            datefrom: Start time of a time-based query
            dateto: End time of a time-based query
            lastn: Number of most current values (valid for each attribute, if more than one). You can use lastN with
            or without dateFrom/dateTo.
            firstn: Number of oldest values (valid for each attribute, if more than one). You can use firstN with
            or without dateFrom/dateTo.

            """
        LOGGER.debug("Retrieving history...")

        # /device/{device_id}/history?lastN={lastN}&attr={attr}&dateFrom={dateFrom}&dateTo={dateTo}
        url = "{0}/history/device/{1}/history?".format(CONFIG['dojot']['url'], label)
        if attrs is not None:
            if type(attrs) is str:
                attrs = [attrs]
            url = url + "attr=" + ",".join(attrs) + "&"

        if lastn is not None:
            url = url + "lastN=" + str(lastn) + "&"

        if firstn is not None:
            url = url + "firstN=" + str(firstn) + "&"

        if datefrom is not None:
            url = url + "dateFrom=" + datefrom + "&"

        if dateto is not None:
            url = url + "dateTo=" + dateto + "&"

        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved history")

        return rc, res

    @staticmethod
    def configure_device(jwt: str, device_id: str, data: str or dict) -> tuple:
        """

        Returns the configured device or a error message.
        """
        LOGGER.debug("configuring device...")

        if isinstance(data, dict):
            data = json.dumps(data)
        args = {
            "url": "{0}/device/{1}/actuate".format(CONFIG['dojot']['url'], device_id),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.put, args)

        LOGGER.debug("... configured device")
        return result_code, res

    @staticmethod
    def get_certificates(jwt: str) -> tuple:
        """
        Retrieves all certificates in Dojot.

        Parameters:
            jwt: JWT authorization.

        Returns the certificates or a error message.
        """
        LOGGER.debug("Listing all certificates...")

        args = {
            "url": "{0}/x509/v1/certificates".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved certificates")
        return result_code, res

    @staticmethod
    def get_certificates_with_parameters(jwt: str, attrs: str) -> tuple:
        """

        Parameters:
            jwt: Dojot JWT token
            attrs: optional parameters

            """
        LOGGER.debug("Retrieving certificates with parameters...")

        args = {
            "url": "{0}/x509/v1/certificates?{1}".format(CONFIG['dojot']['url'], attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved certificates with parameters")

        return result_code, res

    @staticmethod
    def get_certificate(jwt: str, fingerprint: str) -> tuple:
        """
        Retrieves all certificates in Dojot.

        Parameters:
            jwt: JWT authorization.

        Returns the certificates or a error message.
        """
        LOGGER.debug("Listing specific certificate...")

        args = {
            "url": "{0}/x509/v1/certificates/{1}".format(CONFIG['dojot']['url'], fingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved certificate")
        return result_code, res

    @staticmethod
    def get_certificate_with_parameters(jwt: str, fingerprint: str, attrs: str) -> tuple:
        """

        Parameters:
            jwt: Dojot JWT token
            attrs: optional parameters

            """
        LOGGER.debug("Retrieving certificate with parameters...")

        args = {
            "url": "{0}/x509/v1/certificates/{1}?{2}".format(CONFIG['dojot']['url'], fingerprint, attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved certificate with parameters")

        return result_code, res

    @staticmethod
    def create_certificate(jwt: str, data: dict or str) -> tuple:
        """
        Create the device certificate

        Returns the fingerprint or a error message.
        """
        LOGGER.debug("Creating certificate...")

        if isinstance(data, dict):
            data = json.dumps(data)

        if isinstance(data, str):
            data = json.dumps({
                "csr": data
            })

        args = {
            "url": "{0}/x509/v1/certificates".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... created the certificate")

        return result_code, res

    @staticmethod
    def register_external_certificate(jwt: str, caFingerprint: str, certificateChain: str, device_id: str = None) -> str: # tuple:
        """
        Registers a x.509 certificate issued by a CA previously registered

        Returns the certificateFingerprint or a error message.
        """
        LOGGER.debug("Registering certificate...")

        if device_id is not None:
            device_id = str(device_id)

        data = {
            "caFingerprint": str(caFingerprint),
            "certificateChain": str(certificateChain),
            "belongsTo": {
                "device": device_id
            }
        }

        args = {
            "url": "{0}/x509/v1/certificates".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": json.dumps(data),
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... registered the certificate")

        return result_code, res

    @staticmethod
    def get_external_certificates(jwt: str, caFingerprint: str) -> tuple:
        """
        Retrieves all external certificates in Dojot.

        Parameters:
            jwt: JWT authorization.

        Returns the certificates or a error message.
        """
        LOGGER.debug("Listing all external certificates...")

        args = {
            "url": "{0}/x509/v1/certificates?cafingerprint={1}".format(CONFIG['dojot']['url'], caFingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved external certificates")
        return result_code, res

    @staticmethod
    def delete_certificates(jwt: str) -> tuple:
        """
        Delete all certificates.
        """
        LOGGER.debug("Deleting certificates...")

        args = {
            "url": "{0}/x509/v1/certificates".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... deleted certificates")
        return result_code, res

    @staticmethod
    def delete_certificate(jwt: str, fingerprint: str) -> tuple:
        """
        Delete certificate.
        """
        LOGGER.debug("Deleting certificate...")

        args = {
            "url": "{0}/x509/v1/certificates/{1}".format(CONFIG['dojot']['url'], fingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... deleted certificate")
        return result_code, res

    @staticmethod
    def associate_certificate(jwt: str, fingerprint: str, device_id: str) -> tuple:
        """

        Returns the updated device ID or a error message.
        """
        LOGGER.debug("Associating certificate...")

        data = json.dumps({
            "belongsTo": {
                "device": device_id
            }
        })

        args = {
            "url": "{0}/x509/v1/certificates/{1}".format(CONFIG['dojot']['url'], fingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data
        }

        result_code, res = DojotAPI.call_api(requests.patch, args)

        LOGGER.debug("... associated certificate")
        return result_code, res


    @staticmethod
    def disassociate_certificate(jwt: str, fingerprint: str) -> tuple:
        """
        disassociate a device with a certificate
        Returns the updated device ID or a error message.
        """
        LOGGER.debug("disassociate a device with a certificate...")

        data = json.dumps({
            "belongsTo": {
                "device": None
            }
        })
        args = {
            "url": "{0}/x509/v1/certificates/{1}/belongsto".format(CONFIG['dojot']['url'], fingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... associated certificate")
        return result_code, res

    @staticmethod
    def get_schemas(jwt: str) -> tuple:
        """
        Obtains the JSON schemas.

        Parameters:
            jwt: JWT authorization.

        Returns schemas or a error message.
        """
        LOGGER.debug("Obtaining schemas ...")

        args = {
            "url": "{0}/x509/v1/schemas".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... done")
        return result_code, res

    @staticmethod
    def get_ca(jwt: str) -> tuple:
        """
        Retrieves root CA in Dojot.

        Parameters:
            jwt: JWT authorization.

        Returns the certificate or a error message.
        """
        LOGGER.debug("Listing root CA ...")

        args = {
            "url": "{0}/x509/v1/ca".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... done")
        return result_code, res

    @staticmethod
    def get_crl(jwt: str) -> tuple:
        """
        Retrieves latest CRL.

        Parameters:
            jwt: JWT authorization.

        Returns the certificate or a error message.
        """
        LOGGER.debug("Listing latest CRL ...")

        args = {
            "url": "{0}/x509/v1/ca/crl".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... done")
        return result_code, res

    @staticmethod
    def register_trusted_ca(jwt: str, ca_pem: str, allow_auto_registration: bool) -> tuple:
        """
        Registers a trusted CA certificate

        Returns the fingerprint or a error message.
        """
        LOGGER.debug("Registering a trusted CA certificate...")

        data = {
            "caPem": ca_pem,
            "allowAutoRegistration": allow_auto_registration
        }

        args = {
            "url": "{0}/x509/v1/trusted-cas".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": json.dumps(data),
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... registered certificate")
        return result_code, res

    @staticmethod
    def delete_trusted_ca(jwt: str, caFingerprint: str) -> tuple:
        """
        Remove a trusted CA certificate

        """
        LOGGER.debug("Removing a trusted CA certificate...")

        args = {
            "url": "{0}/x509/v1/trusted-cas/{1}".format(CONFIG['dojot']['url'], caFingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt)
            }
        }

        result_code, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... done")
        return result_code, res

    @staticmethod
    def get_trusted_cas(jwt: str) -> tuple:
        """
        Listing a trusted CA certificates

        """
        LOGGER.debug("Listing a trusted CA certificates...")

        args = {
            "url": "{0}/x509/v1/trusted-cas".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... done")
        return result_code, res

    @staticmethod
    def get_trusted_cas_with_parameters(jwt: str, attrs: str) -> tuple:
        """
        Listing a trusted CA certificates

        """
        LOGGER.debug("Listing a trusted CAs certificates with parameters...")

        args = {
            "url": "{0}/x509/v1/trusted-cas?{1}".format(CONFIG['dojot']['url'], attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved CAs with parameters")
        return result_code, res

    @staticmethod
    def get_trusted_ca(jwt: str, caFingerprint: str) -> tuple:
        """
        Get a trusted CA certificate

        """
        LOGGER.debug("Getting a trusted CA certificate...")

        args = {
            "url": "{0}/x509/v1/trusted-cas/{1}".format(CONFIG['dojot']['url'], caFingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt)
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... done")
        return result_code, res

    @staticmethod
    def get_trusted_ca_with_parameters(jwt: str, fingerprint: str, attrs: str) -> tuple:
        """

        Parameters:
            jwt: Dojot JWT token
            fingerprint: CA fingerprint
            attrs: optional parameters

            """
        LOGGER.debug("Listing a trusted CA certificate with parameters...")

        args = {
            "url": "{0}/x509/v1/trusted-cas/{1}?{2}".format(CONFIG['dojot']['url'], fingerprint, attrs),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved CA with parameters")

        return result_code, res

    @staticmethod
    def update_trusted_ca(jwt: str, caFingerprint: str, value: bool) -> tuple:
        """

        Returns the updated trusted CA or a error message.
        """
        LOGGER.debug("Updating trusted CA...")

        data = {
            "allowAutoRegistration": value
        }

        args = {
            "url": "{0}/x509/v1/trusted-cas/{1}".format(CONFIG['dojot']['url'], caFingerprint),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": json.dumps(data)
        }

        result_code, res = DojotAPI.call_api(requests.patch, args)

        LOGGER.debug("... updated trusted CA")
        return result_code, res

    @staticmethod
    def create_remote_node(jwt: str, data: dict) -> tuple:
        """
        Create a remote node in Dojot.

        Parameters:
            jwt: JWT authorization.



        Returns the created remote node
        """
        LOGGER.debug("Creating remote node...")

        if isinstance(data, dict):
            data = json.dumps(data)

        args = {
            "url": "{0}/flows/v1/node".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... remote node created")
        return result_code, res

    @staticmethod
    def remove_remote_nodes(jwt: str) -> tuple:
        """
        Remove all remote nodes
        """
        LOGGER.debug("Removing all remote nodes...")

        args = {
            "url": "{0}/flows/v1/node".format(CONFIG['dojot']['url']),
            "headers": {
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("... deleted remote nodes")
        return rc, res

    @staticmethod
    def import_data(jwt: str, data: dict) -> tuple:
        """
        Import a database in Dojot.

        Parameters:
            jwt: JWT authorization.

        Returns the imported data
        """
        LOGGER.debug("Importing database...")

        if isinstance(data, dict):
            data = json.dumps(data)

        args = {
            "url": "{0}/import".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... data imported. Result code: " + str(result_code))

        return result_code, res

    @staticmethod
    def get_history_notifications(jwt: str) -> tuple:
        """
        Retrieves notifications.

        Parameters:
            jwt: Dojot JWT token

        """
        LOGGER.debug("Retrieving notifications...")

        url = "{0}/history/notifications/history?limit=25".format(CONFIG['dojot']['url'])

        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
                }
            }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved notifications")

        return rc, res

    @staticmethod
    def get_users(jwt: str) -> tuple:
        """
        Retrieves users.

        Parameters:
            jwt: Dojot JWT token

        """
        LOGGER.debug("Retrieving users...")

        url = "{0}/auth/user".format(CONFIG['dojot']['url'])

        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
                }
            }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved users")

        return rc, res

    @staticmethod
    def get_tenants(jwt: str) -> tuple:
        """
        Retrieves tenants.

        Parameters:
            jwt: Dojot JWT token

        """
        LOGGER.debug("Retrieving tenants...")

        url = "{0}/auth/admin/tenants".format(CONFIG['dojot']['url'])

        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
                }
            }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved users")

        return rc, res

    @staticmethod
    def get_profiles(jwt: str) -> tuple:
        """
        Retrieves profiles.

        Parameters:
            jwt: Dojot JWT token

        """
        LOGGER.debug("Retrieving profiles...")

        url = "{0}/auth/pap/group".format(CONFIG['dojot']['url'])

        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
                }
            }

        rc, res = DojotAPI.call_api(requests.get, args)
        LOGGER.debug("... retrieved profiles")

        return rc, res

    @staticmethod
    def get_retriever_device_attr(jwt: str, device_id: str, attr: str, datefrom: str = None, dateto: str = None,
                           limit: int = None, order: str = None) -> tuple:
        """
        Retrieves device attribute data stored in influxbd

        Parameters:
            jwt: Dojot JWT token
            device_id: Dojot device id
            attr: Device attribute to be requested.
            datefrom: Start time of a time-based query
            dateto: End time of a time-based query
            limit: Number of the most current values. If order = asc, it is the number of oldest values. You can use limit with or without dateFrom/dateTo.

            """
        LOGGER.debug("Retrieving data stored in influxbd ...")

        # /tss/v1/devices/{device_id}/attrs/{attr}/data?limit={limit}&order={order}&dateFrom={dateFrom}&dateTo={dateTo}
        url = "{0}/tss/v1/devices/{1}/attrs/{2}/data?".format(CONFIG['dojot']['url'], device_id, attr)

        if limit is not None:
            url = url + "limit=" + str(limit) + "&"

        if order is not None:
            url = url + "order=" + str(order) + "&"

        if datefrom is not None:
            url = url + "dateFrom=" + datefrom + "&"

        if dateto is not None:
            url = url + "dateTo=" + dateto + "&"

        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        rc, res = DojotAPI.call_api(requests.get, args)

        LOGGER.debug("... retrieved data")

        return rc, res

    @staticmethod
    def get_credentials_without_body(jwt: str, content: None or str) -> tuple:
        """
        Request a credentials with parameters's default values.
        Returns the credentials or a error message.
        """
        LOGGER.debug("Requesting credentials...")

        if content is None:
            content = "application/json"

        args = {
            "url": "{0}/api/v1/credentials".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "{0}".format(content),
                "Authorization": "Bearer {0}".format(jwt),
            }
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... retrieved the credentials")

        return result_code, res

    @staticmethod
    def get_credentials(jwt: str, data: dict) -> tuple:
        """
        Request a credentials.
        Returns the credentials or a error message.
        """
        LOGGER.debug("Requesting credentials...")

        if isinstance(data, dict):
            data = json.dumps(data)

        args = {
            "url": "{0}/api/v1/credentials".format(CONFIG['dojot']['url']),
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt),
            },
            "data": data,
        }

        result_code, res = DojotAPI.call_api(requests.post, args)

        LOGGER.debug("... retrieved the credentials")

        return result_code, res


    @staticmethod
    def upload_file(jwt: str, filePath: str, path: str) -> tuple:
        """
        Returns the uploaded file or a error message.
        """
        LOGGER.debug("Uploading file...")

        # setting url

        url = "{0}/file-mgmt/api/v1/files/upload".format(CONFIG['dojot']['url'])


        # setting args


        args = {
            "url": url,
            "headers": {
                "Authorization": "Bearer {0}".format(jwt)
            },
            "files": {'file': open(filePath, 'rb')},
            "data": {
                "path": path
            }
        }


        LOGGER.debug("sending request...")
        result_code, res = DojotAPI.call_api(requests.put, args)


        LOGGER.debug("...done ")
        return result_code, res

    @staticmethod
    def list_stored_files(jwt: str, limit: int) -> tuple:
        """
        Returns the uploaded file or a error message.
        """
        LOGGER.debug("Listing stored files...")

        # setting url

        url = "{0}/file-mgmt/api/v1/files/list?limit={1}".format(CONFIG['dojot']['url'], limit)


        # setting args


        args = {
            "url": url,
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(jwt)
            }
        }


        LOGGER.debug("sending request...")
        result_code, res = DojotAPI.call_api(requests.get, args)


        LOGGER.debug("...done ")
        return result_code, res

    @staticmethod
    def remove_stored_file(jwt: str, path: str) -> tuple:
        """

        """
        LOGGER.debug("Removing file...")

        # setting url

        url = "{0}/file-mgmt/api/v1/files/remove?path={1}".format(CONFIG['dojot']['url'], path)

        # setting args

        args = {
            "url": url,
            "headers": {
                "Authorization": "Bearer {0}".format(jwt)
            }
        }

        LOGGER.debug("sending request...")
        result_code, res = DojotAPI.call_api(requests.delete, args)

        LOGGER.debug("...done ")
        return result_code, res

    @staticmethod
    def download_file(jwt: str, filename: str, path: str) -> int:
        """
        Returns the downloaded file or a error message.
        """
        LOGGER.debug("Downloading file...")

        # setting url

        url = "{0}/file-mgmt/api/v1/files/download".format(CONFIG['dojot']['url'])


        # setting args

        args = {
            "url": url,
            "headers": {
                "Authorization": "Bearer {0}".format(jwt),
                "accept": "Any"
            },
            "data": {
                "alt": "media",
                "path": path
            }
        }


        LOGGER.debug("sending request...")
#        rc, res = DojotAPI.call_api(requests.get, args)
        response = requests.get(url, params={"alt": "media", "path": path}, headers={"Authorization": "Bearer {0}".format(jwt), "accept": "Any"})
        open(filename, 'wb').write(response.content)



        LOGGER.debug("...done ")
        return response.status_code
#        return rc, res


    @staticmethod
    def divide_loads(total: int, batch: int) -> List:
        """
        Divides `n` in a list with each element being up to `batch`.
        """
        loads = []

        if total > batch:
            iterations = total // batch
            exceeding = total % batch
            # This will create a list with the number `batch` repeated `iterations` times
            # and then `exceeding` at the final
            loads = [batch] * iterations
            if exceeding > 0:
                loads.append(exceeding)

        else:
            loads.append(total)

        return loads

    @staticmethod
    def call_api(func: Callable[..., requests.Response], args: dict) -> tuple:
        """
        Calls the Dojot API using `func` and `args`.

        Parameters:
            func: function to call Dojot API.
            args: dictionary of arguments to `func`

        Returns the response in a dictionary
        """
        for _ in range(CONFIG['dojot']['api']['retries'] + 1):
            try:
                res = func(**args)

            except Exception as exception:
                LOGGER.debug(str(exception))
                gevent.sleep(CONFIG['dojot']['api']['time'])

            else:
                # return res.status_code, res.json()
                return res.status_code, res.json() if res.status_code != 204 else None

        raise APICallError("exceeded the number of retries to {0}".format(args['url']))
