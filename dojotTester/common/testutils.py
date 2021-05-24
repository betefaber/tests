from dojot.api import DojotAPI as Api


def add_a_simple_device(self, template=None, label="SimpleDevice"):
    self.logger.info('Executing Api dummy test...')
    jwt = Api.get_jwt()
    self.logger.info("JWT = " + jwt)
    self.assertTrue(jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
    if template is None:
        template = add_a_simple_template(self)

    rc, res = Api.create_device(jwt, template, label)
    self.assertTrue(rc == 200, f"** FAILED ASSERTION: failure to add device {label}**")

    return res["devices"][0]["id"]


def add_a_simple_template(self, label="SimpleTemplate"):
    self.logger.info('Executing Api dummy test...')
    jwt = Api.get_jwt()
    self.logger.info("JWT = " + jwt)
    self.assertTrue(jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

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
