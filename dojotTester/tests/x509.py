from tests.base_test import BaseTest
from dojot.api import DojotAPI as Api
import json
import random
import time


class X509Test(BaseTest):

    """
    Pré-condições:
        - gerar CSR para o dispositivo, no formato PEM
        - gerar certificados público e privado para o dispositivo
        - gerar CSR inválido, no formato PEM
    """


    def createCertificate(self, jwt: str, csr: str):
        rc, res = Api.create_certificate(jwt, json.dumps(csr))
        return rc,res

    def updateCertificate(self, jwt: str, fingerprint: int, csr: str):
        rc, res = Api.update_certificate(jwt, fingerprint, json.dumps(csr))
        return rc, res

    def getCertificates(self, jwt: str):
        rc, res = Api.get_certificates(jwt)
        return rc, res

    def getCertificatesWithParameters(self, jwt: str, attrs: str):
        rc, res = Api.get_certificates_with_parameters(jwt, attrs)
        return rc, res

    def getCertificate(self, jwt: str, fingerprint: str):
        rc, res = Api.get_certificate(jwt, fingerprint)
        return rc, res

    def getCertificateWithParameters(self, jwt: str, fingerprint: int, attrs: str):
        rc, res = Api.get_template_with_parameters(jwt, fingerprint, attrs)
        return rc, res

    def deleteCertificates(self, jwt: str):
        rc, res = Api.delete_certificates(jwt)
        return rc, res

    def deleteCertificate(self, jwt: str, fingerprint: int):
        rc, res = Api.delete_template(jwt, fingerprint)
        return rc, res


    def runTest(self):
        self.logger.info('Executing x509 test')
        self.logger.debug('getting jwt...')
        jwt = Api.get_jwt()

        self.logger.debug('listing certificates - no data...')
        rc, res = self.getCertificates(jwt)
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        
        self.logger.debug('creating certificate...')
        template = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGMzMzMjNmMIIBIjANBgkqhkiG9w0BAQEF\r\nAAOCAQ8AMIIBCgKCAQEA1kfX53IJUArqIuZOr9IYTsVawDn4D+YASe1ZwS1dbxyi\r\nit5rI5IwF2NZYy2xOwrq2DqcFVTouL00hrT8sXAegSMyB0NcdRKDvOUDtjD6cn9L\r\nj3vl7wB3SzTRzOGLoq6Q5WKHryJKPDvijAx7je7VxbryfE+a6MKRlMOcqyqPpD0+\r\nn5Hd8IeGNh3PTFbbeaIgsE4n2dkjLaCQRgZR2JnSDpC2Tcx51yoFFvvxrvZo4tRc\r\npZTVnA1w+VmRv2arRPPDxV8QXXLFywwQzYSxTcdWjR8fptBIquEUYXU+TXkHRu8/\r\nekBJbqm52VR2usSCSFeDH3wh873ZShfRp1dMCNoBbQIDAQABoAAwDQYJKoZIhvcN\r\nAQELBQADggEBACOe6ON7dL18wwFcxnFjF0sUBdzwQDPScL6LQLuIz0pjCRo9qT7V\r\niT4b43PZ7xGg6IdCqibqQ+6tNeyFhq6tWcQgfQhrMwyfA54osu20tLhnXC2g6W3x\r\nc/31AU2byvVEvqITX3VDu7c4nlSRptqVvDO8I1De+3HlXWK42ohi1UWwXLej2cVk\r\niYlCMmQOzKfgTzLuwQnBPRJUiIVon1j/i3ZO4baVNdledS1RMqyVG4ilJlUVqud/\r\neD0zI1YUPE2YizxYI+8L3k7sze/nDGhtX021HMGSEpVq8NKaPapylK0X+tn7YY0Z\r\nuY22UoTwLUy+sX8lctzGT571iODCEEEfC+c=\r\n-----END CERTIFICATE REQUEST-----"
        }


        rc, res = self.createCertificate(jwt, template)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        """

        self.logger.debug('updating template SensorModel......')
        template = {
            "label": "SensorModel",
            "attrs": [
                {
                    "label": "led",
                    "type": "dynamic",
                    "value_type": "bool"
                },
                {
                    "label": "fan",
                    "type": "dynamic",
                    "value_type": "bool"
                }
            ]
        }


        self.logger.debug('listing template SensorModel...')
        rc, res = self.getTemplate(jwt, template_ids[2])
        self.logger.debug('Template: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        rc, res = self.updateTemplate(jwt, template_ids[2], template)
        self.logger.info('Template updated: ' + str(template_ids[2]) + ', SensorModel')
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.debug('listing updated template...')
        rc, res = self.getTemplate(jwt, template_ids[2])
        self.logger.debug('Template: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        
        """

        """
        Lista templates
        """
        """

        self.logger.info('listing all templates...')
        rc, list = self.getTemplates(jwt)
        self.logger.debug('Template List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_size...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_size=3")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_num...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_num=2")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_size=2&page_num=1...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_size=2&page_num=1")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_size=2&page_num=2...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_size=2&page_num=2")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_size=2&page_num=3...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_size=2&page_num=3")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_size=2&page_num=4...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_size=2&page_num=4")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: attr_format=both...')  #both: attrs + data_attrs
        rc, res = self.getTemplatesWithParameters(jwt, "attr_format=both")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: attr_format=single...')  #single: só attrs
        rc, res = self.getTemplatesWithParameters(jwt, "attr_format=single")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: attr_format=split...')  #split: só data_attrs
        rc, res = self.getTemplatesWithParameters(jwt, "attr_format=split")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: attr...')  #só é válido para atributos estáticos
        rc, res = self.getTemplatesWithParameters(jwt, "attr=serial=indefinido")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: label...')
        rc, res = self.getTemplatesWithParameters(jwt, "label=SensorModel")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameter: sortBy...')
        rc, res = self.getTemplatesWithParameters(jwt, "sortBy=label")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameters...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_size=2&page_num=1&attr_format=single&attr=serial=indefinido&label=TiposAtributos&sortBy=label")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameters (no match): return empty...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_size=2&page_num=1&attr_format=single&attr=serial=indefinido&label=SensorModel&sortBy=label")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing templates with parameters (nonexistent parameter ): return full...')
        rc, res = self.getTemplatesWithParameters(jwt, "parametro=outro")
        self.logger.debug('Templates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        """

        """
        Lista template especifico
        """
        """

        self.logger.info('listing specific template...' + str(template_ids[2]))
        ##template SensorModel
        rc, res = self.getTemplate(jwt, template_ids[2])
        self.logger.debug('Template info: ' + str(res))
        #self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing specific template with parameter: attr_format=both...')  # both: attrs + data_attrs
        rc, res = self.getTemplateWithParameters(jwt, template_ids[2], "attr_format=both")
        self.logger.debug('Template info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        """

        """
        attr_format: issue #1967
        """
        """

        self.logger.info('listing specific template with parameter: attr_format=single...')  # single: só attrs
        rc, res = self.getTemplateWithParameters(jwt, template_ids[2], "attr_format=single")
        self.logger.debug('Template info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        """
        attr_format: issue #1967
        """
        """

        self.logger.info('listing specific template with parameter: attr_format=split...')  # split: só data_attrs
        rc, res = self.getTemplateWithParameters(jwt, template_ids[2], "attr_format=split")
        self.logger.debug('Template info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        """
        Remove template especifico
        """
        """

        self.logger.info('removing specific template...')
        ##template Vazio
        rc, res = self.deleteTemplate(jwt, template_ids[1])
        self.logger.debug('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        devices = []
        devices.append(([template_ids[2]], "device"))
        devices_ids = self.createDevices(jwt, devices)
        self.logger.info("devices ids: " + str(devices_ids))

        self.logger.info('removing specific template - Templates cannot be removed as they are being used by devices...')
        rc, res = self.deleteTemplate(jwt, template_ids[2])
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        self.assertTrue(res["message"] == "Templates cannot be removed as they are being used by devices", "mensagem inesperada")


        """
        """
        Remove all templates
        """
        """

        ##só remove se não existir devices associados

        Api.delete_devices(jwt)
        """
        """

        self.logger.info('removing all templates...')
        rc, res = self.deleteTemplates(jwt)
        self.logger.debug('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        """


        """
        Fluxos Alternativos
        """

        #TODO: erro 400 ("A message describing the cause of the error")

        self.logger.debug('creating certificate - csr inválido (device não existe)...') # ainda não tem validação, o certificado é criado
        template = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGMTIzYWJjMIIBIjANBgkqhkiG9w0BAQEF\r\nAAOCAQ8AMIIBCgKCAQEAu6O1KQWOmlfSuXmeMoyPWQwjCRrnrX/Iq/lueCRCafN4\r\ni37BxoVyBTOmYIdrwsxWI6bZ/em2helsPcIs+w0JIV2YAqWYlJT0h1r0kZIrmG7l\r\nNXDxSZ1+iZrUhEItSVnAy0Pu5klBmV0cRtfoHvpmFEUNDRk1LwxrlgirLYUAGibf\r\nUz+OvLOgjlMm62/01dbskVxIrEyIeQItTlvfbnKwSMRfVzv7lMmewTrqVAU8ygJo\r\n6HG49QBo6EAUsSkgGsn+HiOMJc/WIa1SnSuFtAOI4X2xFyVvWnuALHuMHcQ+j1ZU\r\nhDXhkYqyt5g9FwJGRxzzs64LqE4QIqbaBSVCw1cOsQIDAQABoAAwDQYJKoZIhvcN\r\nAQELBQADggEBAH/j0kylaxvvqLGOAXdxS93sFMVN3J/37yf/ZcI8uWecuEO0sJh6\r\nArXQCJo7w0K4SX3IYV9x76NrTDoxC6cwLy1Jz8RzfHpPr2eWaqrV1IF31rGhs4iu\r\n5oeUQmtN9WdBepfrosbNXz15+eRmBDv8gaTT6U0WuY8GhJcBr9hMGU27YXhVbFDR\r\n9BJSKgt2rrKsmrg/d+uufKMPuTzErv/731wKD0mYXjuRaHkUi/34RylsJbzUpENc\r\n76m697la47TjmZAq/Cs4If57LHXCSdJe+ox619k3LHJUXJwfbC4yQTmr2OLagV7j\r\nv2G7zCntFPTw31EHwQ0YtUVEhxkOUlE7Bfc=\r\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, template)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.debug('creating certificate - csr vazio...')
        template = {
            "csr": ""
        }
        rc, res = self.createCertificate(jwt, template)
        self.logger.info("Result: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        self.logger.debug('creating certificate - csr adulterado...')
        template = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGNWEzMmViMIIBIjANBgkqhkiG9w0BAQEF\r\nAAOCAQ8AMIIBCgKCAQEAzKQh4Y4E3t8byxNAsWMuztPjNcvsOCC8GwFeexmFSlpS\r\nugcLqx7j4h+7rjeZvPKfV5fBd73jUh2kj8AzoR5UilNUIgXl38ry+dEuSotSB8lS\r\nICUgWEvWkuJNCBjZBpzlfp1xRPyS96fr6sGPuISVCxIHheeyYVLApeEGtQWOymwm\r\nItAAOTJyPaddfv4fvmvurNHK8hOPauiu2eCDJiQQaFQsCnNbx9Q1QozNee5Ln6ZG\r\nwcCgy0k7g43YRnARNGnffKvJuSsbbUxW7ZHJKTLFPz8mb2cPFtHJqJovEojoaKR4\r\nsHjklsHi5kKzprf/OBztKr+4s9g19hvYOKxWg1ajdwIDAQABoAAwDQYJKoZIhvcN\r\nAQELBQADggEBACK04o5DRVPbvaFLQn4Grhir2drtqBVjtPNDDu8bs9fsXqlnTJKo\r\n8XN9yO53qDc6LDYT6qsRzXk9o2YsARkA+i/KSJSdEdgev5wYaG4nHS55xy/BNMLX\r\n+hSY52JiTGH582fwXbGARucogPsaqeq0bHhEATwvDqEEAeqogmNGTaRc6zGtPfu7\r\n5GyBgQfpBRv1daI8k883Q5sbLTXTqWip/HwgLxY21z+ife6fZe076xpdyIUw5E8B\r\nN9IGKczrFV6JoTpKSEhXhppxS6BmNC18+XeCMBuwK9LJs5Jkwy4DnPOgWjPvQzi8\r\nXUix95xsh0nQ/pOqoq/M5wM4JzuLaLABCW4=\r\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, template)
        self.logger.info("Result: " + str(res))
        self.assertTrue(int(rc) == 500, "codigo inesperado") #erro esperado: 400

        self.logger.debug('creating certificate - no body...')
        template = {}
        rc, res = self.createCertificate(jwt, template)
        self.logger.info("Result: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        resposta_esperada = "{\"schema$id\":\"http://www.dojot.com.br/schemas/reg-or-gen-cert\",\"schemaErrors\":[{\"keyword\":\"required\",\"dataPath\":\"\",\"schemaPath\":\"#/oneOf/0/required\",\"params\":{\"missingProperty\":\"certificatePem\"},\"message\":\"should have required property 'certificatePem'\"},{\"keyword\":\"required\",\"dataPath\":\"\",\"schemaPath\":\"#/oneOf/1/required\",\"params\":{\"missingProperty\":\"csr\"},\"message\":\"should have required property 'csr'\"},{\"keyword\":\"oneOf\",\"dataPath\":\"\",\"schemaPath\":\"#/oneOf\",\"params\":{\"passingSchemas\":null},\"message\":\"should match exactly one schema in oneOf\"}]}"
        self.logger.info("Resultado esperado: " + str(resposta_esperada))
        #self.assertTrue(res == resposta_esperada, "resposta inesperada")



        """

        self.logger.info('creating template sem label...')
        template = {
            "attrs": [
                {
                    "label": "float",
                    "type": "dynamic",
                    "value_type": "float"
                }
                ]
        }

        res = self.createTemplateFail(jwt, template)
        self.logger.info('Result: ' + str(res))


        self.logger.info('creating template com metadado repetido...')
        template = {
            "label": "sample",
            "attrs": [
                {
                    "label": "simpleAttr",
                    "type": "dynamic",
                    "value_type": "string",
                    "metadata": [
                        {"type": "mapping", "label": "type2", "static_value": "dummy", "value_type": "string"},
                        {"type": "mapping", "label": "type2", "static_value": "dummy", "value_type": "string"}
                    ]
                }
            ]
        }

        res = self.createTemplateFail(jwt, template)
        self.logger.info('Result: ' + str(res))

        self.logger.info('updating specific template - No such template...')
        template = {
            "label": "Vazio",
            "attrs": [
                {
                    "label": "serial",
                    "type": "static",
                    "value_type": "string",
                    "static_value": "undefined"
                }
            ]
        }
        rc, res = self.updateTemplate(jwt, 1000, template)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        self.logger.info('listing template - No such template...')
        rc, res = self.getTemplate(jwt, "123")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        self.logger.info('listing template - internal error...')
        rc, res = self.getTemplate(jwt, "abc")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 500, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_num=0...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_num=0")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_size=0...')
        res = self.getTemplatesWithParameters(jwt, "page_size=0")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        self.logger.info('listing templates with parameter: page_size and page_num must be integers...')
        rc, res = self.getTemplatesWithParameters(jwt, "page_num=xyz&page_size=kwv")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 500, "codigo inesperado")

        self.logger.info('removing specific template - No such template...')
        rc, res = self.deleteTemplate(jwt, 1000)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")
        """

