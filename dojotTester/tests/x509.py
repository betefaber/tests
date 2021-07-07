from common.base_test import BaseTest
from dojot.api import DojotAPI as Api
from mqtt.mqttClient import MQTTClient
import json


class X509Test(BaseTest):

    """
    Pré-condições:
        - gerar CSR para o dispositivo, no formato PEM
        - gerar certificados público e privado para o dispositivo
        - existir certificados de CAs confiáveis
    """

    def getCA(self, jwt: str):
        rc, res = Api.get_ca(jwt)
        return rc, res

    def getCRL(self, jwt: str):
        rc, res = Api.get_crl(jwt)
        return rc, res

    def getSchemas(self, jwt: str):
        rc, res = Api.get_schemas(jwt)
        return rc, res

    def importData(self, jwt: str):
        data = {
            "devices": [{"attrs": [], "id": "12f286", "label": "sensor", "templates": [2]},
                        {"attrs": [], "id": "33323f", "label": "dispositivo", "templates": [1]},
                        {"attrs": [], "id": "41d208", "label": "device2", "templates": [2]},
                        {"attrs": [], "id": "545da1", "label": "device5", "templates": [2]},
                        {"attrs": [], "id": "5a15cc", "label": "sensor2", "templates": [2]},
                        {"attrs": [{"created": "2021-07-05T18:21:38.149667+00:00", "id": 7, "is_static_overridden": True, "label": "serial", "static_value": "SN5242", "template_id": "1", "type": "static", "value_type": "string"},
                                   {"created": "2021-07-05T18:21:38.149675+00:00", "id": 4, "label": "gps", "metadata": [{"created": "2021-07-05T18:21:38.152451+00:00", "id": 9, "is_static_overridden": True, "label": "descricao", "static_value": "posicao inicial", "type": "static", "updated": None, "value_type": "string"}], "template_id": "1", "type": "dynamic", "value_type": "geo:point"}], "id": "6206c6", "label": "dispositivo2", "templates": [1]},
                        {"attrs": [], "id": "85bd7f", "label": "sensor4", "templates": [2]},
                        {"attrs": [], "id": "9c7e06", "label": "device4", "templates": [2]},
                        {"attrs": [], "id": "ae8533", "label": "device3", "templates": [2]},
                        {"attrs": [], "id": "ca2133", "label": "sensor3", "templates": [2]},
                        {"attrs": [], "id": "ced750", "label": "dispositivo3", "templates": [1]},
                        {"attrs": [], "id": "f67d46", "label": "device", "templates": [2]}],
            "templates": [{"attrs": [{"id": 8, "label": "objeto", "template_id": "1", "type": "dynamic", "value_type": "object"},
                                     {"id": 7, "label": "serial", "static_value": "indefinido", "template_id": "1", "type": "static", "value_type": "string"},
                                     {"id": 6, "label": "mensagem", "template_id": "1", "type": "actuator", "value_type": "string"},
                                     {"id": 5, "label": "bool", "template_id": "1", "type": "dynamic", "value_type": "bool"},
                                     { "id": 4, "label": "gps", "metadata": [{ "created": "2021-07-05T18:21:38.152451+00:00", "id": 9, "label": "descricao", "static_value": "localizacao do device", "type": "static", "updated": None, "value_type": "string"}], "template_id": "1", "type": "dynamic", "value_type": "geo:point"},
                                     { "id": 3, "label": "text", "template_id": "1", "type": "dynamic", "value_type": "string"},
                                     { "id": 2, "label": "int", "template_id": "1", "type": "dynamic", "value_type": "integer"},
                                     { "id": 1, "label": "float", "template_id": "1", "type": "dynamic", "value_type": "float"}],
                           "id": 1,
                           "label": "Template"},
                          {"attrs": [{"id": 11, "label": "model-id", "static_value": "model-001", "template_id": "2", "type": "static", "value_type": "string"},
                                     {"id": 10, "label": "temperature", "template_id": "2", "type": "dynamic", "value_type": "float"}],
                           "id": 2,
                           "label": "SensorModel"},
                          {"attrs": [{"id": 12, "label": "temperature", "template_id": "3", "type": "dynamic", "value_type": "float"}],
                           "id": 3,
                           "label": "Temperature"}],
            "flowRemoteNodes": [],
            "flows": [],
            "cronJobs": []}

        rc, res = Api.import_data(jwt, json.dumps(data))
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

    def getAssociatedCertificates(self, jwt: str):
        rc, res = Api.get_associated_certificates(jwt)
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

    def getTrustedCA(self, jwt: str, caFingerprint: str):
        rc, res = Api.get_trusted_ca(jwt, caFingerprint)
        return rc, res

    def getTrustedCAsWithParameters(self, jwt: str, attrs: str):
        rc, res = Api.get_trusted_cas_with_parameters(jwt, attrs)
        return rc, res

    def getTrustedCAWithParameters(self, jwt: str, fingerprint: str, attrs: str):
        rc, res = Api.get_trusted_ca_with_parameters(jwt, fingerprint, attrs)
        return rc, res

    def registerExternalCertificate(self, jwt: str, caFingerprint: str, certificateChain: str, device_id: str):
        rc, res = Api.register_external_certificate(jwt, caFingerprint, certificateChain, device_id)
        return rc,res

    def getExternalCertificates(self, jwt: str, caFingerprint: str):
        rc, res = Api.get_external_certificates(jwt, caFingerprint)
        return rc, res

    def runTest(self):
        self.logger.info('Executing x509 test')
        self.logger.debug('getting jwt...')
        jwt = Api.get_jwt()

        rc, res = self.importData(jwt)
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.debug('listing certificates - no data...')
        rc, res = self.getCertificates(jwt)
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.debug('creating certificate from CSR: sensor, device_id 12f286...')
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGMTJmMjg2MIIBIjANBgkqhkiG9w0BAQEF\nAAOCAQ8AMIIBCgKCAQEA0IveTiBQUCaUjrUhFqJVE8cKZctF2SlGFhLOg56pMkBD\nQaL6w+LENt3kHg7fOjaw/ziR6GAWotxCv0CL4PvB+WZG6tzn360P0CIY4G9Ptlt5\noGsmHS5/1vRi818FPMZK+K5mf74Fy84QGBP903NxdeMUJoaLOFxp8mklQtFhxp08\nSEF/Bt9vCVw7NOfy2Cf+3Ol83Iqw7+bfZippaq1yssxusu+0q5iVYtdibBNU3ejP\n+brYR50kTvPLT8KvdupEriYXOR2MbaNZoEbL6CmolyMOIeNC4XQL8S/N9DAGVLPa\nqA3X67EqzhPYPoXqgxOCps/QGxKe78Nxn4CeejvUbQIDAQABoAAwDQYJKoZIhvcN\nAQELBQADggEBAECVuCuDJbwHJDJc7T3rUD1k4sEVTS6QDx99nbXFWmRK/fsC2nph\nsC9iPd2Y4gW/eIRdEBplrwS1/Q4erkAB6EtvLV2pT2H8pUEbTbRhcXBalgJyKeGQ\ndyXvsFeJk32WWWc6QvUcytzUDYzAz7kjEoBTfLjbQM4strXDg3tWMJPb5q1R1dA2\nsBUS7b5QaTPNS2NjUSv1Mu1ixxryNpR1Ajy7NNUNFkIEtURaxlAtrr83Jd5uDluu\nRnNVoxlZfRu7gBVW3ipUit2gv4Z4y5deB8Q8tN07qJ2MZd/KoUd9VdEgLdd2No6o\nrOkqXYzMukIgkRSd7OoyWgQ/sBIITBox6f4=\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_sensor = res['certificateFingerprint']
        self.logger.info("fingerprint_sensor: " + str(fingerprint_sensor))

        self.logger.info('listing all certificates...')
        rc, list = self.getCertificates(jwt)
        self.logger.debug('Certificate List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.debug('creating certificate from CSR: sensor2, device_id 5a15cc...')
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGNWExNWNjMIIBIjANBgkqhkiG9w0BAQEF\nAAOCAQ8AMIIBCgKCAQEA6CnyI3JRBhfkWUoYwUS20xFelzI697oNJAshrKYM1LRf\nEjfAbbiNDfu+u5mSitw4Z9tdD0bAvd7EPKZrNLy1+BGfLw/R1ev7zLx6K8XBI4rN\n5FgaRBSkNiV/LiTCs7djDxUG3TaCKC+GoQTOndzm/7lsjpyJIP+Q7YOP7B048K3V\nDQmezcC5xUyX5zIAgSwIO1NjOqzdqumWae0739nSexMlVcGjiLayyAbR2Gc2N2Wa\nUJVt52h2RKtMa9/qgkGOy854tnXEk13Ma/P7PT2OC4o39TtpSyEFkFoVmcunr1rM\n6fd0p06vLbO1ZUHtHA7NgzK64d3+mt9uZnIfIUN/ywIDAQABoAAwDQYJKoZIhvcN\nAQELBQADggEBAMkj8rQ23UbqydPPDRIXQqiOhArYS9acDnK5pHTxnV/CRsuFt5ZH\n3EQ0CukWhfctIulFDT8564TObN1gEjj6iqfO7jnUcNLbxdlN6J/j92TbOCDVPz9U\njnOGvtIi9/OXBVi1YglFkzoWHd0wyeVmunO6OqDPqXLynlQTcdNMrbDeEzW4BCn7\n7s9mXU35DVYNgXyz76FQpuU9PWwXPfI3grb9D3jVX57xO/jEoJzo1WUeHJex8FH1\n/ne+l1+NIStHBx7QKad8HtfGNa1cKy6aKIeDLB/Q0VBhd3Y2G+1DA0Utg3a1WJlF\ny6hlp2Md0B93rAsEoKvbsbkO8497GxbZPIs=\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_sensor2 = res['certificateFingerprint']
        self.logger.info("fingerprint_sensor2: " + str(fingerprint_sensor2))

        self.logger.debug('creating certificate from CSR: sensor3, device_id ca2133...')
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGY2EyMTMzMIIBIjANBgkqhkiG9w0BAQEF\nAAOCAQ8AMIIBCgKCAQEAm54J3fcIlGTtTEScbJIfbRl6Bm5436e1+z1fA5JqT6KV\nCnfYDKA8ugZVTFqxKdLH2+znkHCbhbCOi6L6EE1hli4ILSO0qX4fh4wW/kadc/M0\nTbEuesP+MuAjO+kZCAFlZBRC/GEkahswPwQ81sqGqvmDNXg4GEa5e4Hf4Od0UfSd\nrmmLs2VUb6fKEs0NV2v8VNwqEBv68WvsWO9MiRFQmpCE2QDJJEAv8rQO1QT1+iC+\nGB+zYAqSkKlzqwlo8Qv4gnvEMPVb311qce80W3+nOoPmVnUk25qiiDbeBrhub/xh\npdNcAHrFX3oyirvmyTeOhgnxorIfCu7Lep5tmkBEWwIDAQABoAAwDQYJKoZIhvcN\nAQELBQADggEBAE0DyMNoyzovaF4qaIM5B+jDC6pV0NqUM/90zDP0I4UE46ewjGFb\n9PgdrmbNmjBP5Qbal8hf6gGypOPZFdVIK/hYcHegNkXvRPYtBY7NSwbyLG2VdeVu\nA8Oa2NcAU3jov8VzMlgkdWAxhDwu2eo5Q4GBAF705K8qY8x0FlEq/g7VQaEZBr52\n820H6Kl8sCpPE+V21rgcqdClm1SzcAhVj3Pk4P31mHC4nyvqsl32kjSexq9svVQy\np40L+QMeBDhmMls8Cvdm8Je4+jB+4P0RHj0oFrsL43LOybKlZRvIFnOxPSTMatH1\nzRQvtv4boG+0vH66KFKbu611ICxAhHn7lVM=\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_sensor3 = res['certificateFingerprint']
        self.logger.info("fingerprint_sensor3: " + str(fingerprint_sensor3))

        self.logger.debug('creating certificate from CSR: sensor4, device_id 85bd7f ...')
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICVjCCAT4CAQAwETEPMA0GA1UEAwwGODViZDdmMIIBIjANBgkqhkiG9w0BAQEF\nAAOCAQ8AMIIBCgKCAQEAurW+A+JCe+/ioJ5EPSl0S9oHCtGNUsYPGdzKeuttPsBr\nlzCNa0H/A4rfxUt1OWqhU+uJ2Kykoxzq61sqbnQ7KE7gOapzYsfApEMYMNKIpbzY\n6gnMJf1Q/LCjiQfcwtO79gPsN3OgvjUIfATBdoZnafQGeqoXD5IFdJCt+1ANb9AA\na2zky+13cbmWyD8KYmFSWp6liS2/mVB3aCTDGRhfNFmIm6rMEifarYZow21Ovvog\nL8oo8/kqLOa2GUPRL19OyvfMW1f7GW8CmmccfkwN68rfzoimnGVY7rz/HI0YFZD8\nkaCsy8UwTVEcUz5rpBzkhLyFF9GZoBT2Z0ifdUnMfQIDAQABoAAwDQYJKoZIhvcN\nAQELBQADggEBAIaip1MrVvtVN/CUxvdCqXH8hVF5QC2w2VFC0OumM0OPOjVb3FP6\n/CteRbOAo4GW5+NRo/HSDPyemd2Vyju25SC5VOfba9/qjI4VBZXbXoeqJHAQJci2\nVPHcyL9zX1TmYHGvzB0K4l9UAti+QNhs/dC9PgnFCIk/SK/Z+94v2QEX2qVHDu7w\nUfU3oiTrl91GnyxjvTDlesJ/AutxVNASP5bSD3L/OIgSfZXtzvoo7DKOYNEggCbe\n91t4SI6IuwXWqQS/o0Inv87ZUITWjW7gurVlxbOPnuC8mcYCN7QYe1oZxebFRN/0\nmfDgS63/YRoQ/V9YGJXVPJsVbhdNKFXwdX8=\n-----END CERTIFICATE REQUEST-----"
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("certificate: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_sensor4 = res['certificateFingerprint']
        self.logger.info("fingerprint_sensor4: " + str(fingerprint_sensor4))


        """
        Lista certificados
        """

        self.logger.info('listing all certificates...')
        rc, list = self.getCertificates(jwt)
        self.logger.debug('Certificate List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        #GET < base - url > /v1/certificates?page = < number > & limit = < number > & fields = < list > & key1 = val1 & ... & keyn = valn

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
        Lista certificado específico
        """

        fingerprint = fingerprint_sensor
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
        Get schemas, CA e CRL
        """

        """
        self.logger.info('Get schemas...')
        rc, res = self.getSchemas(jwt)
        self.logger.debug('Schemas: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
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

        dev_id = Api.get_deviceid_by_label(jwt, "sensor2")
        dev_topic = "admin:" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id)
        dev.publish(dev_topic, {"temperature": 30})


        """
        Revogar o certificado
        """

        self.logger.info('removing specific Certificate...')
        self.logger.info('Fingerprint: ' + str(fingerprint_sensor3))
        rc, res = self.deleteCertificate(jwt, fingerprint_sensor3)
        self.assertTrue(int(rc) == 204, "codigo inesperado")


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
        self.logger.info('removing specific Certificate...')
        self.logger.info('Fingerprint: ' + str(fingerprint_sensor2))
        rc, res = self.deleteCertificate(jwt, fingerprint_sensor2)
        self.logger.info('result: ' + str(rc) + ' , ' + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")

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
        Fluxos Alternativos - Certificados
        """

        #erro 400: A message describing the cause of the error

        self.logger.debug('creating certificate - csr inválido ...') # ainda não tem validação, o certificado é criado
        certificate = {
            "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIICVTCCAT0CAQAwEDEOMAwGA1UEAwwFMTIzNDUwggEiMA0GCSqGSIb3DQEBAQUA\nA4IBDwAwggEKAoIBAQDW8w7hGihNHojCncVz11pPxlo607uAhvUgMBue20cmuV7c\npDfbYeaL3xO9BEZPL+/fn6CI04UhAcVsAe26PZPYAfHyncnNDXrOE4O5a0MBYciU\nZj4TLj3Ya7JjCEqpCbim9HNfQCCJuWw/pMMUbrgDLVzl2fui36cfHEvG2d9pjylg\nS/x9jNeI47J0uEnrV2BIhFMNZdBqeaOEH8lRrOx9+O7cgHhlxqUQMS39wZKGiFpy\n9/Fn0cPvCzCUklWhvPvWMjMoiOCQBNuDCCK8uFb3184aV2PzNadKZ4iSkIJZoYT6\ndDtcu1iOkbEJOP3N/Pgv5jPnKV97hSsx4kQM4S/LAgMBAAGgADANBgkqhkiG9w0B\nAQsFAAOCAQEAoSDMluGBjbONBD9vLGeVexlBkSWKNxBzc+5127jeCPHSQUndHf09\nKmDhaGWlnDzfLY5ZPrfybnecpp5BmMfOHEwmx3aULIYPlwQjjET3O30lhuZzwL+L\nUCT9QmzPxS29OkSy4fk6BGe0zlJAbPlVz1bVZuJlmXO9kSfC7pn/omGDO69wxRMA\nO0v3CrBr1ZrpJoBtSCY2Tqf3qR+mPPdzb+NHfXRv6ogzxRQjB2BJQGNnR+9asdA4\n9yKz/nhqKo2CezZedWo0y3icWbFlhmK8N3gyxx3/NWBrO7AEsBnWCwhUoDiumbpB\nqF6dHXuiQhQWqBo71Nar/4+VAhsjL4PeSw==\n-----END CERTIFICATE REQUEST----"
        }
        rc, res = self.createCertificate(jwt, certificate)
        self.logger.info("certificate: " + str(rc) + ", " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

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
        rc, res = self.deleteCertificate(jwt, "40:50:35:1C:97:2A:00:BE:8E:75:AC:89:59:12:48:9C:FE:53:92:2F:4D:EA:1E:9E:C2:52:E5:A7:B2:B5:83:F7")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")


        """
        Trusted CA Certificates
        """

        """
        Registro de CA externa
        """

        self.logger.debug('registering trusted CA ... ') #CN=DST Root CA X3, O=Digital Signature Trust Co.
        caPem = "-----BEGIN CERTIFICATE-----\nMIIDSjCCAjKgAwIBAgIQRK+wgNajJ7qJMDmGLvhAazANBgkqhkiG9w0BAQUFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTAwMDkzMDIxMTIxOVoXDTIxMDkzMDE0MDExNVow\nPzEkMCIGA1UEChMbRGlnaXRhbCBTaWduYXR1cmUgVHJ1c3QgQ28uMRcwFQYDVQQD\nEw5EU1QgUm9vdCBDQSBYMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN+v6ZdQCINXtMxiZfaQguzH0yxrMMpb7NnDfcdAwRgUi+DoM3ZJKuM/IUmTrE4O\nrz5Iy2Xu/NMhD2XSKtkyj4zl93ewEnu1lcCJo6m67XMuegwGMoOifooUMM0RoOEq\nOLl5CjH9UL2AZd+3UWODyOKIYepLYYHsUmu5ouJLGiifSKOeDNoJjj4XLh7dIN9b\nxiqKqy69cK3FCxolkHRyxXtqqzTWMIn/5WgTe1QLyNau7Fqckh49ZLOMxt+/yUFw\n7BZy1SbsOFU5Q9D8/RhcQPGX69Wam40dutolucbY38EVAjqr2m7xPi71XAicPNaD\naeQQmxkqtilX4+U9m5/wAl0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNV\nHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFMSnsaR7LHH62+FLkHX/xBVghYkQMA0GCSqG\nSIb3DQEBBQUAA4IBAQCjGiybFwBcqR7uKGY3Or+Dxz9LwwmglSBd49lZRNI+DT69\nikugdB/OEIKcdBodfpga3csTS7MgROSR6cz8faXbauX+5v3gTt23ADq1cEmv8uXr\nAvHRAosZy5Q6XkjEGB5YGV8eAlrwDPGxrancWYaLbumR9YbK+rlmM6pZW87ipxZz\nR8srzJmwN0jP41ZL9c8PDHIyh8bwRLtTcm1D9SZImlJnt1ir/md2cXjbDaJWFBM5\nJDGFoqgCWjBH4d1QB7wCCZAA62RjYJsWvIjJEubSfZGL+T0yjWW06XyxV3bqxbYo\nOb8VZRzI9neWagqNdwvYkQsEjgfbKbYK7p2CNTUQ\n-----END CERTIFICATE-----"
        rc, caFingerprint = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("caFingerprintDSTRoot: " + str(caFingerprint))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.debug('registering trusted CA ... ') #CN=Root CA Teste
        caPem = "-----BEGIN CERTIFICATE-----\nMIICDTCCAW6gAwIBAgIUZAYqWqoeYfWqF5oXaGU0IeWfxuEwCgYIKoZIzj0EAwIw\nGDEWMBQGA1UEAwwNUm9vdCBDQSBUZXN0ZTAeFw0yMTA2MTcxMzA2MzBaFw0yNjA2\nMTYxMzA2MzBaMBgxFjAUBgNVBAMMDVJvb3QgQ0EgVGVzdGUwgZswEAYHKoZIzj0C\nAQYFK4EEACMDgYYABACJ5AcvLttv/pB5EjitNcKMCgyF+IYyDoPYLilanvpd26qi\nVSWlU2fnUikgzHuWUPAoVI0SI+MlluMxsycTzFcCQgHFgWQO5OV4QvYQZfcMNn+q\n3Sy7gCn2WkSqQIxBSLh3YvMyBGnL0wUFzLwb1sKk9pKAE6+J62WK2tswAkVdxdV6\nwqNTMFEwHQYDVR0OBBYEFLHxc59Y0GqKz0I1QRRsfTi4BwUKMB8GA1UdIwQYMBaA\nFLHxc59Y0GqKz0I1QRRsfTi4BwUKMA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0E\nAwIDgYwAMIGIAkIA71h70oucxkSQPhnqIVTInMFQf1a+Acp0l7UQpgeVezj4gGso\noLRVX5kWE+W0mALmF/vYCj+l2OctLe3PS95LBroCQgCoqCexRvdGEyToOnLyKdzn\n+eBrJbanwL9mtY9v0Rvt2XKEFynVQiQQ2/qdB7EnkJDeE/JwRArlCYHNZCFOk0gD\nHA==\n-----END CERTIFICATE-----"
        rc, caFingerprint = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("caFingerprintRootTeste: " + str(caFingerprint))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.debug('registering trusted CA ... ') #CN=Root CA Teste2
        caPem = "-----BEGIN CERTIFICATE-----\nMIICDjCCAXCgAwIBAgIUV5S5IYicPqJWWU3GVhSVZfH+UbIwCgYIKoZIzj0EAwIw\nGTEXMBUGA1UEAwwOUm9vdCBDQSBUZXN0ZTIwHhcNMjEwNjI1MTIzMTUwWhcNMjYw\nNjI0MTIzMTUwWjAZMRcwFQYDVQQDDA5Sb290IENBIFRlc3RlMjCBmzAQBgcqhkjO\nPQIBBgUrgQQAIwOBhgAEAU5GkPFlFyAv6xsxCrkQlmiFrrMSIrxjrBMjF56/kUk2\n/jqtSO4y8kCgLwpisQzybazSTunWqlPN2MN75bX4nQznAEQ8ED7ad1NB33T1RBHf\nBnX7naQunEU1nKeqXHkL0Ey2484LvU4Tl5kMrXmg+80Yhu0w/arKE3Kb63hm3Jxj\nQX4Co1MwUTAdBgNVHQ4EFgQUVeCFjcbjH8ZezmzzG86E592/yp8wHwYDVR0jBBgw\nFoAUVeCFjcbjH8ZezmzzG86E592/yp8wDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjO\nPQQDAgOBiwAwgYcCQgHRg0ofa+wxJUJGVjkUDV7Cl+Ka/yY7hrvaFlpusoKUg763\nCiNKDT+Qu1FAgXQINCpLdVy8/HxpRTHbk7f3tov++gJBDOlfCASJCWE25If7H2xX\nF+7Hpgalz9TAcpJdpiE7KJnZ78v9N5OBMC2oTnleeOzTYyBujs8snI2n3RQWCG6y\na70=\n-----END CERTIFICATE-----"
        rc, caFingerprint = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("caFingerprintRootTeste2: " + str(caFingerprint))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        """
        Obter lista de CAs externas
        """

        self.logger.debug('List Trusted CA Certificates ... ')
        rc, res = self.getTrustedCAs(jwt)
        self.logger.info("trusted-cas: " + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        CERTIFICADOS EXTERNOS
        """
        """
        Registrar um certificado externo – com certificateChain - 1 nivel
        """
        # caFingerprint da CA Root Teste
        caFingerprint = "4F:64:DE:09:24:AB:EC:C3:F0:96:41:E2:94:98:45:97:19:B0:26:EF:02:16:7A:44:DA:0F:C6:05:BE:BC:86:EA"
        self.logger.info("caFingerprint - CA Root Teste: " + str(caFingerprint))
        #certificateChain = certificado assinado pela Root CA Teste, CN=device4
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICTTCCAa+gAwIBAgIUDXs2wKRo1VeC9H97IE5w293a9oEwCgYIKoZIzj0EAwIw\nGDEWMBQGA1UEAwwNUm9vdCBDQSBUZXN0ZTAeFw0yMTA2MTcxMzIxNTVaFw0yMjA2\nMTcxMzIxNTVaMBIxEDAOBgNVBAMMB2RldmljZTQwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABACNnSro/BOc+CMgceFjxOFiW2qMghNHXzCBMt4i0lLmV/LwYcGKZGI0\nKtsslM2vrgp00XfKtdwICpiL+nPi0BYi3wANNMuWrAzAg24yFK7+SDxO34sOVMLS\nc36O0/sT5HL0XLLC86n4LPH2p0/G24KBEkfzSG9OQwg2rDws2wgrxiEXzaOBmTCB\nljAdBgNVHQ4EFgQUUgSd0v2IzF3Er2WmKP3LHf9qE94wHwYDVR0jBBgwFoAUsfFz\nn1jQaorPQjVBFGx9OLgHBQowDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCA+gwHQYD\nVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBoGA1UdEQQTMBGCCWxvY2FsaG9z\ndIcEfwAAATAKBggqhkjOPQQDAgOBiwAwgYcCQgEGEn3wz/AUMoGlrtuvJnrtD6AH\nkQw2RQv+/V7LvK/MbrEr4GQLfW7MuutFZMqnX/3PKhdMunm6iSEiwzGjIXPXmgJB\nT/J+n/hmv6pGhqXBwuwKwgvsSQKgvaxRFriWpWk+aigV3W+C29vyOqElQW2sZIOh\n/v9shdIN5dxmvFgxJ756Viw=\n-----END CERTIFICATE-----"

        self.logger.debug('registering certificate ... com certificateChain - 1 nivel (device4)')
        rc, res = self.registerExternalCertificate(jwt, str(caFingerprint), certificateChain, None)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_device4 = res['certificateFingerprint']
        self.logger.info("certificateFingerprint: " + str(fingerprint_device4))

        #certificateChain = certificado assinado pela Root CA Teste, CN=device5
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICTjCCAa+gAwIBAgIUfG4ExAIaikRnrlN2N5XUHGPqOOkwCgYIKoZIzj0EAwIw\nGDEWMBQGA1UEAwwNUm9vdCBDQSBUZXN0ZTAeFw0yMTA3MDUyMDQ1NTNaFw0yMjA3\nMDUyMDQ1NTNaMBIxEDAOBgNVBAMMB2RldmljZTUwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAH5LGRR3qM4FMSXSkbFUvt5FwazLtcXwcnhCBdWzHEeHckCplxY6quA\nbVyZcTXwTPhupYDNB5M+z6jY0YRPdbHaEQAk3Y7ycKqAsY+DdpZof6gftGYn3jJ/\n07OC8/39bzh/00B/7hgP0/LRxDBfx/rQBxVltBivF8IWBDAuzFNMzKroXKOBmTCB\nljAdBgNVHQ4EFgQUeMD2DeK0Ls73aHI+BgyOsJJUDc0wHwYDVR0jBBgwFoAUsfFz\nn1jQaorPQjVBFGx9OLgHBQowDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCA+gwHQYD\nVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBoGA1UdEQQTMBGCCWxvY2FsaG9z\ndIcEfwAAATAKBggqhkjOPQQDAgOBjAAwgYgCQgEaWNxZTBivu3L5/ostDww55KhW\n5HLDQkWra9Cjeon1uQH3QyodRui6pELpLFVhTpdacb0XkyfaiDrgjxvhWhkRmgJC\nAZ7DOVSmQn01Yy8+nf4F2Zz7mcxF8h6O2fyLuppHtPF7uAJXXewmnOrL2eatP/hK\nQMZQFe6EOWprSEJiqhnFN8ik\n-----END CERTIFICATE-----"

        self.logger.debug('registering certificate ... com certificateChain - 1 nivel (device5)')
        rc, res = self.registerExternalCertificate(jwt, str(caFingerprint), certificateChain, None)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_device5 = res['certificateFingerprint']
        self.logger.info("certificateFingerprint: " + str(fingerprint_device5))

        caFingerprint = "53:1A:AB:F1:86:F4:BF:B9:44:F7:4A:98:46:BB:05:A7:31:D0:1D:E0:43:51:EF:33:DA:53:FE:46:0B:02:01:48"
        self.logger.info("caFingerprint - CA Root Teste2: " + str(caFingerprint))
        #certificateChain = certificado assinado pela Root CA Teste2, CN=device2
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICTzCCAbCgAwIBAgIUDXs2wKRo1VeC9H97IE5w293a9oMwCgYIKoZIzj0EAwIw\nGTEXMBUGA1UEAwwOUm9vdCBDQSBUZXN0ZTIwHhcNMjEwNjI1MTgwNDM1WhcNMjIw\nNjI1MTgwNDM1WjASMRAwDgYDVQQDDAdkZXZpY2UyMIGbMBAGByqGSM49AgEGBSuB\nBAAjA4GGAAQBg1/F8MbHyWpx0090W23aUPhrnQwKenC+/p7WPNlmYZMYA8hXuKrb\n+fdkSc27HosBlKiXCS2yd+dZi0YZtUbcbmoBIahHpm/GwakWv8r3R/WupKQ7gPzm\nij1a5U8sgDDHAYxcZpcGNQC02b6dp6hZjNF3tw8aA/GjjL8eOqsep17uAQmjgZkw\ngZYwHQYDVR0OBBYEFDezsGGZOC4i4pXYKWlvKeGyBS8oMB8GA1UdIwQYMBaAFFXg\nhY3G4x/GXs5s8xvOhOfdv8qfMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgPoMB0G\nA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAaBgNVHREEEzARgglsb2NhbGhv\nc3SHBH8AAAEwCgYIKoZIzj0EAwIDgYwAMIGIAkIBiyrj9IohxhNk9cmbmty9TXzK\ndrxEyTUZwZs2KwEjTiLfD1RbtBQr5m+P9tu7nebD/q9B6XJVwX7t1nhdB+Qxbq0C\nQgGcEfcxTY6ZEqtLKET6jR1wYoHpH7uAFqi6fz5pRBW6gqqJ2o3926mNWMRxFYUo\nEUhs0ykCZT3G5uUNHJezuJ60tg==\n-----END CERTIFICATE-----"

        self.logger.debug('registering certificate ... com certificateChain - 1 nivel (device2)')
        rc, res = self.registerExternalCertificate(jwt, str(caFingerprint), certificateChain, None)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_device2 = res['certificateFingerprint']
        self.logger.info("certificateFingerprint: " + str(fingerprint_device2))

        #certificateChain = certificado assinado pela Root CA Teste2, CN=dispositivo2
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICUzCCAbWgAwIBAgIUfG4ExAIaikRnrlN2N5XUHGPqOOswCgYIKoZIzj0EAwIw\nGTEXMBUGA1UEAwwOUm9vdCBDQSBUZXN0ZTIwHhcNMjEwNzA2MTMyMjIyWhcNMjIw\nNzA2MTMyMjIyWjAXMRUwEwYDVQQDDAxkaXNwb3NpdGl2bzIwgZswEAYHKoZIzj0C\nAQYFK4EEACMDgYYABAEmDEtErrFtmVDV7nYNAHgHZIlr5m0+lp3xrGL0Slvvw0iq\nxwzzb0dAaK5mAioH1fYEU9Vs6u9y2Egw3k3NlT7UWgAdu0WMZEh3+2zr/36zRTiC\njOYYJmYG7K3Yj6Gddzv3Yu/f8DChtYZooQlyBDPiAT6DHtNy+pB5gYpLHfXglYL8\nPKOBmTCBljAdBgNVHQ4EFgQUAn8Hn4oJfyGKQ2I6Dv9vO78FeiswHwYDVR0jBBgw\nFoAUVeCFjcbjH8ZezmzzG86E592/yp8wDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMC\nA+gwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBoGA1UdEQQTMBGCCWxv\nY2FsaG9zdIcEfwAAATAKBggqhkjOPQQDAgOBiwAwgYcCQgCVlYTr1alXtYjZoNd6\nH2k9C5c3UxJRDzndFdaE+qO4c79sDZklsSE//92+KCunMsOzjkXORBwZoylec0y1\n1unurwJBKqgjfZ7MlHrvdOjJbWiCSi4yaqMLP6t7uRoeDhwBjyqz22mG1O94m6sN\nJToYc/gyElAhsA9SWL1w0gI0+zlsTJQ=\n-----END CERTIFICATE-----"

        self.logger.debug('registering certificate ... com certificateChain - 1 nivel (dispositivo2)')
        rc, res = self.registerExternalCertificate(jwt, str(caFingerprint), certificateChain, None)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_dispositivo2 = res['certificateFingerprint']
        self.logger.info("certificateFingerprint: " + str(fingerprint_dispositivo2))

        #TODO: Registrar um certificado externo – com certificateChain - 2 niveis
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIIHJTCCBg2gAwIBAgISA/c80WOrBS1B0YKU1WnbOIwuMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0yMDEwMDUxMzAyNDRaFw0y\nMTAxMDMxMzAyNDRaMB4xHDAaBgNVBAMMEyouc3RhY2tleGNoYW5nZS5jb20wggEi\nMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDgvEf4788HVB81wIAnFbY556Qb\n7BOB5IhjozLwLS9OsOAn2Dmr+P/456nysCXQAFw/Y98R+INfjTScScZa+WfKM9tk\nTSLrrHuPyFQ0IEwpy59+cdnPoJQWrAu6Y0RGRv27yOOVRyeAqge2pArDiYqrc0sE\nHSrBSS1wsq/nnzcaSZroL9uBqGi8hhe5GJUYk2F5EiexsYxv9jx8uLQ7vpBmk3Et\nJbOlP00unQZH5Wd6swTntOhFUHSE2g3Bj3Wi/Mjhq6spTQmvjazN6+ZT6l+UEFSI\n8PdlS9cH99DlPyVxiZfezobk9CGAfkhWhFRoecXKIeMGY49jUmicuZJfa5A7AgMB\nAAGjggQvMIIEKzAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEG\nCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFK+7kfNW1XVWKaiJnPL+\nLA+dQ6qqMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMG8GCCsGAQUF\nBwEBBGMwYTAuBggrBgEFBQcwAYYiaHR0cDovL29jc3AuaW50LXgzLmxldHNlbmNy\neXB0Lm9yZzAvBggrBgEFBQcwAoYjaHR0cDovL2NlcnQuaW50LXgzLmxldHNlbmNy\neXB0Lm9yZy8wggHkBgNVHREEggHbMIIB14IPKi5hc2t1YnVudHUuY29tghIqLmJs\nb2dvdmVyZmxvdy5jb22CEioubWF0aG92ZXJmbG93Lm5ldIIYKi5tZXRhLnN0YWNr\nZXhjaGFuZ2UuY29tghgqLm1ldGEuc3RhY2tvdmVyZmxvdy5jb22CESouc2VydmVy\nZmF1bHQuY29tgg0qLnNzdGF0aWMubmV0ghMqLnN0YWNrZXhjaGFuZ2UuY29tghMq\nLnN0YWNrb3ZlcmZsb3cuY29tghUqLnN0YWNrb3ZlcmZsb3cuZW1haWyCDyouc3Vw\nZXJ1c2VyLmNvbYINYXNrdWJ1bnR1LmNvbYIQYmxvZ292ZXJmbG93LmNvbYIQbWF0\naG92ZXJmbG93Lm5ldIIUb3BlbmlkLnN0YWNrYXV0aC5jb22CD3NlcnZlcmZhdWx0\nLmNvbYILc3N0YXRpYy5uZXSCDXN0YWNrYXBwcy5jb22CDXN0YWNrYXV0aC5jb22C\nEXN0YWNrZXhjaGFuZ2UuY29tghJzdGFja292ZXJmbG93LmJsb2eCEXN0YWNrb3Zl\ncmZsb3cuY29tghNzdGFja292ZXJmbG93LmVtYWlsghFzdGFja3NuaXBwZXRzLm5l\ndIINc3VwZXJ1c2VyLmNvbTBMBgNVHSAERTBDMAgGBmeBDAECATA3BgsrBgEEAYLf\nEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCC\nAQMGCisGAQQB1nkCBAIEgfQEgfEA7wB1AJQgvB6O1Y1siHMfgosiLA3R2k1ebE+U\nPWHbTi9YTaLCAAABdPkSXP4AAAQDAEYwRAIgVay70Cu9d46NEOmUt3XUu7bXIqkS\nh+DQXw0Rdy5qIQ0CIH4GmNouXeCovRlx/T4B9Hh//+VvA1tBakgiq+6WEPR8AHYA\nfT7y+I//iFVoJMLAyp5SiXkrxQ54CX8uapdomX4i8NcAAAF0+RJdVgAABAMARzBF\nAiEAs4iZyvg1zC2zaFCs9CNuiGhkuD3cdmcuPCx1qi7rZqcCIAQIaxcyd5wkVWNj\n1CeXrUriThrMyOElkNXaN34j3WqUMA0GCSqGSIb3DQEBCwUAA4IBAQA5BQYZcDBu\nh1NnUYspMTFcuDjYSmZDlD9MBTSaA4alsHN2l+jsz/cLgPNZWdOhn1NPb6OU3x4J\nAOz/4waQvqQ0VYhjBplLMiH3HPXHIiaHJw+p+Hdz0gi3gMcvuoz7ifu+9GemmdGV\nwdpeGuZP4NQXJCnuNhwjrqFQHuoimKvm2M555fJB+ij+p3K2KhbQnq2BKnn2EqIR\nOX9Euhv1TVpUz+rSSJJ89tIUAqzpHSS6CJt3Z3Ljgtyy1u0J1+UNlJ69JNEZIhsG\nfcfc6rV6/wF3uRRBdJck9qyMCejg7NESyxTGnj+QcgbzEpMbGdzZ0PCyvaJWccl7\nqysRzGiJF1WI\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----"
        device_id = ""

        self.logger.debug('registering certificate ... com certificateChain - 2 niveis')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, device_id)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        """

        #TODO:Registrar um certificado externo – com certificateChain - incluindo CA externa
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIIHJTCCBg2gAwIBAgISA/c80WOrBS1B0YKU1WnbOIwuMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0yMDEwMDUxMzAyNDRaFw0y\nMTAxMDMxMzAyNDRaMB4xHDAaBgNVBAMMEyouc3RhY2tleGNoYW5nZS5jb20wggEi\nMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDgvEf4788HVB81wIAnFbY556Qb\n7BOB5IhjozLwLS9OsOAn2Dmr+P/456nysCXQAFw/Y98R+INfjTScScZa+WfKM9tk\nTSLrrHuPyFQ0IEwpy59+cdnPoJQWrAu6Y0RGRv27yOOVRyeAqge2pArDiYqrc0sE\nHSrBSS1wsq/nnzcaSZroL9uBqGi8hhe5GJUYk2F5EiexsYxv9jx8uLQ7vpBmk3Et\nJbOlP00unQZH5Wd6swTntOhFUHSE2g3Bj3Wi/Mjhq6spTQmvjazN6+ZT6l+UEFSI\n8PdlS9cH99DlPyVxiZfezobk9CGAfkhWhFRoecXKIeMGY49jUmicuZJfa5A7AgMB\nAAGjggQvMIIEKzAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEG\nCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFK+7kfNW1XVWKaiJnPL+\nLA+dQ6qqMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMG8GCCsGAQUF\nBwEBBGMwYTAuBggrBgEFBQcwAYYiaHR0cDovL29jc3AuaW50LXgzLmxldHNlbmNy\neXB0Lm9yZzAvBggrBgEFBQcwAoYjaHR0cDovL2NlcnQuaW50LXgzLmxldHNlbmNy\neXB0Lm9yZy8wggHkBgNVHREEggHbMIIB14IPKi5hc2t1YnVudHUuY29tghIqLmJs\nb2dvdmVyZmxvdy5jb22CEioubWF0aG92ZXJmbG93Lm5ldIIYKi5tZXRhLnN0YWNr\nZXhjaGFuZ2UuY29tghgqLm1ldGEuc3RhY2tvdmVyZmxvdy5jb22CESouc2VydmVy\nZmF1bHQuY29tgg0qLnNzdGF0aWMubmV0ghMqLnN0YWNrZXhjaGFuZ2UuY29tghMq\nLnN0YWNrb3ZlcmZsb3cuY29tghUqLnN0YWNrb3ZlcmZsb3cuZW1haWyCDyouc3Vw\nZXJ1c2VyLmNvbYINYXNrdWJ1bnR1LmNvbYIQYmxvZ292ZXJmbG93LmNvbYIQbWF0\naG92ZXJmbG93Lm5ldIIUb3BlbmlkLnN0YWNrYXV0aC5jb22CD3NlcnZlcmZhdWx0\nLmNvbYILc3N0YXRpYy5uZXSCDXN0YWNrYXBwcy5jb22CDXN0YWNrYXV0aC5jb22C\nEXN0YWNrZXhjaGFuZ2UuY29tghJzdGFja292ZXJmbG93LmJsb2eCEXN0YWNrb3Zl\ncmZsb3cuY29tghNzdGFja292ZXJmbG93LmVtYWlsghFzdGFja3NuaXBwZXRzLm5l\ndIINc3VwZXJ1c2VyLmNvbTBMBgNVHSAERTBDMAgGBmeBDAECATA3BgsrBgEEAYLf\nEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCC\nAQMGCisGAQQB1nkCBAIEgfQEgfEA7wB1AJQgvB6O1Y1siHMfgosiLA3R2k1ebE+U\nPWHbTi9YTaLCAAABdPkSXP4AAAQDAEYwRAIgVay70Cu9d46NEOmUt3XUu7bXIqkS\nh+DQXw0Rdy5qIQ0CIH4GmNouXeCovRlx/T4B9Hh//+VvA1tBakgiq+6WEPR8AHYA\nfT7y+I//iFVoJMLAyp5SiXkrxQ54CX8uapdomX4i8NcAAAF0+RJdVgAABAMARzBF\nAiEAs4iZyvg1zC2zaFCs9CNuiGhkuD3cdmcuPCx1qi7rZqcCIAQIaxcyd5wkVWNj\n1CeXrUriThrMyOElkNXaN34j3WqUMA0GCSqGSIb3DQEBCwUAA4IBAQA5BQYZcDBu\nh1NnUYspMTFcuDjYSmZDlD9MBTSaA4alsHN2l+jsz/cLgPNZWdOhn1NPb6OU3x4J\nAOz/4waQvqQ0VYhjBplLMiH3HPXHIiaHJw+p+Hdz0gi3gMcvuoz7ifu+9GemmdGV\nwdpeGuZP4NQXJCnuNhwjrqFQHuoimKvm2M555fJB+ij+p3K2KhbQnq2BKnn2EqIR\nOX9Euhv1TVpUz+rSSJJ89tIUAqzpHSS6CJt3Z3Ljgtyy1u0J1+UNlJ69JNEZIhsG\nfcfc6rV6/wF3uRRBdJck9qyMCejg7NESyxTGnj+QcgbzEpMbGdzZ0PCyvaJWccl7\nqysRzGiJF1WI\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIDSjCCAjKgAwIBAgIQRK+wgNajJ7qJMDmGLvhAazANBgkqhkiG9w0BAQUFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTAwMDkzMDIxMTIxOVoXDTIxMDkzMDE0MDExNVow\nPzEkMCIGA1UEChMbRGlnaXRhbCBTaWduYXR1cmUgVHJ1c3QgQ28uMRcwFQYDVQQD\nEw5EU1QgUm9vdCBDQSBYMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN+v6ZdQCINXtMxiZfaQguzH0yxrMMpb7NnDfcdAwRgUi+DoM3ZJKuM/IUmTrE4O\nrz5Iy2Xu/NMhD2XSKtkyj4zl93ewEnu1lcCJo6m67XMuegwGMoOifooUMM0RoOEq\nOLl5CjH9UL2AZd+3UWODyOKIYepLYYHsUmu5ouJLGiifSKOeDNoJjj4XLh7dIN9b\nxiqKqy69cK3FCxolkHRyxXtqqzTWMIn/5WgTe1QLyNau7Fqckh49ZLOMxt+/yUFw\n7BZy1SbsOFU5Q9D8/RhcQPGX69Wam40dutolucbY38EVAjqr2m7xPi71XAicPNaD\naeQQmxkqtilX4+U9m5/wAl0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNV\nHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFMSnsaR7LHH62+FLkHX/xBVghYkQMA0GCSqG\nSIb3DQEBBQUAA4IBAQCjGiybFwBcqR7uKGY3Or+Dxz9LwwmglSBd49lZRNI+DT69\nikugdB/OEIKcdBodfpga3csTS7MgROSR6cz8faXbauX+5v3gTt23ADq1cEmv8uXr\nAvHRAosZy5Q6XkjEGB5YGV8eAlrwDPGxrancWYaLbumR9YbK+rlmM6pZW87ipxZz\nR8srzJmwN0jP41ZL9c8PDHIyh8bwRLtTcm1D9SZImlJnt1ir/md2cXjbDaJWFBM5\nJDGFoqgCWjBH4d1QB7wCCZAA62RjYJsWvIjJEubSfZGL+T0yjWW06XyxV3bqxbYo\nOb8VZRzI9neWagqNdwvYkQsEjgfbKbYK7p2CNTUQ\n-----END CERTIFICATE-----"
        device_id = ""

        self.logger.debug('registering certificate ... certificateChain com CA externa')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, device_id)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
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
        """
        # caFingerprint da CA RootTeste
        caFingerprint = "4F:64:DE:09:24:AB:EC:C3:F0:96:41:E2:94:98:45:97:19:B0:26:EF:02:16:7A:44:DA:0F:C6:05:BE:BC:86:EA"
        # certificateChain = certificado assinado pela Root CA Teste, CN=device3
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICTTCCAa+gAwIBAgIUDXs2wKRo1VeC9H97IE5w293a9oIwCgYIKoZIzj0EAwIw\nGDEWMBQGA1UEAwwNUm9vdCBDQSBUZXN0ZTAeFw0yMTA2MTgxOTM5MDZaFw0yMjA2\nMTgxOTM5MDZaMBIxEDAOBgNVBAMMB2RldmljZTMwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABABBU7UQ/VO7VVvE19XtxQDpeZDreuPy/Z7jQe0dJeGFw7G26HrUsI1x\nA8Fka0zkR6U4DdTvhXu2sH1QcMY1EIZYCwC4cHcX63pYXtKL1/J1mXR95XjRfr9C\n7MvKj+AN72kZnpokzQFRblanHRWRlD9qskNZbb55MZbAUAUUbgyRD4EAVaOBmTCB\nljAdBgNVHQ4EFgQUIMcNVdBggmro1ZMe+8xKP26gDk4wHwYDVR0jBBgwFoAUsfFz\nn1jQaorPQjVBFGx9OLgHBQowDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCA+gwHQYD\nVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBoGA1UdEQQTMBGCCWxvY2FsaG9z\ndIcEfwAAATAKBggqhkjOPQQDAgOBiwAwgYcCQRe+1t0mWzZMRtYaMV88ert9HXvK\nhfkQVGLAZ4UmrAC453j/2o2quRXPJlMGfegMVWH3rC+QDhOA85dJL46VlyCMAkIB\neQ0NjbStvG5L1mazXnl7WLLQ//GxCEX7cYECahMR4gnBL29fo672fqA0wqGmUPQr\neWaAJ13fpdoRSp6Is37XsoQ=\n-----END CERTIFICATE-----"
        device_id = "ae8533"
        self.logger.debug('registering certificate ... com dispositivo associado: device3, device_id ae8533')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, device_id)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_device3 = res['certificateFingerprint']
        self.logger.info("certificateFingerprint: " + str(fingerprint_device3))

        # caFingerprint da CA RootTeste2
        caFingerprint = "53:1A:AB:F1:86:F4:BF:B9:44:F7:4A:98:46:BB:05:A7:31:D0:1D:E0:43:51:EF:33:DA:53:FE:46:0B:02:01:48"
        # certificateChain = certificado assinado pela Root CA Teste2, CN=device
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICTjCCAa+gAwIBAgIUDXs2wKRo1VeC9H97IE5w293a9oUwCgYIKoZIzj0EAwIw\nGTEXMBUGA1UEAwwOUm9vdCBDQSBUZXN0ZTIwHhcNMjEwNjI1MTgxNjIzWhcNMjIw\nNjI1MTgxNjIzWjARMQ8wDQYDVQQDDAZkZXZpY2UwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABABTXDme3BjAr1nt9cXWYksDjxgWDlR5jrxZmTjA4k3f/lOyzolbGEyw\nfQUHrxmIMoOCsMj0Nnmei0GHVor2KlsKqACQYxK+YS23QwqD2DYQ1nc8ro/ozFzz\nfzx8PplkDHfD2XjerCSUg05Z1fJz+pRqvucqNgQsgJTtcLO2g24MMQNktaOBmTCB\nljAdBgNVHQ4EFgQUAwHw8Z1rZUF7X/xzhVN+9fUbw0QwHwYDVR0jBBgwFoAUVeCF\njcbjH8ZezmzzG86E592/yp8wDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCA+gwHQYD\nVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBoGA1UdEQQTMBGCCWxvY2FsaG9z\ndIcEfwAAATAKBggqhkjOPQQDAgOBjAAwgYgCQgDg7gF2oyndSPVK5D3uJqDWTg28\nM+Y1bfImiEBWG/3+CPFoOkcrQaMW0AULN38rWM7aj28DT726IcQFGpxk6peetQJC\nAYhdPPoy63ZuydSfRoNkP8alUd/sCQLBM/fvUV4moRPE441VJlOI88gbHadAnYjU\niAK8f3GZcOK6rvBNBvqL+l8C\n-----END CERTIFICATE-----"
        device_id = "f67d46"
        self.logger.debug('registering certificate ... com dispositivo associado: device, device_id f67d46')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, device_id)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        fingerprint_device = res['certificateFingerprint']
        self.logger.info("certificateFingerprint: " + str(fingerprint_device))

        """
        Registrar um certificado externo (CN=dispositivo) - Trusted CA não cadastrada (CN=Root CA Teste3)
        """
        caFingerprint = "7C:0D:0B:3A:ED:33:E9:AF:62:46:77:3E:3B:54:D5:BF:F1:23:67:46:E7:94:54:75:12:BA:DE:C9:88:89:35:23"
        #certificateChain = "-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICUjCCAbSgAwIBAgIUDXs2wKRo1VeC9H97IE5w293a9oYwCgYIKoZIzj0EAwIw\nGTEXMBUGA1UEAwwOUm9vdCBDQSBUZXN0ZTMwHhcNMjEwNjI1MjIyNjQ1WhcNMjIw\nNjI1MjIyNjQ1WjAWMRQwEgYDVQQDDAtkaXNwb3NpdGl2bzCBmzAQBgcqhkjOPQIB\nBgUrgQQAIwOBhgAEAF44plpEtN6qHA5tFHGmqaOVG6vXGYAkUu43vNB6xq+OgeZ6\nzEMvAO7X4rg4Bp2Xc1y0V3QtG19jKv/I3zEH7Q0vAI8Yb4OSZSDsjoQjA1O2D74g\nwVlcCJ7G/MnHOaxU5PQXwcMbV2qOlrSw3YMFPdOdrNidmfrH7ICe+GAjGbCSSeoX\no4GZMIGWMB0GA1UdDgQWBBQ/unAYZEobvR+7JqURYShy4tjs3zAfBgNVHSMEGDAW\ngBSxVy6D4vwtDL2KfPwZ1ndA8xG7UDAMBgNVHRMBAf8EAjAAMAsGA1UdDwQEAwID\n6DAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwGgYDVR0RBBMwEYIJbG9j\nYWxob3N0hwR/AAABMAoGCCqGSM49BAMCA4GLADCBhwJCANu3whMA6YHj/dU2dujO\n0wLy7Ptpkpd6vTdULt/P6nvRNb5aM/FvouZ7SVcW1cPwKM0e3RL0xivzTguE1Nuc\nC0/rAkFO8jv6/v/hvV2goZO0jFieBV0pXzywY8jDrf8qNr3yhXo5p3ezdqCy4CBW\nlUZ1dssoGNDbX9hPBsk83Ai1cZveqQ==\n-----END CERTIFICATE-----"
        device_id = Api.get_deviceid_by_label(jwt, "dispositivo")
        self.logger.info('device_id: ' + device_id)
        self.logger.debug('registering certificate ... Trusted CA não cadastrada')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, device_id)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registrar um certificado externo -  com certificateChain vazio
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        self.logger.info('device_id: ' + device_id)
        self.logger.debug('registering certificate ... empty certificateChain')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, "", device_id)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
         Registrar um certificado externo, certificateChain inválido
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,F57524B7B26F4694\nIJ/e6Xrf4pTBSO+CHdcqGocyAj5ysUre5BwTp6Yk2w9P/r7si7YA+pivghbUzYKc\nuy2hFwWG+LVajZXaG0dFXmbDHd9oYlW/SeJhPrxMvxaqC9R/x4MugAMFOhCQGMq3\nXW58R70L48BIuG6TCSOAGIwMDowv5ToL4nZYnqIRT77aACcsM0ozC+LCyqmLvvsU\nNV/YX4ZgMhzaT2eVK+mtOut6m1Wb7t6iUCS14dB/fTF+RaGYYZYMGut/alFaPqj0\n/KKlTNxCRD99+UZDbg3TnxIFSZd00zY75votTZnlLypoB9pUFP5iQglvuQ4pD3Ux\nbzU4cO0/hrdo04wORwWG/DUoAPlq8wjGei5jbEwHQJ8fNBzCl3Zy5Fx3bcAaaXEK\nzB97cyqhr80f2KnyiAKzk7vmyuRtMO/6Y4yE+1mLFE7NWcRkGXLEd3+wEt8DEq2R\nnQibvRTbT26HkO0bcfBAaeOYxHawdNcF2SZ1dUSZeo/teHNBI2JD5xRgtEPekXRs\nbBuCmxUevuh2+Q632oOpNNpFWBJTsyTcp9cAsxTEkbOCicxLN6c1+GvwyIqfSykR\nG08Y5M88n7Ey5GZ43KUbGh60vV5QN/mzhf3SotBl9+wetpm+4AmkKVUQyQVdRrn2\n1jXrkUZcSN8VbYk2tB74/FFXuaaF2WRQNawceXjrvegxz3/AkjZ7ahYI4rgptCqz\nOXvMk+le5tmVKbJfl1G+EZm2CqDLly5makeMKvX3fSWefKoZSbN0NuW28RgSJIQC\npqja3dWZyGl7Z9dlM+big0nbLhMdIvT8526lD+p+9aMMuBL14MhWGp4IIfvXOPR+\nOts3ZoGR9vtPQyO6YN5/CtRp1DBbRA48W9xk0BnnjSNpFBLY4ykqZj/cS01Up88x\nUMATqoMLiBwKCyaeibiIXpzqPTagG3PEEJkYPsrG/zql1EktjTtNo4LaYdFuZZzb\nfMmcEpFZLerCIgu2cOnhhKwCHYWbZ2MSVsgoiu6RyqqBblAfNkttthiPtCLY82sQ\n2ejN3NMsq+xlc/ISc21eClUaoUXmvyaSf2E3D4CN3FAi8fD74fP64EiKr+JjMNUC\nDWZ79UdwZcpl2VJ7JUAAyRzEt66U5PwQqv1U8ITjsBjykxRQ68/c/+HCOfg9NYn3\ncmpK5UxdFGj6261c6nVRlLVmV0+mPj1+sWHow5jZiH81IuoL3zqGkKzqy5FkTgs4\nMG3hViN9lHEmMPZdK16EPhCwvff0eBV+vhfPjmGoAE6TK3YY/yh9bfhMliLoc1jr\nNmPxL0FWrNzqWxZwMtDYcXu4KUesBL6/Hr+K9HSUa8zF+4UbELJTPOd1QAU6HF7a\n9BidzGMZ+J2Vjqa/NGpWckBRjWb6S7aItK6rrtORU1QHmpQlYpqEh49sreo6DCrb\ns8yejjKm2gSB/KhTe1nJXcTM16Xa4qWXTv11x46FNTZPUWQ7KoI0AzzScn6StBdo\nYCvzqCrla1em/Kakkws7Qu/pVj9R8ndHzoLktOi3l6lwwy5d4L697DyhP+02+eLt\nSBefoVnBNp449CSHW+brvPEyKD3D5CVpTIDfu2y8+nHszfBL22wuO4T+oem5h55A\n-----END RSA PRIVATE KEY-----"
        self.logger.info('device_id: ' + device_id)
        self.logger.debug('registering certificate ... invalid certificateChain')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, device_id)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registrar um certificado externo - The certificate chain of trust is not valid.
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIICYzCCAcagAwIBAgIUJO+7ZVClAgCuMwNNa0czfje7jhkwCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMTA2MTYyMDA0MzlaFw0yMjA2MTYyMDA0MzlaMBExDzANBgNVBAMMBjljN2Uw\nNjCBmzAQBgcqhkjOPQIBBgUrgQQAIwOBhgAEARx1mFV6ib+zAwyqZva0p7hgNint\no9fqAORH19WluwwJxdRpfCNn4v55nc+J4LE8fgciHEnOLqHaFGMjNcLGNXDcAFTv\nFPOPlUjGzfWegZwtgHtlGrLaZEEQK3CtcHlCkrDTp7P5L52uEZhkAlxVNuNUxUUh\nsRxmv/WIuZIEyNTQqpTBo4GcMIGZMB0GA1UdDgQWBBTcZo9b96/QYJ0jiO8jEDwc\nM+KXazAfBgNVHSMEGDAWgBQm7lNXxFGPGBxQkoDHuTfEZTv0gzAMBgNVHRMBAf8E\nAjAAMAsGA1UdDwQEAwID6DAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIw\nHQYDVR0RBBYwFIIMZG9qb3QuY29tLmJyhwR/AAABMAoGCCqGSM49BAMCA4GKADCB\nhgJBQbnPvidH9jlZgedttQ+FLq/r9K2xjfW08dvs2DlUf0fzCEmHg8lsQ9s0buLO\nzO9C3BD0eYAeElaH6OlF1eCJZB0CQXtRI0f40Dro+UJ50866NbYT112VtTasAG0W\n8wz356bohFlvmbIoa0y9pkMwPsGtRHd+Jz+YlU7he8d8pE5VG2D9\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIDSjCCAjKgAwIBAgIQRK+wgNajJ7qJMDmGLvhAazANBgkqhkiG9w0BAQUFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTAwMDkzMDIxMTIxOVoXDTIxMDkzMDE0MDExNVow\nPzEkMCIGA1UEChMbRGlnaXRhbCBTaWduYXR1cmUgVHJ1c3QgQ28uMRcwFQYDVQQD\nEw5EU1QgUm9vdCBDQSBYMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAN+v6ZdQCINXtMxiZfaQguzH0yxrMMpb7NnDfcdAwRgUi+DoM3ZJKuM/IUmTrE4O\nrz5Iy2Xu/NMhD2XSKtkyj4zl93ewEnu1lcCJo6m67XMuegwGMoOifooUMM0RoOEq\nOLl5CjH9UL2AZd+3UWODyOKIYepLYYHsUmu5ouJLGiifSKOeDNoJjj4XLh7dIN9b\nxiqKqy69cK3FCxolkHRyxXtqqzTWMIn/5WgTe1QLyNau7Fqckh49ZLOMxt+/yUFw\n7BZy1SbsOFU5Q9D8/RhcQPGX69Wam40dutolucbY38EVAjqr2m7xPi71XAicPNaD\naeQQmxkqtilX4+U9m5/wAl0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNV\nHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFMSnsaR7LHH62+FLkHX/xBVghYkQMA0GCSqG\nSIb3DQEBBQUAA4IBAQCjGiybFwBcqR7uKGY3Or+Dxz9LwwmglSBd49lZRNI+DT69\nikugdB/OEIKcdBodfpga3csTS7MgROSR6cz8faXbauX+5v3gTt23ADq1cEmv8uXr\nAvHRAosZy5Q6XkjEGB5YGV8eAlrwDPGxrancWYaLbumR9YbK+rlmM6pZW87ipxZz\nR8srzJmwN0jP41ZL9c8PDHIyh8bwRLtTcm1D9SZImlJnt1ir/md2cXjbDaJWFBM5\nJDGFoqgCWjBH4d1QB7wCCZAA62RjYJsWvIjJEubSfZGL+T0yjWW06XyxV3bqxbYo\nOb8VZRzI9neWagqNdwvYkQsEjgfbKbYK7p2CNTUQ\n-----END CERTIFICATE-----"
        device_id = "9c7e06"

        self.logger.debug('registering certificate ... com dispositivo associado: device4, device_id 9c7e06')
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, device_id)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        #TODO: Registrar um certificado externo – invalid request (ex: sem chave Authorization)

        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIIHJTCCBg2gAwIBAgISA/c80WOrBS1B0YKU1WnbOIwuMA0GCSqGSIb3DQEBCwUA\nMEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD\nExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0yMDEwMDUxMzAyNDRaFw0y\nMTAxMDMxMzAyNDRaMB4xHDAaBgNVBAMMEyouc3RhY2tleGNoYW5nZS5jb20wggEi\nMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDgvEf4788HVB81wIAnFbY556Qb\n7BOB5IhjozLwLS9OsOAn2Dmr+P/456nysCXQAFw/Y98R+INfjTScScZa+WfKM9tk\nTSLrrHuPyFQ0IEwpy59+cdnPoJQWrAu6Y0RGRv27yOOVRyeAqge2pArDiYqrc0sE\nHSrBSS1wsq/nnzcaSZroL9uBqGi8hhe5GJUYk2F5EiexsYxv9jx8uLQ7vpBmk3Et\nJbOlP00unQZH5Wd6swTntOhFUHSE2g3Bj3Wi/Mjhq6spTQmvjazN6+ZT6l+UEFSI\n8PdlS9cH99DlPyVxiZfezobk9CGAfkhWhFRoecXKIeMGY49jUmicuZJfa5A7AgMB\nAAGjggQvMIIEKzAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEG\nCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFK+7kfNW1XVWKaiJnPL+\nLA+dQ6qqMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMG8GCCsGAQUF\nBwEBBGMwYTAuBggrBgEFBQcwAYYiaHR0cDovL29jc3AuaW50LXgzLmxldHNlbmNy\neXB0Lm9yZzAvBggrBgEFBQcwAoYjaHR0cDovL2NlcnQuaW50LXgzLmxldHNlbmNy\neXB0Lm9yZy8wggHkBgNVHREEggHbMIIB14IPKi5hc2t1YnVudHUuY29tghIqLmJs\nb2dvdmVyZmxvdy5jb22CEioubWF0aG92ZXJmbG93Lm5ldIIYKi5tZXRhLnN0YWNr\nZXhjaGFuZ2UuY29tghgqLm1ldGEuc3RhY2tvdmVyZmxvdy5jb22CESouc2VydmVy\nZmF1bHQuY29tgg0qLnNzdGF0aWMubmV0ghMqLnN0YWNrZXhjaGFuZ2UuY29tghMq\nLnN0YWNrb3ZlcmZsb3cuY29tghUqLnN0YWNrb3ZlcmZsb3cuZW1haWyCDyouc3Vw\nZXJ1c2VyLmNvbYINYXNrdWJ1bnR1LmNvbYIQYmxvZ292ZXJmbG93LmNvbYIQbWF0\naG92ZXJmbG93Lm5ldIIUb3BlbmlkLnN0YWNrYXV0aC5jb22CD3NlcnZlcmZhdWx0\nLmNvbYILc3N0YXRpYy5uZXSCDXN0YWNrYXBwcy5jb22CDXN0YWNrYXV0aC5jb22C\nEXN0YWNrZXhjaGFuZ2UuY29tghJzdGFja292ZXJmbG93LmJsb2eCEXN0YWNrb3Zl\ncmZsb3cuY29tghNzdGFja292ZXJmbG93LmVtYWlsghFzdGFja3NuaXBwZXRzLm5l\ndIINc3VwZXJ1c2VyLmNvbTBMBgNVHSAERTBDMAgGBmeBDAECATA3BgsrBgEEAYLf\nEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCC\nAQMGCisGAQQB1nkCBAIEgfQEgfEA7wB1AJQgvB6O1Y1siHMfgosiLA3R2k1ebE+U\nPWHbTi9YTaLCAAABdPkSXP4AAAQDAEYwRAIgVay70Cu9d46NEOmUt3XUu7bXIqkS\nh+DQXw0Rdy5qIQ0CIH4GmNouXeCovRlx/T4B9Hh//+VvA1tBakgiq+6WEPR8AHYA\nfT7y+I//iFVoJMLAyp5SiXkrxQ54CX8uapdomX4i8NcAAAF0+RJdVgAABAMARzBF\nAiEAs4iZyvg1zC2zaFCs9CNuiGhkuD3cdmcuPCx1qi7rZqcCIAQIaxcyd5wkVWNj\n1CeXrUriThrMyOElkNXaN34j3WqUMA0GCSqGSIb3DQEBCwUAA4IBAQA5BQYZcDBu\nh1NnUYspMTFcuDjYSmZDlD9MBTSaA4alsHN2l+jsz/cLgPNZWdOhn1NPb6OU3x4J\nAOz/4waQvqQ0VYhjBplLMiH3HPXHIiaHJw+p+Hdz0gi3gMcvuoz7ifu+9GemmdGV\nwdpeGuZP4NQXJCnuNhwjrqFQHuoimKvm2M555fJB+ij+p3K2KhbQnq2BKnn2EqIR\nOX9Euhv1TVpUz+rSSJJ89tIUAqzpHSS6CJt3Z3Ljgtyy1u0J1+UNlJ69JNEZIhsG\nfcfc6rV6/wF3uRRBdJck9qyMCejg7NESyxTGnj+QcgbzEpMbGdzZ0PCyvaJWccl7\nqysRzGiJF1WI\n-----END CERTIFICATE-----"

        self.logger.debug('registering certificate ... invalid request - TODO')
        """
        rc, res = self.registerExternalCertificate(jwt, caFingerprint, certificateChain, 0)
        self.logger.info("certificateFingerprint: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        """

        """
        Registrar um certificado externo – JWT vazio
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----"
        self.logger.debug('registering certificate ... empty JWT')
        rc, res = self.registerExternalCertificate("", caFingerprint, certificateChain, "")
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Registrar um certificado externo – JWT invalido
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----"
        self.logger.debug('registering certificate ... invalid JWT')
        rc, res = self.registerExternalCertificate("", caFingerprint, certificateChain, "")
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Registrar um certificado externo – operação não autorizada
        """
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        certificateChain = "-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----"
        self.logger.debug('registering certificate - not authorized operation...')
        rc, res = self.registerExternalCertificate(token, caFingerprint, certificateChain, "")
        self.logger.info("message: " + str(rc) + ", " + str(res))
        self.assertTrue(int(rc) == 403, "codigo inesperado")
        """

        self.logger.debug('registering trusted CA - Only one CA certificate is expected per request.... ')
        #CN=Root CA Dojot + Root CA Teste2
        caPem = "-----BEGIN CERTIFICATE-----\nMIIF6jCCA9KgAwIBAgIUNyzcpYLXAmKe+flbfSbyXjSF/B8wDQYJKoZIhvcNAQEL\nBQAwejEjMCEGCgmSJomT8ixkAQEME2MtMGE3NGU5ZmM3MzE3NDFjZjQxGTAXBgNV\nBAMMEFg1MDkgSWRlbnRpdHkgQ0ExGzAZBgNVBAsMEkNlcnRpZmljYXRlIElzc3Vl\ncjEbMBkGA1UECgwSZG9qb3QgSW9UIFBsYXRmb3JtMCAXDTIxMDYyMTExNTMwNVoY\nDzIwNTEwNjE0MTE1MzA1WjB6MSMwIQYKCZImiZPyLGQBAQwTYy0wYTc0ZTlmYzcz\nMTc0MWNmNDEZMBcGA1UEAwwQWDUwOSBJZGVudGl0eSBDQTEbMBkGA1UECwwSQ2Vy\ndGlmaWNhdGUgSXNzdWVyMRswGQYDVQQKDBJkb2pvdCBJb1QgUGxhdGZvcm0wggIi\nMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDO89/kQ3KEm8rU9F9HSh6GMLly\nEGWfGU40JYr2lUFp+obloHJJlgrJEQU4dngTszux7N69XGr0nUvzgy8BakxMmV0/\ne2kI9PeE8rE2678LMsOU0dDtJJyXsfmaajp5FK4SQzvwQQNB9olPfupY1jVmAU8y\nED8t/3rZhgajAw6Nff3GoTPA9Jcp9PuqMSgbx+kHMThfyN5xWRvBqTgpJCUVCT8C\nJTVWsL44UGkxUWQBSdz4iV4SjW4sQhfYr9h8oJJeYwqvHf9Bi/dBxVPdEEKb+puy\nwaSuwKWfmbqRinMK4T5R4t0pji3aiB5ITKNn1t+H3EhAYpjIFIGmCPHlHAtdQg1S\nwfXVpVEyHkVALg0xYQBiQ/TnevuJlBz2Hp7nvvIBVsNgVUK9GsSACi/2oGiTLOpM\nxyl3EIil2VE/0GWaKrTFaPaalk/4V28HA0bjuSwfhCJt7Pm3ilpbdUQpF8Uuj7Sx\nU+rL835kMYKv0ZfvY9WRbtJlbIE+6Vi6y+E1vO8q8LGvSm/wF0MNQgI9QOYPWIBU\nVQ+LZlAkr0pgGm2SDwAInr8SQ+G1eG+W20rQB5YUlXm9OzOnB/IZr8s8nP1C84xw\nK+A9DJOC0d+yo/kxfDyEFk7j63Fxg95PJa3kBe447f4JHVSGcC8n8HO5hEnyK91P\ngOsOSHYjxS1+Xj+6vQIDAQABo2YwZDASBgNVHRMBAf8ECDAGAQH/AgEAMB8GA1Ud\nIwQYMBaAFJrbsILKDC3rSTiofJDVSHVK4JnuMB0GA1UdDgQWBBSa27CCygwt60k4\nqHyQ1Uh1SuCZ7jAOBgNVHQ8BAf8EBAMCAYYwDQYJKoZIhvcNAQELBQADggIBAHjy\nxE0N8KDlgMTe82skT0yT8C4HXzwSL8N8QvSGmmRYd5xvRTvvI07akjZksx1pTfto\nQsVk4KOs1U7ch8dcRZ7xhc0Z7fv+Phmm3X79PRTKGVMQgTBMNne8SDbdRsJf4+W+\nM/lvVFBn8U7Kk0Z3hiMX13DJ7nlRrji9e1W10YvT4HI3XaykmP4eXV3ajquMdx27\nKBQc1foKr4S22aHCx2O/HggxP+9BCHx5oJ5nzH/wHHqsrS4ual22HbItdToiYU9q\n5UDWQH+FfRoYYuhYzVxwhUN7HaKEHiatpSqpjR2mDRWERFDDuANK6V2gPIbuHWfi\nfPkSC8W/ZwStx0EbizBfXaT2kQZLwgZkscZRpQARMbkYntUAdm+vnaJ+hogABm8H\nc6P49dMa8gbrXmm06JFqbTr5RlIyYq3iXyg0+leeMJm7M89r8aK3p5U/4MwJ7P6b\nifc5QFeR4QEiaFmNb9UbUZDkn0r9SMhq8PAJh/Oi2fJX1DBLk8g0nJ1PzTdg+s06\ngRdztmHptIc2tr3gzkPbTtvUN0nADeBbhcnwPVZnWMUPaOyiugmiiuCXHeVHXT2o\nGLG8AGuqed2bY6Po5tXD5GGYdbPg0CmrPyEHYX5fWguxjNnu0fNi82ykpiUWRzbX\ntZ5A21EJAP9J/d0w0GAO31KgcWY+vALv/r6zwCQF\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIICDjCCAXCgAwIBAgIUV5S5IYicPqJWWU3GVhSVZfH+UbIwCgYIKoZIzj0EAwIw\nGTEXMBUGA1UEAwwOUm9vdCBDQSBUZXN0ZTIwHhcNMjEwNjI1MTIzMTUwWhcNMjYw\nNjI0MTIzMTUwWjAZMRcwFQYDVQQDDA5Sb290IENBIFRlc3RlMjCBmzAQBgcqhkjO\nPQIBBgUrgQQAIwOBhgAEAU5GkPFlFyAv6xsxCrkQlmiFrrMSIrxjrBMjF56/kUk2\n/jqtSO4y8kCgLwpisQzybazSTunWqlPN2MN75bX4nQznAEQ8ED7ad1NB33T1RBHf\nBnX7naQunEU1nKeqXHkL0Ey2484LvU4Tl5kMrXmg+80Yhu0w/arKE3Kb63hm3Jxj\nQX4Co1MwUTAdBgNVHQ4EFgQUVeCFjcbjH8ZezmzzG86E592/yp8wHwYDVR0jBBgw\nFoAUVeCFjcbjH8ZezmzzG86E592/yp8wDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjO\nPQQDAgOBiwAwgYcCQgHRg0ofa+wxJUJGVjkUDV7Cl+Ka/yY7hrvaFlpusoKUg763\nCiNKDT+Qu1FAgXQINCpLdVy8/HxpRTHbk7f3tov++gJBDOlfCASJCWE25If7H2xX\nF+7Hpgalz9TAcpJdpiE7KJnZ78v9N5OBMC2oTnleeOzTYyBujs8snI2n3RQWCG6y\na70=\n-----END CERTIFICATE-----"
        rc, caFingerprint = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("caFingerprintRootTeste2: " + str(caFingerprint))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Associating certificate with device
        """

        self.logger.info('associating certificate with device sensor...') #certificado interno
        self.logger.info('Fingerprint sensor: ' + fingerprint_sensor)
        device_id = Api.get_deviceid_by_label(jwt, "sensor")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_sensor, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        self.logger.info('associating certificate with device sensor4...') #certificado interno
        self.logger.info('Fingerprint sensor4: ' + fingerprint_sensor4)
        device_id = Api.get_deviceid_by_label(jwt, "sensor4")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_sensor4, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        self.logger.info('associating external certificate with device device2...') #certificado externo
        self.logger.info('Fingerprint device2: ' + fingerprint_device2)
        device_id = Api.get_deviceid_by_label(jwt, "device2")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_device2, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        self.logger.info('associating external certificate with device device4...') #certificado externo
        self.logger.info('Fingerprint device4: ' + fingerprint_device4)
        device_id = Api.get_deviceid_by_label(jwt, "device4")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_device4, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        """
        Remover certificado com dispositivo associado
        """

        self.logger.info('removing associated certificate... device2')
        self.logger.info('Fingerprint: ' + str(fingerprint_device2))
        rc, res = self.deleteCertificate(jwt, fingerprint_device2)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        """
        Remover a associação entre dispositivo e certificado
        """

        self.logger.info('disassociating device with certificate...')
        self.logger.info('Fingerprint: ' + fingerprint_device3)
        rc, res = self.associateCertificate(jwt, fingerprint_device3, None)
        self.logger.debug('Certificate disassociated: ' + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        self.logger.info('disassociating device with certificate...')
        self.logger.info('Fingerprint: ' + fingerprint_sensor)
        rc, res = self.associateCertificate(jwt, fingerprint_sensor, None)
        self.logger.debug('Certificate disassociated: ' + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        """
        Remover certificado sem dispositivo associado
        """

        self.logger.info('removing associated certificate...')
        self.logger.info('Fingerprint: ' + str(fingerprint_sensor))
        rc, res = self.deleteCertificate(jwt, fingerprint_sensor)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))


        """
        Associar dois certificados, assinados pela mesma CA, a um dispositivo
        """

        self.logger.info('associating external certificate with device "dispositivo"...') #certificado externo
        self.logger.info('Fingerprint device4: ' + fingerprint_device4)
        device_id = Api.get_deviceid_by_label(jwt, "dispositivo")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_device4, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        self.logger.info('associating external certificate with device "dispositivo"...') #certificado externo
        self.logger.info('Fingerprint device3: ' + fingerprint_device3)
        device_id = Api.get_deviceid_by_label(jwt, "dispositivo")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_device3, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))


        """
        Associar um certificado a dois dispositivos
        CN=dispositivo2, associar a dispositivo2: 6206c6, e também a dispositivo3: ced750
        """

        self.logger.info('associating external certificate to 2 devices ...') #certificado externo
        self.logger.info('Fingerprint device: ' + fingerprint_dispositivo2)
        device_id = Api.get_deviceid_by_label(jwt, "dispositivo2")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_dispositivo2, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        device_id = Api.get_deviceid_by_label(jwt, "dispositivo3")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_dispositivo2, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        """ 
        Associar dois certificados, assinados por CAs diferentes, a um dispositivo
        CN=device, assinado pela CA RootTeste2, e CN=device5, assinado pela CA RootTeste
        """

        self.logger.info('associating external certificates issued by different CAs, with device...') #certificado externo
        self.logger.info('Fingerprint device: ' + fingerprint_device)
        device_id = Api.get_deviceid_by_label(jwt, "device3")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_device, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))

        self.logger.info('associating external certificate with device "device3"...') #certificado externo
        self.logger.info('Fingerprint device3: ' + fingerprint_device5)
        device_id = Api.get_deviceid_by_label(jwt, "device3")
        self.logger.info('device_id: ' + device_id)
        rc, res = self.associateCertificate(jwt, fingerprint_device5, device_id)
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        rc, res = self.getCertificatesWithParameters(jwt, "fields=fingerprint,belongsTo")
        self.logger.info('result: ' + str(res))


        #TODO: Associar um certificado inválido a um dispositivo
        """
        Endpoint: v1/certificates/{fingerprint}
        status
        code: 400
        method: PATCH
        """


        #TODO: Associar um dispositivo inválido a um certificado
        """
        Endpoint: v1/certificates/{fingerprint}
        status
        code: 400
        method: PATCH
        """


        #TODO: Associar certificado com dispositivo – certificado com CNAME
        """
        Endpoint: v1/certificates
        status
        code: 201
        method: POST
        """


        #TODO: Associar certificado com dispositivo – certificado sem CNAME
        """
        Endpoint: v1/certificates
        status
        code: 201
        method: POST
        """

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
        Obter lista de CAs externas - parâmetros válidos
        """

        #GET < base - url > /v1/trusted-cas?offset = < number > & limit = < number > & fields = < list > & key1 = val1 & ... & keyn = valn

        self.logger.info('List Trusted CA Certificates with parameters: page=1...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "page=1")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: page=2...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "page=2")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: page=5...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "page=5")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """

        self.logger.info('List Trusted CA Certificates with parameters: offset=1...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=1")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: offset=2...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=2")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: offset=5...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=5")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        """

        self.logger.info('List Trusted CA Certificates with parameters: limit=1...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=1")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=3...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=3")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=30...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=30")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=250...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=250")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=251...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=251")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=2&offset=1...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=1")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=2&offset=2...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=2")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=2&offset=3...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=3")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: limit=2&offset=4...')
        rc, res = self.getTrustedCAsWithParameters(jwt, "limit=2&offset=4")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: fields=caFingerprint')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: caFingerprint=^05')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint&caFingerprint=^05")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: fields=caPem')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caPem")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: caPem=^MIIFWjCCA0KgA')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caPem&caPem=^MIIFWjCCA0KgA")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: caFingerprint, caPem')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint,caPem")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: createdAt')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=createdAt")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: createdAt')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=createdAt&createdAt=<=2021-12-25T00:00:00.000Z")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: modifiedAt')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=modifiedAt&modifiedAt=>=2021-05-25T00:00:00.000Z")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: caFingerprint,createdAt')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint,createdAt")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: allowAutoRegistration')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=allowAutoRegistration")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: allowAutoRegistration=false')
        rc, res = self.getTrustedCAsWithParameters(jwt, "allowAutoRegistration=false")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: allowAutoRegistration=true')
        rc, res = self.getTrustedCAsWithParameters(jwt, "allowAutoRegistration=true")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with parameters: caFingerprint,allowAutoRegistration')
        rc, res = self.getTrustedCAsWithParameters(jwt, "fields=caFingerprint,allowAutoRegistration")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('List Trusted CA Certificates with all parameters')
        rc, res = self.getTrustedCAsWithParameters(jwt, "offset=1&limit=2&fields=caFingerprint&caFingerprint=~:44")
        self.logger.debug('Trusted CA Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Listing associated certificates (belongsTo preenchido)
        """
        """
        self.logger.info('listing associated certificates...')
        rc, list = self.getAssociatedCertificates(jwt)
        self.logger.debug('Certificates List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        """

        """
        Lista certificados externos
        """

        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        self.logger.info('listing all certificates...')
        rc, list = self.getExternalCertificates(jwt, caFingerprint)
        self.logger.debug('Certificates List: ' + str(list))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        #GET < base - url > /v1/certificates?offset = < number > & limit = < number > & fields = < list > & key1 = val1 & ... & keyn = valn

        self.logger.info('listing certificates with parameter: offset=1...')
        rc, res = self.getCertificatesWithParameters(jwt, "offset=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: offset=2...')
        rc, res = self.getCertificatesWithParameters(jwt, "offset=2")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: offset=5...')
        rc, res = self.getCertificatesWithParameters(jwt, "offset=5")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=1...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=3...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=3")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=30...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=30")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=250...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=250")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=251...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=251")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=1...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&offset=1")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=2...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&offset=2")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=3...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&offset=3")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameter: limit=2&offset=4...')
        rc, res = self.getCertificatesWithParameters(jwt, "limit=2&offset=4")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: fields=caFingerprint')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=caFingerprint")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('listing certificates with parameters: caFingerprint=^05')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=caFingerprint&caFingerprint=^05")
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

        self.logger.info('listing certificates with parameters: caFingerprint, pem')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=caFingerprint,pem")
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

        self.logger.info('listing certificates with parameters: caFingerprint,createdAt')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=caFingerprint,createdAt")
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

        self.logger.info('listing certificates with parameters: caFingerprint,autoRegistered')
        rc, res = self.getCertificatesWithParameters(jwt, "fields=caFingerprint,autoRegistered")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        self.logger.info('listing certificates with all parameters')
        rc, res = self.getCertificatesWithParameters(jwt, "offset=1&limit=2&fields=caFingerprint&caFingerprint=~:44")
        self.logger.debug('Certificates: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Obter CA externa
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA...')
        rc, res = self.getTrustedCA(jwt, caFingerprint)
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Obter CA externa - com filtros
        """

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA with parameters: fields=caFingerprint...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=caFingerprint")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA with parameters: fields=caPem...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=caPem")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA with parameters: fields=allowAutoRegistration...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=allowAutoRegistration")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA with parameters: fields=subjectDN...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=subjectDN")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        
        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA with parameters: fields=validity...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=validity")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        
        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA with parameters: fields=createdAt...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=createdAt")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
        
        self.logger.info('caFingerprint: ' + caFingerprint)
        self.logger.info('listing specific CA with parameters: fields=modifiedAt...')
        rc, res = self.getTrustedCAWithParameters(jwt, caFingerprint, "fields=modifiedAt")
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        #TODO: Obter lista de CA externa - invalid request


        self.logger.debug('List Trusted CA Certificates: invalid request: TODO ')
        """
        rc, res = self.getTrustedCAs(jwt)
        self.logger.info("trusted-cas: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        """

        """
        Obter lista de CA externa - JWT vazio
        """

        self.logger.debug('List Trusted CA Certificates: empty JWT ... ')
        rc, res = self.getTrustedCAs("")
        self.logger.info("trusted-cas: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Obter lista de CA externa - JWT inválido
        """

        self.logger.debug('List Trusted CA Certificates: invalid JWT ... ')
        rc, res = self.getTrustedCAs("abcde")
        self.logger.info("trusted-cas: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")


        #TODO: Obter lista de CA externa - operação não autorizada


        """
        Obter CA externa - CA não existe
        """

        caFingerprint = "93:5F:29:55:6C:A1:08:67:C7:A5:54:CC:3B:05:FF:4B:4C:42:11:D5:6F:48:76:98:69:34:2D:93:6D:9D:74:5A"
        self.logger.info('listing specific CA: CA does not exist...')
        rc, res = self.getTrustedCA(jwt, caFingerprint)
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        """
        Registro de CA externa com certificado expirado
        """
        self.logger.debug('registering trusted CA - expired certificate ... USAR UM CERTIFICADO EXPIRADO')
        caPem = "-----BEGIN CERTIFICATE-----\nMIICNTCCAZigAwIBAgIUGis7n29EcOsEoCxCm980onT5sR4wCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMDA5MzAxMzI2MDRaFw0yNTA5MjkxMzI2MDRaMC0xKzApBgNVBAMMIlJvb3Qg\nQ0EgZHVtbXkgKGRvam90IElvVCBQbGF0Zm9ybSkwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAFTleScH0EakSco7iPtMN76N3h9PvR7l1UDzYLiDkgYch3W4FwGUDCS\n9yBtaKEiMEv8hGHMHzf0Jsy03hse6DjSagCYWpMqXlYSUZ5muKD7IPC4l+T9KLbB\nmWptY8NQTMiFPZDs2OcLPaaGKJwN42EKBjEyC9dS+WaBFRYFajDvg9rUrKNTMFEw\nHQYDVR0OBBYEFNEcTxzYBiTx3QvnLxnsdHdJySJ2MB8GA1UdIwQYMBaAFNEcTxzY\nBiTx3QvnLxnsdHdJySJ2MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDgYoA\nMIGGAkFhyI5TpL5voJWQPhjo1AqKzwGcwA3KcSv+Gmz8dbIBt5G+tDmZi213x8CB\nlxNWsrb3Q7+M1emWwrPc/bfXcSHZZwJBZMX4XC6wJTRHkrjNV28evQb+mYbpJl8M\nuK6pmr2SWatOSndPkhgOY5VPGEsnrVpT0OGrUkoe9khvdaDX2yFlAXY=\n-----END CERTIFICATE----"
        rc, res = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registro de CA externa - certificado não é CA root
        """
        self.logger.debug('registering trusted CA - is not root CA certificate')
        caPem = "-----BEGIN CERTIFICATE-----\nMIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\nSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\nGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\nq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\nSMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\nZ8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\na6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\nAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\nCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\nbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\nc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\nVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\nARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\nMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\nY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\nAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\nuM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\nwApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\nX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\nPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\nKOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n-----END CERTIFICATE-----"
        rc, res = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registro de CA externa, certificado não é uma CA
        """
        self.logger.debug('registering trusted CA ...certificate is not a CA')
        caPem = "-----BEGIN CERTIFICATE-----\nMIIFWjCCA0KgAwIBAgIUY70TLLWslpbCM3L/MnZCP/VaBLMwDQYJKoZIhvcNAQEL\nBQAwejEjMCEGCgmSJomT8ixkAQEME2MtMDU5ZmEzNjQ3ZDA4YjhkYWUxGTAXBgNV\nBAMMEFg1MDkgSWRlbnRpdHkgQ0ExGzAZBgNVBAsMEkNlcnRpZmljYXRlIElzc3Vl\ncjEbMBkGA1UECgwSZG9qb3QgSW9UIFBsYXRmb3JtMB4XDTIxMDQxNjIwMjkwMFoX\nDTIxMDQxNzIwMjkwMFowNDEbMBkGA1UECgwSZG9qb3QgSW9UIFBsYXRmb3JtMRUw\nEwYDVQQDDAxhZG1pbjphZTg1MzMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\nAoIBAQCa7GF/FT8ONsOn1X0D3O3F5rNlpwU9QcuTc9icUmo/2VQe/5D5BVDErgZK\nBDrE2/60QtE36jVk85UYKaE71hbWJPQGE1Ol0Xb22qSDhFXEduWBxquqMyj/Wwi9\n6h2HZ1DiYx4H2XIqi3QVEtFgS9RkVvbwOdxCJrW7egMC4WuQfYWEyMVQAuAoTnHt\nVsKlEarSbHCJlWYufsyiNv/cySHXeSqmryo9+w+PpdPmTWcaumTqOUWSWF2iyHes\nuyIWsEyeaxs6XOfJ9S4TsVgfzYMs6/gvp1hihn+kyk5vks4wPnL0zdcgtytd5gjH\nrQZfyieWLhDNutLwje/JgHMWoxlbAgMBAAGjggEcMIIBGDAMBgNVHRMBAf8EAjAA\nMB8GA1UdIwQYMBaAFM+7R2Tb+BALpFixz4iuqAIH8PKzMCcGA1UdJQQgMB4GCCsG\nAQUFBwMCBggrBgEFBQcDBAYIKwYBBQUHAwEwgY4GA1UdHwSBhjCBgzCBgKJ+pHww\nejEjMCEGCgmSJomT8ixkAQEME2MtMDU5ZmEzNjQ3ZDA4YjhkYWUxGTAXBgNVBAMM\nEFg1MDkgSWRlbnRpdHkgQ0ExGzAZBgNVBAsMEkNlcnRpZmljYXRlIElzc3VlcjEb\nMBkGA1UECgwSZG9qb3QgSW9UIFBsYXRmb3JtMB0GA1UdDgQWBBSrsnjUp/t5bPTo\nn9pRnNxhOIirVDAOBgNVHQ8BAf8EBAMCA+gwDQYJKoZIhvcNAQELBQADggIBAIGI\nFYmZkKKs9nDoIL4z255FnPVTbTgr/Ey630UzCTqWGkn89tnVDWj7F4DKgKZKVrgR\nfUZZDP3RzFWkdWqGblqBawfF4UDakb7yZU98/TFghOV26Pt1G2X8p0va7jIe2VT0\n4kV43YXMgrF+cdMe80rzjsi0wvdrG7bWMg4WofgesBpCQshqjGPhdIQBZOeQ89US\nGTDN9nfIDZw5dvF6sQzsNuLW1Gi296VNjp+0p3fGaRAmZz2BcCk1qWHda7f2AiKz\nwhinYcK84fnw96c1fWUjVpBtCtle7qr1TcBEgwUvN/NtxgKCLI/X6LDOLqrIQXyE\nQHrhN1ahL9gtXpP//ikXQZ93hcWqqGMHdUqSF6uujBzfWvhNUxqbWMut8MDqbRcp\nfHPnCoubIXS8eWSbAgctU5UhiwsIVzjUM2kHK+kxAcbi5HLh3r8pGeE03oKwmprD\nNIYZkQ6wb37C2cLq90hgkecaPmFhQjWreG/2OgaGv1vObB/vGZFXr5ljmacDZ3v+\nt++K3TxB2OsSDi04ubcc4Yjr4GgZv9Xo2zAKwc6VH+WqcsYS8pqdGnCLafOB9eWf\n7yGfZ82IlOKHc8pReP3N6TfWDmpy3HRZmTrQpCx7MA0C1lPrN6Qqg58y2JHdD/p2\nL1BVKzZoabBT8oGYHxoy06wJnq6e0EgL1sDokFzs\n-----END CERTIFICATE-----"
        rc, res = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registro de CA externa - certificado com mesmo CName da CA da dojot
        """
        self.logger.debug('registering trusted CA - CName of trusted CA is the same as the platform')
        caPem = "-----BEGIN CERTIFICATE-----\nMIIF6jCCA9KgAwIBAgIUBVdadTYpaBGs3NK+B+Akv8BxDlwwDQYJKoZIhvcNAQEL\nBQAwejEjMCEGCgmSJomT8ixkAQEME2MtMDU5ZmEzNjQ3ZDA4YjhkYWUxGTAXBgNV\nBAMMEFg1MDkgSWRlbnRpdHkgQ0ExGzAZBgNVBAsMEkNlcnRpZmljYXRlIElzc3Vl\ncjEbMBkGA1UECgwSZG9qb3QgSW9UIFBsYXRmb3JtMCAXDTIxMDQxNTE4MDkyOVoY\nDzIwNTEwNDA4MTgwOTI5WjB6MSMwIQYKCZImiZPyLGQBAQwTYy0wNTlmYTM2NDdk\nMDhiOGRhZTEZMBcGA1UEAwwQWDUwOSBJZGVudGl0eSBDQTEbMBkGA1UECwwSQ2Vy\ndGlmaWNhdGUgSXNzdWVyMRswGQYDVQQKDBJkb2pvdCBJb1QgUGxhdGZvcm0wggIi\nMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQCwRQT10khfCUhtKel7Vzx0Q/E/\n4C9a8H90wJzLfjFs6gMocl8BVGP9Mrf3i+NYYNEyJJpRYGxuyO/1wv9feOQxl5CT\nZie6BVKu2yA59MrcVfbn+yuUBNk3Q7MmsEpjmcuuth2tvc7NTmCeaG8UbXvN55mT\nn2R/NFhxwyyE0h2RstHpT2GDSAlJu3HrNuTGsIBMCBA5ffIR0a+aGDy+2qDkHSWy\nWuo58+KuIsl64JamrtW1i2o5BIsxvsMqMvY1EfI0CLdSBinvVcChdd3JnISdIGu7\n/xPBfdVDWm4d+sd3rO5Td3V0Nts6sbBmkWUwxLKGntcXG57SKy88UV0JRUjhxu0H\nj/fGHLvzscJwvjvjB0K6KaXnKd2rc+k/OsdbwBoupXOHX3u/6FyOSA+2JI9XGBBV\nAqhyTnehbrkfK4Ie35YRHOK2cwxhdQCY3cIhKfwXT9WNVReDrwjRot1uhLraDjBb\nV9FJg/1A3Vgh7mZpm4KJtY5bNx/pG654cuRcz5wLFtlp6iZfD8Zu/aZzxvhYVgZW\nEYaefJVdZLcy7OdsFT/0xrJJ61yWtZ8rU0U3PK+gzfwHL1AfzKnWLULI4w5Q/6ML\nKsA9ade/9UHHan5dLZlhAY7hdopx0y9t7iqx4yA/DMOfv6c1teQo5s9zgcO4e9Qh\ngypOV5mqVWgbkDM1CwIDAQABo2YwZDASBgNVHRMBAf8ECDAGAQH/AgEAMB8GA1Ud\nIwQYMBaAFM+7R2Tb+BALpFixz4iuqAIH8PKzMB0GA1UdDgQWBBTPu0dk2/gQC6RY\nsc+IrqgCB/DyszAOBgNVHQ8BAf8EBAMCAYYwDQYJKoZIhvcNAQELBQADggIBAKSR\nDqtbU/douJHwuafQFYwbJIKO2m40AG+M0ZpRuhZTqDXKJ0VAe61xStXxs8gNaXqo\nVwLebLIUXo47HtgzJV9xDFZ4F+sc4AYjjST+MPTKVNtHhdggfIwEuj/R13wKVYDa\nAuJzF0+o8fpgFJ5qCr1Elv5dLg/7pkhFXIwupewz/DSwjbEkPxAmMb1GarZx1BWp\nqHPPwRPQTo4jkns50zF47DsKAfP2RvSUFacG8XDv8jks+KsWTsdlt5oaCFgeBWED\nRdYGnHAQmtmKJwPtUeQC/H/WW9Sps7tPp7nz7f/6GL75uzvRpipDkJ2znO7MC7GE\nR0VFdXGsWz33riW80ttxlipbslKzpwjVIC0+hAZvOMbu86E+me/L5HA8KEk2IZ4Z\ncKrmU3MdxTQe55HvTMF5dHxP1xrRkzPKc4EB46c+NgljnJKQNVPj38v5otvcVpTc\nSJDyi00RWSLPGL3Ofd2d32WSUiYKQ9snZ1yHjUCYIVqNgtvmlBSYN8RW8ErJcut2\n9GlR/hElvgbliQ8JJ71jwXdxAlvdEOk/tALuzt9wW7cRoyaSBqV4v3mZ/dawrh/J\nyEqZc+EUhuRR/DunSqcrOvVAa+I/u5r6mV0IcAbj4KFz6TVpXAezEkC2fSlEm0mr\nqY9DYbf9dFNhSfYb2jmiZXiC/L94H9hm5yrMp+Bd\n-----END CERTIFICATE-----"
        rc, res = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registro de CA externa com certificado vazio
        """

        self.logger.debug('registering trusted CA ... empty pem')
        caPem = ""
        rc, res = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registro de CA externa, certificado já existe
        """
        self.logger.debug('registering trusted CA ... certificate already exists')
        caPem = "-----BEGIN CERTIFICATE-----\nMIICDTCCAW6gAwIBAgIUZAYqWqoeYfWqF5oXaGU0IeWfxuEwCgYIKoZIzj0EAwIw\nGDEWMBQGA1UEAwwNUm9vdCBDQSBUZXN0ZTAeFw0yMTA2MTcxMzA2MzBaFw0yNjA2\nMTYxMzA2MzBaMBgxFjAUBgNVBAMMDVJvb3QgQ0EgVGVzdGUwgZswEAYHKoZIzj0C\nAQYFK4EEACMDgYYABACJ5AcvLttv/pB5EjitNcKMCgyF+IYyDoPYLilanvpd26qi\nVSWlU2fnUikgzHuWUPAoVI0SI+MlluMxsycTzFcCQgHFgWQO5OV4QvYQZfcMNn+q\n3Sy7gCn2WkSqQIxBSLh3YvMyBGnL0wUFzLwb1sKk9pKAE6+J62WK2tswAkVdxdV6\nwqNTMFEwHQYDVR0OBBYEFLHxc59Y0GqKz0I1QRRsfTi4BwUKMB8GA1UdIwQYMBaA\nFLHxc59Y0GqKz0I1QRRsfTi4BwUKMA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0E\nAwIDgYwAMIGIAkIA71h70oucxkSQPhnqIVTInMFQf1a+Acp0l7UQpgeVezj4gGso\noLRVX5kWE+W0mALmF/vYCj+l2OctLe3PS95LBroCQgCoqCexRvdGEyToOnLyKdzn\n+eBrJbanwL9mtY9v0Rvt2XKEFynVQiQQ2/qdB7EnkJDeE/JwRArlCYHNZCFOk0gD\nHA==\n-----END CERTIFICATE-----"
        rc, res = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("message: " + str(rc) + ',  ' + str(res))
        self.assertTrue(int(rc) == 409, "codigo inesperado") #erro esperdo: 400


        #TODO: Registro de CA externa, excedeu o nº de CAs registradas

        self.logger.debug('registering trusted CA ...number of registered CAs has been exceeded - TODO')
        """
        caPem = "-----BEGIN CERTIFICATE-----\nMIICNTCCAZigAwIBAgIUGis7n29EcOsEoCxCm980onT5sR4wCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMDA5MzAxMzI2MDRaFw0yNTA5MjkxMzI2MDRaMC0xKzApBgNVBAMMIlJvb3Qg\nQ0EgZHVtbXkgKGRvam90IElvVCBQbGF0Zm9ybSkwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAFTleScH0EakSco7iPtMN76N3h9PvR7l1UDzYLiDkgYch3W4FwGUDCS\n9yBtaKEiMEv8hGHMHzf0Jsy03hse6DjSagCYWpMqXlYSUZ5muKD7IPC4l+T9KLbB\nmWptY8NQTMiFPZDs2OcLPaaGKJwN42EKBjEyC9dS+WaBFRYFajDvg9rUrKNTMFEw\nHQYDVR0OBBYEFNEcTxzYBiTx3QvnLxnsdHdJySJ2MB8GA1UdIwQYMBaAFNEcTxzY\nBiTx3QvnLxnsdHdJySJ2MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDgYoA\nMIGGAkFhyI5TpL5voJWQPhjo1AqKzwGcwA3KcSv+Gmz8dbIBt5G+tDmZi213x8CB\nlxNWsrb3Q7+M1emWwrPc/bfXcSHZZwJBZMX4XC6wJTRHkrjNV28evQb+mYbpJl8M\nuK6pmr2SWatOSndPkhgOY5VPGEsnrVpT0OGrUkoe9khvdaDX2yFlAXY=\n-----END CERTIFICATE----"
        rc, res = self.registerTrustedCA(jwt, caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        """

        """
        Registro de CA externa – invalid request
        """
        self.logger.debug('registering trusted CA ...Invalid request.')
        caPem = "-----BEGIN CERTIFICATE-----\nMIICNTCCAZigAwIBAgIUGis7n29EcOsEoCxCm980onT5sR4wCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMDA5MzAxMzI2MDRaFw0yNTA5MjkxMzI2MDRaMC0xKzApBgNVBAMMIlJvb3Qg\nQ0EgZHVtbXkgKGRvam90IElvVCBQbGF0Zm9ybSkwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAFTleScH0EakSco7iPtMN76N3h9PvR7l1UDzYLiDkgYch3W4FwGUDCS\n9yBtaKEiMEv8hGHMHzf0Jsy03hse6DjSagCYWpMqXlYSUZ5muKD7IPC4l+T9KLbB\nmWptY8NQTMiFPZDs2OcLPaaGKJwN42EKBjEyC9dS+WaBFRYFajDvg9rUrKNTMFEw\nHQYDVR0OBBYEFNEcTxzYBiTx3QvnLxnsdHdJySJ2MB8GA1UdIwQYMBaAFNEcTxzY\nBiTx3QvnLxnsdHdJySJ2MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDgYoA\nMIGGAkFhyI5TpL5voJWQPhjo1AqKzwGcwA3KcSv+Gmz8dbIBt5G+tDmZi213x8CB\nlxNWsrb3Q7+M1emWwrPc/bfXcSHZZwJBZMX4XC6wJTRHkrjNV28evQb+mYbpJl8M\nuK6pmr2SWatOSndPkhgOY5VPGEsnrVpT0OGrUkoe9khvdaDX2yFlAXY=\n-----END CERTIFICATE----"
        rc, res = self.registerTrustedCA(jwt, caPem, 'falso')
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registro de CA externa – campo allowAutoRegistration vazio
        """
        self.logger.debug('registering trusted CA ...empty allowAutoRegistration.')
        caPem = "-----BEGIN CERTIFICATE-----\nMIICNTCCAZigAwIBAgIUGis7n29EcOsEoCxCm980onT5sR4wCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMDA5MzAxMzI2MDRaFw0yNTA5MjkxMzI2MDRaMC0xKzApBgNVBAMMIlJvb3Qg\nQ0EgZHVtbXkgKGRvam90IElvVCBQbGF0Zm9ybSkwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAFTleScH0EakSco7iPtMN76N3h9PvR7l1UDzYLiDkgYch3W4FwGUDCS\n9yBtaKEiMEv8hGHMHzf0Jsy03hse6DjSagCYWpMqXlYSUZ5muKD7IPC4l+T9KLbB\nmWptY8NQTMiFPZDs2OcLPaaGKJwN42EKBjEyC9dS+WaBFRYFajDvg9rUrKNTMFEw\nHQYDVR0OBBYEFNEcTxzYBiTx3QvnLxnsdHdJySJ2MB8GA1UdIwQYMBaAFNEcTxzY\nBiTx3QvnLxnsdHdJySJ2MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDgYoA\nMIGGAkFhyI5TpL5voJWQPhjo1AqKzwGcwA3KcSv+Gmz8dbIBt5G+tDmZi213x8CB\nlxNWsrb3Q7+M1emWwrPc/bfXcSHZZwJBZMX4XC6wJTRHkrjNV28evQb+mYbpJl8M\nuK6pmr2SWatOSndPkhgOY5VPGEsnrVpT0OGrUkoe9khvdaDX2yFlAXY=\n-----END CERTIFICATE----"
        rc, res = self.registerTrustedCA(jwt, caPem, '')
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Registro de CA externa – JWT vazio
        """
        self.logger.debug('registering trusted CA ...empty JWT.')
        caPem = "-----BEGIN CERTIFICATE-----\nMIICNTCCAZigAwIBAgIUGis7n29EcOsEoCxCm980onT5sR4wCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMDA5MzAxMzI2MDRaFw0yNTA5MjkxMzI2MDRaMC0xKzApBgNVBAMMIlJvb3Qg\nQ0EgZHVtbXkgKGRvam90IElvVCBQbGF0Zm9ybSkwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAFTleScH0EakSco7iPtMN76N3h9PvR7l1UDzYLiDkgYch3W4FwGUDCS\n9yBtaKEiMEv8hGHMHzf0Jsy03hse6DjSagCYWpMqXlYSUZ5muKD7IPC4l+T9KLbB\nmWptY8NQTMiFPZDs2OcLPaaGKJwN42EKBjEyC9dS+WaBFRYFajDvg9rUrKNTMFEw\nHQYDVR0OBBYEFNEcTxzYBiTx3QvnLxnsdHdJySJ2MB8GA1UdIwQYMBaAFNEcTxzY\nBiTx3QvnLxnsdHdJySJ2MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDgYoA\nMIGGAkFhyI5TpL5voJWQPhjo1AqKzwGcwA3KcSv+Gmz8dbIBt5G+tDmZi213x8CB\nlxNWsrb3Q7+M1emWwrPc/bfXcSHZZwJBZMX4XC6wJTRHkrjNV28evQb+mYbpJl8M\nuK6pmr2SWatOSndPkhgOY5VPGEsnrVpT0OGrUkoe9khvdaDX2yFlAXY=\n-----END CERTIFICATE----"
        rc, res = self.registerTrustedCA("", caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Registro de CA externa – JWT invalido
        """
        self.logger.debug('registering trusted CA ...invalid JWT.')
        caPem = "-----BEGIN CERTIFICATE-----\nMIICNTCCAZigAwIBAgIUGis7n29EcOsEoCxCm980onT5sR4wCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMDA5MzAxMzI2MDRaFw0yNTA5MjkxMzI2MDRaMC0xKzApBgNVBAMMIlJvb3Qg\nQ0EgZHVtbXkgKGRvam90IElvVCBQbGF0Zm9ybSkwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAFTleScH0EakSco7iPtMN76N3h9PvR7l1UDzYLiDkgYch3W4FwGUDCS\n9yBtaKEiMEv8hGHMHzf0Jsy03hse6DjSagCYWpMqXlYSUZ5muKD7IPC4l+T9KLbB\nmWptY8NQTMiFPZDs2OcLPaaGKJwN42EKBjEyC9dS+WaBFRYFajDvg9rUrKNTMFEw\nHQYDVR0OBBYEFNEcTxzYBiTx3QvnLxnsdHdJySJ2MB8GA1UdIwQYMBaAFNEcTxzY\nBiTx3QvnLxnsdHdJySJ2MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDgYoA\nMIGGAkFhyI5TpL5voJWQPhjo1AqKzwGcwA3KcSv+Gmz8dbIBt5G+tDmZi213x8CB\nlxNWsrb3Q7+M1emWwrPc/bfXcSHZZwJBZMX4XC6wJTRHkrjNV28evQb+mYbpJl8M\nuK6pmr2SWatOSndPkhgOY5VPGEsnrVpT0OGrUkoe9khvdaDX2yFlAXY=\n-----END CERTIFICATE----"
        rc, res = self.registerTrustedCA("abcde", caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Registro de CA externa – operação não autorizada
        """
        """
        self.logger.debug('registering trusted CA- not authorized operation...')
        caPem = "-----BEGIN CERTIFICATE-----\nMIICNTCCAZigAwIBAgIUGis7n29EcOsEoCxCm980onT5sR4wCgYIKoZIzj0EAwIw\nLTErMCkGA1UEAwwiUm9vdCBDQSBkdW1teSAoZG9qb3QgSW9UIFBsYXRmb3JtKTAe\nFw0yMDA5MzAxMzI2MDRaFw0yNTA5MjkxMzI2MDRaMC0xKzApBgNVBAMMIlJvb3Qg\nQ0EgZHVtbXkgKGRvam90IElvVCBQbGF0Zm9ybSkwgZswEAYHKoZIzj0CAQYFK4EE\nACMDgYYABAFTleScH0EakSco7iPtMN76N3h9PvR7l1UDzYLiDkgYch3W4FwGUDCS\n9yBtaKEiMEv8hGHMHzf0Jsy03hse6DjSagCYWpMqXlYSUZ5muKD7IPC4l+T9KLbB\nmWptY8NQTMiFPZDs2OcLPaaGKJwN42EKBjEyC9dS+WaBFRYFajDvg9rUrKNTMFEw\nHQYDVR0OBBYEFNEcTxzYBiTx3QvnLxnsdHdJySJ2MB8GA1UdIwQYMBaAFNEcTxzY\nBiTx3QvnLxnsdHdJySJ2MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDgYoA\nMIGGAkFhyI5TpL5voJWQPhjo1AqKzwGcwA3KcSv+Gmz8dbIBt5G+tDmZi213x8CB\nlxNWsrb3Q7+M1emWwrPc/bfXcSHZZwJBZMX4XC6wJTRHkrjNV28evQb+mYbpJl8M\nuK6pmr2SWatOSndPkhgOY5VPGEsnrVpT0OGrUkoe9khvdaDX2yFlAXY=\n-----END CERTIFICATE----"
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPTnFqWFJURWpGRklHT0ZoYWZMYmpxcGNTRGhJQjFUTCIsImlhdCI6MTYyMzA3NzY1MiwiZXhwIjoxNjIzMDc4MDcyLCJwcm9maWxlIjoiYWRtaW4iLCJncm91cHMiOlsxXSwidXNlcmlkIjoyLCJqdGkiOiI4Y2M5YzRhZTcwNTMzODRiMjIzMTNhNmVjZTU4NGUyMSIsInNlcnZpY2UiOiJhZG1pbiIsInVzZXJuYW1lIjoiYmV0ZSJ9.y-xm7lCjLxRa5MgO9Gm9FtOcvTO0_gn20CRKbkUSfCo"
        rc, res = self.registerTrustedCA(token, caPem, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 403, "codigo inesperado")
        """

        """
        Remoção de uma CA externa
        """

        #caFingerprint da CA DST Root
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        self.logger.debug('removing trusted CA - DST Root...')
        rc, res = self.deleteTrustedCA(jwt, caFingerprint)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")


        """
        Remoção de uma CA externa - existe certificado assinado pela CA (There are certificates dependent on the CA to be removed)
        """

        #caFingerprint da CA (Root CA Teste)
        caFingerprint = "4F:64:DE:09:24:AB:EC:C3:F0:96:41:E2:94:98:45:97:19:B0:26:EF:02:16:7A:44:DA:0F:C6:05:BE:BC:86:EA"
        self.logger.debug('removing trusted CA with certificate issued by CA ...')
        rc, res = self.deleteTrustedCA(jwt, caFingerprint)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


        #TODO: Remoção de uma CA externa - invalid request

        self.logger.debug('removing trusted CA - invalid request ... - TODO')
        """
        caFingerprint = ""
        rc, res = Api.delete_trusted_ca(jwt, caFingerprint)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")
        """

        """
        Remoção de uma CA externa - JWT vazio
        """
        #caFingerprint da CA DST Root
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        self.logger.debug('removing trusted CA - empty JWT ...')
        rc, res = Api.delete_trusted_ca("", caFingerprint)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Remoção de uma CA externa - JWT inválido
        """

        # caFingerprint da CA RootTeste3
        caFingerprint = "BE:59:03:12:AD:A8:06:5F:FF:48:2A:70:12:C0:50:99:53:41:1B:7D:D3:6C:DF:C2:11:23:2A:B7:F3:07:DF:58"
        self.logger.debug('removing trusted CA - invalid JWT ...')
        rc, res = Api.delete_trusted_ca("abcde", caFingerprint)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Remoção de uma CA externa - operação não autorizada
        """
        """
        # caFingerprint da DST Root CA
        caFingerprint = "06:87:26:03:31:A7:24:03:D9:09:F1:05:E6:9B:CF:0D:32:E1:BD:24:93:FF:C6:D9:20:6D:11:BC:D6:77:07:39"
        self.logger.debug('removing trusted CA - not authorized operation ...')
        rc, res = Api.delete_trusted_ca(jwt, caFingerprint)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 403, "codigo inesperado")
        """

        """
        Remoção de uma CA externa - CA não existe (RootTeste3)
        """
        caFingerprint="BE:59:03:12:AD:A8:06:5F:FF:48:2A:70:12:C0:50:99:53:41:1B:7D:D3:6C:DF:C2:11:23:2A:B7:F3:07:DF:58"
        self.logger.debug('removing trusted CA - CA does not exist ...')
        rc, res = Api.delete_trusted_ca(jwt, caFingerprint)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        """
        Atualizar CA externa - alterar o parâmetro allowAutoRegistration
        """

        # caFingerprint da CA Root Teste2
        caFingerprint = "53:1A:AB:F1:86:F4:BF:B9:44:F7:4A:98:46:BB:05:A7:31:D0:1D:E0:43:51:EF:33:DA:53:FE:46:0B:02:01:48"
        self.logger.debug('updating trusted CA - allowAutoRegistration = true...')
        rc, res = Api.update_trusted_ca(jwt, caFingerprint, True)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        self.logger.info('listing specific CA...')
        rc, res = self.getTrustedCA(jwt, caFingerprint)
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        self.logger.debug('updating trusted CA - allowAutoRegistration = false...')
        rc, res = Api.update_trusted_ca(jwt, caFingerprint, False)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 204, "codigo inesperado")
        self.logger.info('listing specific CA...')
        rc, res = self.getTrustedCA(jwt, caFingerprint)
        self.logger.debug('Certificate info: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Atualizar CA externa - parâmetro allowAutoRegistration vazio
        """

        self.logger.debug('updating trusted CA - empty allowAutoRegistration ...')
        rc, res = Api.update_trusted_ca(jwt, caFingerprint, "")
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Atualizar CA externa - invalid request
        """

        self.logger.debug('updating trusted CA - invalid request...')
        rc, res = Api.update_trusted_ca(jwt, caFingerprint, 0)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        """
        Atualizar CA externa - JWT vazio
        """

        self.logger.debug('updating trusted CA - empty JWT...')
        rc, res = Api.update_trusted_ca("", caFingerprint, True)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")


        """
        Atualizar CA externa - JWT inválido
        """

        self.logger.debug('updating trusted CA - invalid JWT...')
        rc, res = Api.update_trusted_ca("abcde", caFingerprint, True)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 401, "codigo inesperado")

        """
        Atualizar CA externa - operação não autorizada
        """
        """
        self.logger.debug('updating trusted CA - not authorized operation...')
        rc, res = Api.update_trusted_ca(token, caFingerprint, True)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 403, "codigo inesperado")
        """

        """
        Atualizar CA externa - CA não existe
        """

        caFingerprint = "B7:B0:58:78:6C:BD:6D:FF:D2:FC:99:0D:C3:45:4B:A9:26:F0:BB:97:A0:EB:28:26:84:86:48:8C:EB:74:0E:FF"
        self.logger.debug('updating trusted CA - CA does not exist...')
        rc, res = Api.update_trusted_ca(jwt, caFingerprint, True)
        self.logger.info("message: " + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

        """
        Remover um dispositivo sem certificado associado
        """

        device_id = Api.get_deviceid_by_label(jwt, 'sensor3')
        self.logger.info('device_id: ' + str(device_id))
        rc, res = Api.delete_device(jwt, device_id)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        """
        Remover um dispositivo com certificado associado
        """

        device_id = Api.get_deviceid_by_label(jwt, 'device4')
        rc, res = Api.delete_device(jwt, device_id)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        self.logger.info('removing all certificates')
        rc, res = self.deleteCertificates(jwt)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "codigo inesperado")

