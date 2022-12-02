from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey


class CryptographyHelper:

    def __init__(self):
        self.default_encoding = 'utf-8'
        self.default_hash = hashes.SHA256()
        self.default_padding = padding.PSS(
            mgf=padding.MGF1(self.default_hash),
            salt_length=padding.PSS.MAX_LENGTH
        )

    def generate_keys(self) -> (RSAPrivateKey, RSAPublicKey):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        return private_key, private_key.public_key()

    def sign(self, private_key: RSAPrivateKey, message) -> str:
        message_bytes = bytes(message, self.default_encoding)
        sign_bytes = private_key.sign(
            message_bytes,
            self.default_padding,
            self.default_hash)
        sign_hex = sign_bytes.hex()

        return sign_hex

    def validate_sign(self, message, public_key: RSAPublicKey, sign: str) -> bool:
        try:
            message_bytes = bytes(message, self.default_encoding)
            sign_bytes = bytes.fromhex(sign)
            public_key.verify(
                sign_bytes,
                message_bytes,
                self.default_padding,
                self.default_hash
            )

            return True
        except:
            return False
