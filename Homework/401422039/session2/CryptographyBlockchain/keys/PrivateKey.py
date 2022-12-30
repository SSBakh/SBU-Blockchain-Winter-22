from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

    
def create_private_key():
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    )
    return private_key
    
def private_key_to_PEM(private_key):
    pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())
    return pem.decode("utf-8")

def convert_pem_to_private_key(pem):
    bytes_pem=str.encode(pem)
    private_key=serialization.load_pem_private_key(bytes_pem,password=None)
    return private_key