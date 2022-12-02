from CryptographyBlockchain.keys.PublicKey import convert_pem_to_public_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def covert_hex_to_bytes(hex_text):
    return bytes.fromhex(hex_text)


def get_verify_sign_message(public_key_pem, sign_hex, message):
    public_key = convert_pem_to_public_key(public_key_pem)
    bytes_sign = covert_hex_to_bytes(sign_hex)
    bytes_message = str.encode(message)
    
    try:
        public_key.verify(
        bytes_sign,
        bytes_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
        )
        return True
    except:
        #if message not sign  raise exception 
        return False