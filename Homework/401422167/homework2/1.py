import random

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

DATA = b'Hello World'

PADDING = padding.PSS(
    mgf=padding.MGF1(hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH
)

ALGORITHM = hashes.SHA256()


def generate_rsa_keys() -> (rsa.RSAPrivateKey, rsa.RSAPublicKey):
    """1.aleph"""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    return private_key, private_key.public_key()


def sign_data(private_key: rsa.RSAPrivateKey, data: bytes) -> bytes:
    """1.be"""
    return private_key.sign(data=data, padding=PADDING, algorithm=ALGORITHM)


def verify(data: bytes, public_key: rsa.RSAPublicKey, signature: bytes) -> bool:
    """1.pe"""
    try:
        public_key.verify(signature=signature, data=data, padding=PADDING, algorithm=ALGORITHM)
    except InvalidSignature:
        return False
    return True


def main():
    private_key, public_key = generate_rsa_keys()
    signature = sign_data(private_key, DATA)

    invalid_signature = bytearray(signature)
    random.shuffle(invalid_signature)
    invalid_signature = bytes(invalid_signature)

    print('signature =', signature.hex())
    print()
    print('invalid_signature =', invalid_signature.hex())
    print()
    print('verify(DATA, public_key, signature) =', verify(DATA, public_key, signature))
    print('verify(DATA, public_key, invalid_signature) =', verify(DATA, public_key, invalid_signature))


main()
