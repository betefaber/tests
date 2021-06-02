from common.base_test import BaseTest
from dojot.api import DojotAPI as Api
from mqtt.mqttClient import MQTTClient
import json


class X509Test(BaseTest):

    """
    Pré-condições:
        - gerar CSR para o dispositivo, no formato PEM
        - gerar certificados público e privado para o dispositivo
        - gerar CSR inválido, no formato PEM
    """

    def getCA(self, jwt: str):
        rc, res = Api.get_ca(jwt)
        return rc, res

    def getCRL(self, jwt: str):
        rc, res = Api.get_crl(jwt)
        return rc, res

    def createCertificate(self, jwt: str, csr: str):
        rc, res = Api.create_certificate(jwt, json.dumps(csr))
        return rc,res

    def associateCertificate(self, jwt: str, fingerprint: str, device_id: str):
        rc, res = Api.associate_certificate(jwt, fingerprint, device_id)
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

    def getCertificateWithParameters(self, jwt: str, fingerprint: str, attrs: str):
        rc, res = Api.get_certificate_with_parameters(jwt, fingerprint, attrs)
        return rc, res

    def deleteCertificates(self, jwt: str):
        rc, res = Api.delete_certificates(jwt)
        return rc, res

    def deleteCertificate(self, jwt: str, fingerprint: str):
        rc, res = Api.delete_certificate(jwt, fingerprint)
        return rc, res

    def registerTrustedCA(self, jwt: str, ca_pem: str, allow_auto_registration: bool):
        rc, res = Api.register_trusted_ca(jwt, ca_pem, allow_auto_registration)
        return rc, res

    def deleteTrustedCA(self, jwt: str, caFingerprint: str):
        rc, res = Api.delete_trusted_ca(jwt, caFingerprint)
        return rc, res

    def getTrustedCAs(self, jwt: str):
        rc, res = Api.get_trusted_cas(jwt)
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
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGMzMzMjNmMIIBIjANBgkqhkiG9w0BAQEF\r\nAAOCAQ8AMIIBCgKCAQEA1kfX53IJUArqIuZOr9IYTsVawDn4D+YASe1ZwS1dbxyi\r\nit5rI5IwF2NZYy2xOwrq2DqcFVTouL00hrT8sXAegSMyB0NcdRKDvOUDtjD6cn9L\r\nj3vl7wB3SzTRzOGLoq6Q5WKHryJKPDvijAx7je7VxbryfE+a6MKRlMOcqyqPpD0+\r\nn5Hd8IeGNh3PTFbbeaIgsE4n2dkjLaCQRgZR2JnSDpC2Tcx51yoFFvvxrvZo4tRc\r\npZTVnA1w+VmRv2arRPPDxV8QXXLFywwQzYSxTcdWjR8fptBIquEUYXU+TXkHRu8/\r\nekBJbqm52VR2usSCSFeDH3wh873ZShfRp1dMCNoBbQIDAQABoAAwDQYJKoZIhvcN\r\nAQELBQADggEBACOe6ON7dL18wwFcxnFjF0sUBdzwQDPScL6LQLuIz0pjCRo9qT7V\r\niT4b43PZ7xGg6IdCqibqQ+6tNeyFhq6tWcQgfQhrMwyfA54osu20tLhnXC2g6W3x\r\nc/31AU2byvVEvqITX3VDu7c4nlSRptqVvDO8I1De+3HlXWK42ohi1UWwXLej2cVk\r\niYlCMmQOzKfgTzLuwQnBPRJUiIVon1j/i3ZO4baVNdledS1RMqyVG4ilJlUVqud/\r\neD0zI1YUPE2YizxYI+8L3k7sze/nDGhtX021HMGSEpVq8NKaPapylK0X+tn7YY0Z\r\nuY22UoTwLUy+sX8lctzGT571iODCEEEfC+c=\r\n-----END CERTIFICATE REQUEST-----"
        }


        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        """
        Lista certificados
        """

        self.logger.info('listing all certificates...')
        rc, list = self.getCertificates(jwt)
        self.logger.debug('Certificate List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Associating certificate
        """
        """

        self.logger.info('associating certificate...')
        fingerprint = Api.get_fingerprint(jwt, 0)
        self.logger.info('Fingerprint: ' + fingerprint)
        device_id = Api.get_deviceid_by_label(jwt, "sensor")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint, device_id)
        self.logger.debug('Certificate associated: ' + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        """


        """
        Listing associated certificates (belongsTo preenchido)
        """
        self.logger.info('listing all certificates...')
        rc, list = self.getCertificates(jwt)
        self.logger.debug('Certificate List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Lista certificados
        """
        self.logger.info('listing all certificates...')
        rc, list = self.getCertificates(jwt)
        self.logger.debug('Certificate List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        #GET < base - url > / v1 / certificates?page = < number > & limit = < number > & fields = < list > & key1 = val1 & ... & keyn = valn

        self.logger.info('listing certificates with parameter: page...')
        rc, res = self.getCertificatesWithParameters(jwt, "page=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: page...')
        rc, res = self.getCertificatesWithParameters(jwt, "page=2")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: page...')
        rc, res = self.getCertificatesWithParameters(jwt, "page=5")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=3")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=30")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=250")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&page=1...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&page=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&page=2...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&page=2")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&page=3...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&page=3")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&page=4...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&page=4")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fields=fingerprint')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fingerprint=^05')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint&fingerprint=^05")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fields=pem')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=pem")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: pem=^MIIFWjCCA0KgA')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=pem&pem=^MIIFWjCCA0KgA")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fingerprint, pem')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,pem")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: createdAt')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=createdAt")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: createdAt')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=createdAt&createdAt=<=2021-05-25T00:00:00.000Z")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fingerprint,createdAt')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,createdAt")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: autoRegistered')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=autoRegistered")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: autoRegistered=false')
        rc, res = self.getCertificatesWithParameters(jwt, "autoRegistered=false")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: autoRegistered=true')
        rc, res = self.getCertificatesWithParameters(jwt, "autoRegistered=true")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fingerprint,autoRegistered')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,autoRegistered")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fingerprint, issuedByDojotPki')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,issuedByDojotPki")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fingerprint,belongsTo')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fingerprint,tenant')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,tenant")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with all parameters')
        rc, res = self.getCertificatesWithParameters(jwt, "page=1&limit=2&fields=fingerprint&fingerprint=~:44")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        """
        Lista certificate especifico
        """

        rc, fingerprint = Api.get_fingerprint(jwt, 0)
        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate...')
        rc, res = self.getCertificate(jwt, fingerprint)
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate with parameters: fields=fingerprint...')
        rc, res = self.getCertificateWithParameters(jwt, fingerprint, "fields=fingerprint")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate with parameters: fields=pem...')
        rc, res = self.getCertificateWithParameters(jwt, fingerprint, "fields=pem")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate with parameters: fields=tenant...')
        rc, res = self.getCertificateWithParameters(jwt, fingerprint, "fields=tenant")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate with parameters: fields=autoRegistered...')
        rc, res = self.getCertificateWithParameters(jwt, fingerprint, "fields=autoRegistered")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate with parameters...')
        rc, res = self.getCertificateWithParameters(jwt, fingerprint, "fields=issuedByDojotPki")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate with parameters: fields=issuedByDojotPki...')
        rc, res = self.getCertificateWithParameters(jwt, fingerprint, "fields=belongsTo")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Fingerprint: ' + fingerprint)
        self.logger.info('listing specific certificate with parameters: fields=createdAt...')
        rc, res = self.getCertificateWithParameters(jwt, fingerprint, "fields=createdAt")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        """
        Remove Certificate especifico 
        """
        """
        self.logger.info('removing specific Certificate...')
        fingerprint = Api.get_fingerprint(jwt, 0)
        self.logger.info('Fingerprint: ' + str(fingerprint))
        rc, res = self.deleteCertificate(jwt, fingerprint)
        self.logger.debug('Result: ' + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        """

        self.logger.info('Get root CA...')
        rc, res = self.getCA(jwt)
        self.logger.debug('CA certificate: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('Get latest CRL...empty list')
        rc, res = self.getCRL(jwt)
        self.logger.debug('CRL list: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Publicar dados usando um certificado
        """

        """
        Revogar o certificado
        """
        """
        Verificar se a CRL é atualizada
        """

        self.logger.info('Get latest CRL...')
        rc, res = self.getCRL(jwt)
        self.logger.debug('CRL list: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Publicar dados usando o certificado revogado
        """
        """
        Revogar outro certificado
        """
        """
        Verificar se a CRL é atualizada quando outros certificados são revogados
        """
        self.logger.info('Get latest CRL...')
        rc, res = self.getCRL(jwt)
        self.logger.debug('CRL list: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Publicar dados usando um certificado expirado
        """

        """
        Fluxos Alternativos
        """

        #erro 400: A message describing the cause of the error

        self.logger.debug('creating certificate - csr inválido ...') # ainda não tem validação, o certificado é criado
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGMTIzYWJjMIIBIjANBgkqhkiG9w0BAQEF\r\nAAOCAQ8AMIIBCgKCAQEAu6O1KQWOmlfSuXmeMoyPWQwjCRrnrX/Iq/lueCRCafN4\r\ni37BxoVyBTOmYIdrwsxWI6bZ/em2helsPcIs+w0JIV2YAqWYlJT0h1r0kZIrmG7l\r\nNXDxSZ1+iZrUhEItSVnAy0Pu5klBmV0cRtfoHvpmFEUNDRk1LwxrlgirLYUAGibf\r\nUz+OvLOgjlMm62/01dbskVxIrEyIeQItTlvfbnKwSMRfVzv7lMmewTrqVAU8ygJo\r\n6HG49QBo6EAUsSkgGsn+HiOMJc/WIa1SnSuFtAOI4X2xFyVvWnuALHuMHcQ+j1ZU\r\nhDXhkYqyt5g9FwJGRxzzs64LqE4QIqbaBSVCw1cOsQIDAQABoAAwDQYJKoZIhvcN\r\nAQELBQADggEBAH/j0kylaxvvqLGOAXdxS93sFMVN3J/37yf/ZcI8uWecuEO0sJh6\r\nArXQCJo7w0K4SX3IYV9x76NrTDoxC6cwLy1Jz8RzfHpPr2eWaqrV1IF31rGhs4iu\r\n5oeUQmtN9WdBepfrosbNXz15+eRmBDv8gaTT6U0WuY8GhJcBr9hMGU27YXhVbFDR\r\n9BJSKgt2rrKsmrg/d+uufKMPuTzErv/731wKD0mYXjuRaHkUi/34RylsJbzUpENc\r\n76m697la47TjmZAq/Cs4If57LHXCSdJe+ox619k3LHJUXJwfbC4yQTmr2OLagV7j\r\nv2G7zCntFPTw31EHwQ0YtUVEhxkOUlE7Bfc=\r\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.debug('creating certificate - csr vazio...')
        certificate = {
            "csr": ""
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("Result: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        self.logger.debug('creating certificate - csr adulterado...')
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGNWEzMmViMIIBIjANBgkqhkiG9w0BAQEF\r\nAAOCAQ8AMIIBCgKCAQEAzKQh4Y4E3t8byxNAsWMuztPjNcvsOCC8GwFeexmFSlpS\r\nugcLqx7j4h+7rjeZvPKfV5fBd73jUh2kj8AzoR5UilNUIgXl38ry+dEuSotSB8lS\r\nICUgWEvWkuJNCBjZBpzlfp1xRPyS96fr6sGPuISVCxIHheeyYVLApeEGtQWOymwm\r\nItAAOTJyPaddfv4fvmvurNHK8hOPauiu2eCDJiQQaFQsCnNbx9Q1QozNee5Ln6ZG\r\nwcCgy0k7g43YRnARNGnffKvJuSsbbUxW7ZHJKTLFPz8mb2cPFtHJqJovEojoaKR4\r\nsHjklsHi5kKzprf/OBztKr+4s9g19hvYOKxWg1ajdwIDAQABoAAwDQYJKoZIhvcN\r\nAQELBQADggEBACK04o5DRVPbvaFLQn4Grhir2drtqBVjtPNDDu8bs9fsXqlnTJKo\r\n8XN9yO53qDc6LDYT6qsRzXk9o2YsARkA+i/KSJSdEdgev5wYaG4nHS55xy/BNMLX\r\n+hSY52JiTGH582fwXbGARucogPsaqeq0bHhEATwvDqEEAeqogmNGTaRc6zGtPfu7\r\n5GyBgQfpBRv1daI8k883Q5sbLTXTqWip/HwgLxY21z+ife6fZe076xpdyIUw5E8B\r\nN9IGKczrFV6JoTpKSEhXhppxS6BmNC18+XeCMBuwK9LJs5Jkwy4DnPOgWjPvQzi8\r\nXUix95xsh0nQ/pOqoq/M5wM4JzuLaLABCW4=\r\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("Result: " + str(res))
        self.assertTrue(int(rc) == 500, "codigo inesperado") #erro esperado: 400

        self.logger.debug('creating certificate - no body...')
        certificate = {}
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("Result: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        resposta_esperada = "{\"schema$id\":\"http://www.dojot.com.br/schemas/reg-or-gen-cert\",\"schemaErrors\":[{\"keyword\":\"required\",\"dataPath\":\"\",\"schemaPath\":\"#/oneOf/0/required\",\"params\":{\"missingProperty\":\"certificatePem\"},\"message\":\"should have required property 'certificatePem'\"},{\"keyword\":\"required\",\"dataPath\":\"\",\"schemaPath\":\"#/oneOf/1/required\",\"params\":{\"missingProperty\":\"csr\"},\"message\":\"should have required property 'csr'\"},{\"keyword\":\"oneOf\",\"dataPath\":\"\",\"schemaPath\":\"#/oneOf\",\"params\":{\"passingSchemas\":null},\"message\":\"should match exactly one schema in oneOf\"}]}"
        self.logger.info("Resultado esperado: " + str(resposta_esperada))
        #self.assertTrue(res == resposta_esperada, "resposta inesperada")

        self.logger.info('listing Certificate - No such Certificate...')
        rc, res = self.getCertificate(jwt, "123")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        # GET <base-url>/v1/certificates?page=<number>&limit=<number>&fields=<list>&key1=val1&...&keyn=valn
        self.logger.info('listing Certificates with parameter: page=0...')
        rc, res = self.getCertificatesWithParameters(jwt, "page=0")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado") #erro esperado: 400; page default:1

        self.logger.info('listing Certificates with parameter: limit=0...')
        res = self.getCertificatesWithParameters(jwt, "limit=0")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado") #erro esperado: 400; limit default:25

        self.logger.info('listing Certificates with parameter: limit and page must be integers...')
        rc, res = self.getCertificatesWithParameters(jwt, "page=xyz&limit=kwv")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado") #erro esperado: 400; assume valores default

        self.logger.info('listing certificates with parameters (nonexistent parameter )')
        rc, res = self.getCertificatesWithParameters(jwt, "parametro=outro")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado") #erro esperado: 400; ignora valores inválidos

        self.logger.info('listing certificates with parameters (no data)')
        rc, res = self.getCertificatesWithParameters(jwt, "autoRegistered=true")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado") #erro esperado: 400; ignora valores inválidos

        self.logger.info('listing certificates with all parameters (no data)')
        rc, res = self.getCertificatesWithParameters(jwt, "page=1&limit=22&fields=fingerprint,createdAt&createdAt=<=2020-10-14T00:00:00.000Z&autoRegistered=false")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado") #erro esperado: 400; ignora valores inválidos

        self.logger.info('removing specific Certificate - No such Certificate...')
        rc, res = self.deleteCertificate(jwt, "1000")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        self.logger.info('removing all certificates')
        rc, res = self.deleteCertificates(jwt)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        """
        Certificados externos
        """

        """
        Registrar um certificado externo - Trusted CA não cadastrada

        Endpoint: v1/certificates
        status
        code: 400
        method: POST
        """

        """
        Registrar um certificado externo – com certificateChain - 1 nivel
       
       Endpoint: v1/certificates
       status code: 201
       method: POST
        """
        """
        Registrar um certificado externo – com certificateChain - 2 niveis

        Endpoint: v1 / certificates
        status
        code: 201
        method: POST
        """
        """
        Registrar um certificado externo – com certificateChain - incluindo CA externa
        
        Endpoint: v1/certificates
        status code: 201
        method: POST


        """
        """
        Registrar um certificado externo – sem CNAME
        
        Endpoint: v1/certificates
        status code: 201
        method: POST
        """
        """
        Registrar um certificado externo – com CNAME
        Endpoint: v1/certificates
        status code: 201
        method: POST
        """
        """
        Registrar um certificado externo – sem CNAME - usando fingerprint da CA
        Endpoint: v1/certificates
        status code: 201
        method: POST
        """
        """
        Registrar um certificado externo – sem CNAME - usando certificado CA
        Endpoint: v1/certificates
        status code: 201
        method: POST
        """
        """
        Registrar um certificado com dispositivo associado
        Endpoint: v1/certificates
        status code: 201
        method: POST
        """
        """
        Associar dois certificados a um dispositivo
        
        Endpoint: v1/certificates/{fingerprint}
        status code: 204
        method: PATCH
        """
        """
        Remover um dispositivo com certificado associado
        Endpoint: /device/{deviceid}
        status code: 200
        method: DELETE
        """
        """
        Remover certificado com dispositivo associado

        Endpoint: v1/certificates/{fingerprint}
        status
        code: 204
        method: DELETE
        """
        """
        Associar um certificado inválido a um dispositivo

        Endpoint: v1/certificates/{fingerprint}
        status
        code: 400
        method: PATCH
        """\
        """
        Associar um dispositivo inválido a um certificado

        Endpoint: v1/certificates/{fingerprint}
        status
        code: 400
        method: PATCH

        """
        """
        
        Associar certificado com dispositivo – certificado com CNAME

        Endpoint: v1/certificates
        status
        code: 201
        method: POST
        """
        """
        Associar certificado com dispositivo – certificado sem CNAME
        
        Endpoint: v1/certificates
        status
        code: 201
        method: POST
        """

        """
        Trusted CA Certificates
        """

        """
        Registro de uma CA externa
        """
        self.logger.debug('registering trusted CA ... USAR UM CERTIFICADO VÁLIDO')
        caPem = "-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,F57524B7B26F4694\nIJ/e6Xrf4pTBSO+CHdcqGocyAj5ysUre5BwTp6Yk2w9P/r7si7YA+pivghbUzYKc\nuy2hFwWG+LVajZXaG0dFXmbDHd9oYlW/SeJhPrxMvxaqC9R/x4MugAMFOhCQGMq3\nXW58R70L48BIuG6TCSOAGIwMDowv5ToL4nZYnqIRT77aACcsM0ozC+LCyqmLvvsU\nNV/YX4ZgMhzaT2eVK+mtOut6m1Wb7t6iUCS14dB/fTF+RaGYYZYMGut/alFaPqj0\n/KKlTNxCRD99+UZDbg3TnxIFSZd00zY75votTZnlLypoB9pUFP5iQglvuQ4pD3Ux\nbzU4cO0/hrdo04wORwWG/DUoAPlq8wjGei5jbEwHQJ8fNBzCl3Zy5Fx3bcAaaXEK\nzB97cyqhr80f2KnyiAKzk7vmyuRtMO/6Y4yE+1mLFE7NWcRkGXLEd3+wEt8DEq2R\nnQibvRTbT26HkO0bcfBAaeOYxHawdNcF2SZ1dUSZeo/teHNBI2JD5xRgtEPekXRs\nbBuCmxUevuh2+Q632oOpNNpFWBJTsyTcp9cAsxTEkbOCicxLN6c1+GvwyIqfSykR\nG08Y5M88n7Ey5GZ43KUbGh60vV5QN/mzhf3SotBl9+wetpm+4AmkKVUQyQVdRrn2\n1jXrkUZcSN8VbYk2tB74/FFXuaaF2WRQNawceXjrvegxz3/AkjZ7ahYI4rgptCqz\nOXvMk+le5tmVKbJfl1G+EZm2CqDLly5makeMKvX3fSWefKoZSbN0NuW28RgSJIQC\npqja3dWZyGl7Z9dlM+big0nbLhMdIvT8526lD+p+9aMMuBL14MhWGp4IIfvXOPR+\nOts3ZoGR9vtPQyO6YN5/CtRp1DBbRA48W9xk0BnnjSNpFBLY4ykqZj/cS01Up88x\nUMATqoMLiBwKCyaeibiIXpzqPTagG3PEEJkYPsrG/zql1EktjTtNo4LaYdFuZZzb\nfMmcEpFZLerCIgu2cOnhhKwCHYWbZ2MSVsgoiu6RyqqBblAfNkttthiPtCLY82sQ\n2ejN3NMsq+xlc/ISc21eClUaoUXmvyaSf2E3D4CN3FAi8fD74fP64EiKr+JjMNUC\nDWZ79UdwZcpl2VJ7JUAAyRzEt66U5PwQqv1U8ITjsBjykxRQ68/c/+HCOfg9NYn3\ncmpK5UxdFGj6261c6nVRlLVmV0+mPj1+sWHow5jZiH81IuoL3zqGkKzqy5FkTgs4\nMG3hViN9lHEmMPZdK16EPhCwvff0eBV+vhfPjmGoAE6TK3YY/yh9bfhMliLoc1jr\nNmPxL0FWrNzqWxZwMtDYcXu4KUesBL6/Hr+K9HSUa8zF+4UbELJTPOd1QAU6HF7a\n9BidzGMZ+J2Vjqa/NGpWckBRjWb6S7aItK6rrtORU1QHmpQlYpqEh49sreo6DCrb\ns8yejjKm2gSB/KhTe1nJXcTM16Xa4qWXTv11x46FNTZPUWQ7KoI0AzzScn6StBdo\nYCvzqCrla1em/Kakkws7Qu/pVj9R8ndHzoLktOi3l6lwwy5d4L697DyhP+02+eLt\nSBefoVnBNp449CSHW+brvPEyKD3D5CVpTIDfu2y8+nHszfBL22wuO4T+oem5h55A\n-----END RSA PRIVATE KEY-----",
        allowAutoRegistration = False

        rc, res = self.registerTrustedCA(jwt, caPem, allowAutoRegistration)
        self.logger.info("caFingerprint: " + str(res))
        #self.assertTrue(int(rc) == 201, "codigo inesperado")
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        

        """
        Cadastro certificado externo – CA externa com certificado expirado
        """

        self.logger.debug('registering trusted CA - expired certificate ... USAR UM CERTIFICADO EXPIRADO')
        caPem = "-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,F57524B7B26F4694\nIJ/e6Xrf4pTBSO+CHdcqGocyAj5ysUre5BwTp6Yk2w9P/r7si7YA+pivghbUzYKc\nuy2hFwWG+LVajZXaG0dFXmbDHd9oYlW/SeJhPrxMvxaqC9R/x4MugAMFOhCQGMq3\nXW58R70L48BIuG6TCSOAGIwMDowv5ToL4nZYnqIRT77aACcsM0ozC+LCyqmLvvsU\nNV/YX4ZgMhzaT2eVK+mtOut6m1Wb7t6iUCS14dB/fTF+RaGYYZYMGut/alFaPqj0\n/KKlTNxCRD99+UZDbg3TnxIFSZd00zY75votTZnlLypoB9pUFP5iQglvuQ4pD3Ux\nbzU4cO0/hrdo04wORwWG/DUoAPlq8wjGei5jbEwHQJ8fNBzCl3Zy5Fx3bcAaaXEK\nzB97cyqhr80f2KnyiAKzk7vmyuRtMO/6Y4yE+1mLFE7NWcRkGXLEd3+wEt8DEq2R\nnQibvRTbT26HkO0bcfBAaeOYxHawdNcF2SZ1dUSZeo/teHNBI2JD5xRgtEPekXRs\nbBuCmxUevuh2+Q632oOpNNpFWBJTsyTcp9cAsxTEkbOCicxLN6c1+GvwyIqfSykR\nG08Y5M88n7Ey5GZ43KUbGh60vV5QN/mzhf3SotBl9+wetpm+4AmkKVUQyQVdRrn2\n1jXrkUZcSN8VbYk2tB74/FFXuaaF2WRQNawceXjrvegxz3/AkjZ7ahYI4rgptCqz\nOXvMk+le5tmVKbJfl1G+EZm2CqDLly5makeMKvX3fSWefKoZSbN0NuW28RgSJIQC\npqja3dWZyGl7Z9dlM+big0nbLhMdIvT8526lD+p+9aMMuBL14MhWGp4IIfvXOPR+\nOts3ZoGR9vtPQyO6YN5/CtRp1DBbRA48W9xk0BnnjSNpFBLY4ykqZj/cS01Up88x\nUMATqoMLiBwKCyaeibiIXpzqPTagG3PEEJkYPsrG/zql1EktjTtNo4LaYdFuZZzb\nfMmcEpFZLerCIgu2cOnhhKwCHYWbZ2MSVsgoiu6RyqqBblAfNkttthiPtCLY82sQ\n2ejN3NMsq+xlc/ISc21eClUaoUXmvyaSf2E3D4CN3FAi8fD74fP64EiKr+JjMNUC\nDWZ79UdwZcpl2VJ7JUAAyRzEt66U5PwQqv1U8ITjsBjykxRQ68/c/+HCOfg9NYn3\ncmpK5UxdFGj6261c6nVRlLVmV0+mPj1+sWHow5jZiH81IuoL3zqGkKzqy5FkTgs4\nMG3hViN9lHEmMPZdK16EPhCwvff0eBV+vhfPjmGoAE6TK3YY/yh9bfhMliLoc1jr\nNmPxL0FWrNzqWxZwMtDYcXu4KUesBL6/Hr+K9HSUa8zF+4UbELJTPOd1QAU6HF7a\n9BidzGMZ+J2Vjqa/NGpWckBRjWb6S7aItK6rrtORU1QHmpQlYpqEh49sreo6DCrb\ns8yejjKm2gSB/KhTe1nJXcTM16Xa4qWXTv11x46FNTZPUWQ7KoI0AzzScn6StBdo\nYCvzqCrla1em/Kakkws7Qu/pVj9R8ndHzoLktOi3l6lwwy5d4L697DyhP+02+eLt\nSBefoVnBNp449CSHW+brvPEyKD3D5CVpTIDfu2y8+nHszfBL22wuO4T+oem5h55A\n-----END RSA PRIVATE KEY-----",
        allowAutoRegistration = False

        rc, res = self.registerTrustedCA(jwt, caPem, allowAutoRegistration)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Conexão MQTT, usando TLS, com sucesso – certificado com CNAME
        """
        """
        Conexão MQTT, usando TLS, com sucesso – certificado sem CNAME
        """
        """
        Conexão MQTT utilizando um certificado existente, porém não associado a um dispositivo
        """
        """
        Conexão MQTT utilizando um certificado externo – cadastro utilizando chain
        """
        """
        Conexão MQTT com certificado expirado
        """
        """
        Remoção de uma CA externa
        """



        #obter caFingerprint da CA
        caFingerprint = ""
        self.logger.debug('removing trusted CA ...')
        rc, res = self.deleteTrustedCA(jwt, caFingerprint)
        self.logger.info("message: " + str(res))
        #self.assertTrue(int(rc) == 204, "codigo inesperado")
        self.assertTrue(int(rc) == 404, "codigo inesperado")
        



        """
        Remover um dispositivo sem certificado associado
        
        Endpoint: /device/{deviceid}
        status code: 200
        method: DELETE
        
        """
        """
        Obter lista de CAs externas
        
        Endponit: v1/trusted-cas{?offset,limit,fields,keyVal}
        status code: 200
        method: GET
        """
        self.logger.debug('listing trusted CAs ... TODO')
        #rc, res = self.getTrustedCAs(jwt)
        self.logger.info("trusted-cas: " + str(res))
        #self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Obter lista de CAs externas - parâmetros válidos
        
        Endpoint: v1/trusted-cas{?offset,limit,fields,keyVal}
        status code: 200
        method: GET
        """
        self.logger.debug('listing trusted CAs with parameters...TODO')
        #rc, res = self.getTrustedCAs(jwt)
        self.logger.info("trusted-cas: " + str(res))
        #self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Listing associated certificates
        """
        self.logger.info('listing all certificates...')
        rc, list = self.getTrustedCAs(jwt)
        self.logger.debug('Certificate List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Lista certificados externos
        """
        self.logger.info('listing all certificates...')
        rc, list = self.getTrustedCAs(jwt)
        self.logger.debug('Certificate List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        #GET < base - url > /v1/certificates?offset = < number > & limit = < number > & fields = < list > & key1 = val1 & ... & keyn = valn

        self.logger.info('listing certificates with parameter: offset=1...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: offset=2...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=2")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: offset=5...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=5")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=1...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=3...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=3")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=30...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=30")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=250...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=250")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=251...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=251")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=1...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=2...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=2")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=3...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=3")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=4...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=4")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fields=caFingerprint')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: caFingerprint=^05')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint&caFingerprint=^05")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fields=caPem')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caPem")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: caPem=^MIIFWjCCA0KgA')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caPem&caPem=^MIIFWjCCA0KgA")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: caFingerprint, caPem')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint,caPem")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: createdAt')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=createdAt")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: createdAt')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=createdAt&createdAt=<=2021-05-25T00:00:00.000Z")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: caFingerprint,createdAt')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint,createdAt")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: allowAutoRegistration')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=allowAutoRegistration")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: allowAutoRegistration=false')
        rc, res = self.getTrustedCAsWithParameters(jwt, "allowAutoRegistration=false")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: allowAutoRegistration=true')
        rc, res = self.getTrustedCAsWithParameters(jwt, "allowAutoRegistration=true")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: caFingerprint,allowAutoRegistration')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint,allowAutoRegistration")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        self.logger.info('listing certificates with all parameters')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=1&limit=2&fields=caFingerprint&caFingerprint=~:44")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        """
        Lista certificate externo específico
        """

        caFingerprint = Api.get_caFingerprint(jwt, 0)
        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific certificate...')
        rc, res = self.getTrustedCA(jwt, caFingerprint)
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific certificate with parameters: fields=caFingerprint...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=caFingerprint")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific certificate with parameters: fields=caPem...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=caPem")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific certificate with parameters: fields=allowAutoRegistration...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=allowAutoRegistration")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific certificate with parameters: fields=createdAt...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=createdAt")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        """
        Obter CA externa
        
        Endpoint: v1/trusted-cas/{caFingerprint}{?fields}
        status code: 200
        method: GET
        """
        """
        Obter CA externa - com filtros
        
        Endpoint: v1/trusted-cas/{caFingerprint}{?fields}
status code: 200
method: GET
        """
        """
        Obter lista de CA externa - invalid request
        
        Endpoint: v1/trusted-cas{?page,limit,fields,keyVal}
status code: 400
method: GET
        """
        """
        Obter lista de CA externa - JWT vazio
        Endpoint: v1/trusted-cas{?page,limit,fields,keyVal}
status code: 401
method: GET
        """
        """
        Obter lista de CA externa - JWT inválido
        Endpoint: v1/trusted-cas{?page,limit,fields,keyVal}
status code: 401
method: GET
        """
        """
        Obter lista de CA externa - operação não autorizada
        Endpoint: v1/trusted-cas{?page,limit,fields,keyVal}
status code: 403
method: GET
        """
        """
        Obter CA externa - CA não existe
        Endpoint: v1/trusted-cas/{caFingerprint}{?fields}
status code: 404
method: GET
        """
        """
        Cadastro certificado externo – CA externa com certificado vazio
        Endpoint: v1/trusted-cas
status code: 400
method: POST
        """
        """
        Cadastro certificado externo – CA externa, certificado já existe
        Endpoint: v1/trusted-cas
status code: 400
method: POST
        """
        """
        Cadastro certificado externo – CA externa, certificado não é uma CA
        
        Endpoint: v1/trusted-cas
status code: 400
method: POST
        """
        """
        Cadastro certificado externo – CA externa, certificado não é uma CA root
        Endpoint: v1/trusted-cas
status code: 400
method: POST
        """
        """
        Cadastro certificado externo – CA externa, excedeu o nº de CAs registradas
        Endpoint: v1/trusted-cas
status code: 400
method: POST
        """
        """
        Cadastro certificado externo – invalid request
        Endpoint: v1/trusted-cas
status code: 400
method: POST
        """
        """
        Cadastro certificado externo – campo allowAutoRegistration vazio
        Endpoint: v1/trusted-cas
status code: 400
method: POST
        """
        """
        Cadastro certificado externo – JWT vazio
        Endpoint: v1/trusted-cas
status code: 401
method: POST
        """
        """
        Cadastro certificado externo – JWT invalido
        Endpoint: v1/trusted-cas
status code: 401
method: POST
        """
        """
        Cadastro certificado externo – operação não autorizada
        Endpoint: v1/trusted-cas
status code: 403
method: POST
        """
        """
        Remoção de uma CA externa - existe certificado assinado pela CA
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 400
method: DELETE
        """
        """
        Remoção de uma CA externa - invalid request
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 400
method: DELETE

        """
        """
        Remoção de uma CA externa - JWT vazio
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 401
method: DELETE
        """
        """
        Remoção de uma CA externa - JWT inválido
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 401
method: DELETE
        """
        """
        Remoção de uma CA externa - operação não autorizada
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 403
method: DELETE
        """
        """
        Remoção de uma CA externa - CA não existe
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 404
method: DELETE
        """
        """
        Atualizar CA externa - alterar o parâmetro allowAutoRegistration
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 204
method: PATCH
        """
        """
        Atualizar CA externa - parâmetro allowAutoRegistration vazio
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 400
method: PATCH
        """
        """
        Atualizar CA externa - invalid request
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 400
method: PATCH
        """
        """
        Atualizar CA externa - JWT vazio
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 401
method: PATCH
        """
        """
        Atualizar CA externa - JWT inválido
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 401
method: PATCH
        """
        """
        Atualizar CA externa - operação não autorizada
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 403
method: PATCH
        """
        """
        Atualizar CA externa - CA não existe
        Endpoint: v1/trusted-cas/{caFingerprint}
status code: 404
method: PATCH
        """



