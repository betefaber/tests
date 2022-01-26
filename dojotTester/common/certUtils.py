import os
import random

from OpenSSL import crypto

import dojotTester
from common.utils import save_file
from config import CONFIG


def get_csr(device_id, cname, dnsname, ipaddr):
    private_key_file = dojotTester.ROOT_DIR + "/" + CONFIG['security']['cert_dir'] + "/" + device_id + ".key"
    ss = []
    if dnsname:
        for i in dnsname:
            ss.append("DNS: %s" % i)

    if ipaddr:
        for i in ipaddr:
            ss.append("IP: %s" % i)
    ss = ", ".join(ss)

    req = crypto.X509Req()
    req.get_subject().CN = cname

    # Add in extensions
    base_constraints = ([
        crypto.X509Extension(b"keyUsage", False,
                             b"Digital Signature, Non Repudiation, Key Encipherment"),
        crypto.X509Extension(b"basicConstraints", False, b"CA:FALSE"),
    ])
    x509_extensions = base_constraints

    if ss:
        san_constraint = crypto.X509Extension(b"subjectAltName", False, bytes(ss, "utf-8"))
        x509_extensions.append(san_constraint)

    req.add_extensions(x509_extensions)

    with open(private_key_file) as keyfile:
        key = crypto.load_privatekey(crypto.FILETYPE_PEM, keyfile.read())

    req.set_pubkey(key)
    req.sign(key, "sha256")

    return crypto.dump_certificate_request(crypto.FILETYPE_PEM, req).decode("ascii")


def generatePrivateKey(keyFile, bitLen):
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, bitLen)
    save_file(keyFile, crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode("ascii"))


class CA:
    def __init__(self, cname: str = 'My CA', organization: str = 'My Organization', key: crypto.PKey = None):
        if key is None:
            self.ca_key = crypto.PKey()
            self.ca_key.generate_key(crypto.TYPE_RSA, 2048)
        else:
            if not isinstance(key, crypto.PKey):
                raise TypeError(f"key must be a crypto.PKey object")
            self.ca_key = key
            self.ca_key.check()

        self.ca_cert = crypto.X509()
        self.ca_cert.set_version(2)
        self.ca_cert.set_serial_number(random.randint(50000000, 100000000))

        self.ca_subj = self.ca_cert.get_subject()
        self.ca_subj.commonName = cname
        self.ca_subj.O = organization
        self.ca_subj.OU = "Certificate Issuer"

        self.ca_cert.add_extensions([
            crypto.X509Extension(b"basicConstraints", False, b"CA:TRUE, pathlen:0"),
            crypto.X509Extension(b"keyUsage", True, b"Digital Signature, keyCertSign, cRLSign")
        ])

        self.ca_cert.set_issuer(self.ca_subj)
        self.ca_cert.set_pubkey(self.ca_key)

        self.ca_cert.gmtime_adj_notBefore(0)
        self.ca_cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
        self.ca_cert.add_extensions([
            crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash", subject=self.ca_cert)
        ])

        self.ca_cert.add_extensions([
            crypto.X509Extension(b"authorityKeyIdentifier", False, b"keyid:always", issuer=self.ca_cert)
        ])

        self.ca_cert.sign(self.ca_key, 'sha256')

    def get_crt_pem(self):
        return crypto.dump_certificate(crypto.FILETYPE_PEM, self.ca_cert).decode("ascii")

    def save_crt_file(self, path):
        """
        path: path including file name
        """
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        with open(path, "wt") as f:
            f.write(self.get_crt_pem())

    def save_key_file(self, path):
        """
        path: path including file name
        """
        # Save private key
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        with open(path, "wt") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, self.ca_key).decode("ascii"))


class TrustedClientCertificate:

    def __init__(self, ca: CA, cname: str = "Client"):
        ca_cert = ca.ca_cert
        ca_key = ca.ca_key
        ca_subj = ca.ca_subj

        self.client_key = crypto.PKey()
        self.client_key.generate_key(crypto.TYPE_RSA, 2048)

        self.client_cert = crypto.X509()
        self.client_cert.set_version(2)
        self.client_cert.set_serial_number(random.randint(50000000, 100000000))

        client_subj = self.client_cert.get_subject()
        client_subj.commonName = cname

        self.client_cert.add_extensions([
            crypto.X509Extension(b"basicConstraints", False, b"CA:FALSE"),
            crypto.X509Extension(b"authorityKeyIdentifier", False, b"keyid:always", issuer=ca_cert),
            crypto.X509Extension(b"extendedKeyUsage", False, b"serverAuth, clientAuth, emailProtection"),
            crypto.X509Extension(b"keyUsage", False,
                                 b"Digital Signature, Non Repudiation, Key Encipherment, Key Agreement"),
        ])

        self.client_cert.set_issuer(ca_subj)
        self.client_cert.set_pubkey(self.client_key)

        self.client_cert.gmtime_adj_notBefore(0)
        self.client_cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)

        self.client_cert.add_extensions([
            crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash", subject=self.client_cert),
        ])

        self.client_cert.sign(ca_key, 'sha256')

    def get_crt_pem(self):
        return crypto.dump_certificate(crypto.FILETYPE_PEM, self.client_cert).decode("ascii")

    def save_crt_file(self, path):
        """
        path: path including file name
        """
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        with open(path, "wt") as f:
            f.write(self.get_crt_pem())

    def save_key_file(self, path):
        """
        path: path including file name
        """
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        with open(path, "wt") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, self.client_key).decode("ascii"))
