from common.base_test import BaseTest
from dojot.api import DojotAPI as Api
import json
from common.testutils import *
from dojotTester import ROOT_DIR


class GetCredentialsWithoutBody(BaseTest): 
    """
    Get credentials without body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...default values')
        rc, res = Api.get_credentials_without_body(self.jwt, "application/json")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsPermissionReadOnly(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...permission read-only')

        data = {
            "permission": "read-only",
            "pathPrefixMatch": "*",
            "expiration": 900
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsPermissionWriteOnly(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...permission write-only')

        data = {
            "permission": "write-only",
            "pathPrefixMatch": "/devices/*",
            "expiration": 1800
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsPermissionReadWrite(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...permission read-write')
 
        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")



class GetCredentialsInvalidPermission(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid permission')

        data = {
            "permission": "all",
            "pathPrefixMatch": "*",
            "expiration": 300
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class GetCredentialsEmptyPermission(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...empty permission')

        data = {
            "permission": "",
            "pathPrefixMatch": "*",
            "expiration": 300
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class GetCredentialsDefaultPath(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...default pathPrefixMatch')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsValidPath(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...valid pathPrefixMatch')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/devices/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

class GetCredentialsPathSizeZero(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch size zero')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class GetCredentialsPathDefaultMaximumSize(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch default maximum size (100)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefg/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

class GetCredentialsPathMaximumSize(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch maximum size (25)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/abcdefghi1abcdefghi2ab/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsPathSizeGreaterMaximum(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch maximum size (30)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/abcdefghi1abcdefghi2abcdefg/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

#AQUI
class GetCredentialsInvalidPath(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid pathPrefixMatch')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "-",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class GetCredentialsDefaultExpirationValue(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...default expiration value')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 900
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")



class GetCredentialsValidExpirationValue(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...valid expiration value')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 3600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

class GetCredentialsMaximumExpirationValue(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...maximum expiration value')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 31536000
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsExpirationValueLessMinimum(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration (899)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 899
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class GetCredentialsExpirationValueGreaterMaximum(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration (31536001)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 31536001
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class GetCredentialsExpirationValueText(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration value (text)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": "texto"
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class GetCredentialsExpirationValueZero(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration (zero)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 0
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class GetCredentialsUnsupportedMediaType(BaseTest): 
    """
    Request credentials with unsupported media type.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...unsupported media type (octet-stream)')
        rc, res = Api.get_credentials_without_body(self.jwt, "application/octet-stream")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 415, "codigo inesperado")

        self.logger.info('Executing test...unsupported media type (multipart/form-data)')
        rc, res = Api.get_credentials_without_body(self.jwt, "multipart/form-data")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 415, "codigo inesperado")

class GetCredentialsInvalidSchema(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid schema')

        data = {
            "permission": "read-write"
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

        data = {
           "pathPrefixMatch": "*"
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


        data = {
            "expiration": 300
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class UploadFile(BaseTest):

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):

        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class ListStoredFiles(BaseTest):
    """
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        file = ROOT_DIR + "/" + "resources/files/lana.jpg"

        self.logger.info('file: ' + str(file))

        self.path = "imagens/lana.jpg"

        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        self.logger.info('Setup executed!')


    def runTest(self):
        self.logger.info('Executing test...listing stored files')

        rc, res = Api.list_stored_files(self.jwt, 10)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")



    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()


class RemoveStoredFile(BaseTest):
    """
    """
    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Setup executed!')

        file = ROOT_DIR + "/" + "resources/files/teste.mp4"

        self.logger.info('file: ' + str(file))

        self.path = "videos/teste.mp4"

        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...removing stored file')

        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

class DownloadTextFile(BaseTest):
    """
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(file))

        self.path = "arquivos/arquivo.txt"
        self.filename = "arquivo.txt"

        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):

#        rc, res = Api.download_file(self.jwt, self.filename, self.path)
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class DownloadImageFile(BaseTest):
    """
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        file = ROOT_DIR + "/" + "resources/files/lana.jpg"

        self.logger.info('file: ' + str(file))

        self.path = "images/lana.jpg"
        self.filename = "lana.jpg"

        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):

#        rc, res = Api.download_file(self.jwt, self.filename, self.path)
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class DownloadSoundFile(BaseTest):
    """
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        file = ROOT_DIR + "/" + "resources/files/musica3.mp3"

        self.logger.info('file: ' + str(file))

        self.path = "sounds/musica.mp3"
        self.filename = "musica.mp3"

        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):

#        rc, res = Api.download_file(self.jwt, self.filename, self.path)
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class DownloadVideoFile(BaseTest):
    """
    """

    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        file = ROOT_DIR + "/" + "resources/files/teste.mp4"

        self.logger.info('file: ' + str(file))

        self.path = "video/video.mp4"
        self.filename = "video.mp4"

        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):

#        rc, res = Api.download_file(self.jwt, self.filename, self.path)
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

