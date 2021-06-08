from dojot.api import DojotAPI as Api


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

    # No data for the given attribute
    if rc == 404 and res["description"] == "No data for the given attribute could be found":
        return rc, 0

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to get history from device" + dev_id + " **")

    return rc, len(res)

def get_history_last_attr(self, jwt: str, dev_id: str, attr: str) -> tuple:
    rc, res = Api.get_history_device(jwt, dev_id, attr, lastn=1)

    # No data for the given attribute
    if rc == 404 and res["description"] == "No data for the given attribute could be found":
        return rc, None

    self.assertTrue(rc == 200, "** FAILED ASSERTION: failure to get history from device" + dev_id + " **")

    return rc, res[0]
