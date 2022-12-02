from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def Create_public_key(private_key):
    pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return pem.decode("utf-8")

def convert_pem_to_public_key(pem):
    bytes_pem=str.encode(pem)
    public_key=serialization.load_pem_public_key(bytes_pem)
    return public_key