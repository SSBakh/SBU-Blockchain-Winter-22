from CryptographyBlockchain.keys.PrivateKey import convert_pem_to_private_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def sign_message(message,private_key_pem):
    privat_key=convert_pem_to_private_key(private_key_pem)
    bytes_message=str.encode(message)
    sign=privat_key.sign(bytes_message,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH),
                    hashes.SHA256()
    )
    return sign.hex()