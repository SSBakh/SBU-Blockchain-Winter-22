# Import library
# Import serialization and rsa and padding and hashes, invalid signature exception from cryptography library
import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


# Define crypto class with three methods
class Crypto:
    # Method for generate RSA key pair
    def generateRsaKeys(self):
        # Generate private key
        private_key = rsa.generate_private_key(65537, 2048)
        # Serialize the private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        # Convert to PEM format and create private_key.pem file on your current working directory
        with open('private_key.pem', 'wb') as f:
            f.write(private_pem)
        # Serialize public key
        public_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        # Convert to PEM format and create public_key.pem file on your current working directory
        with open('public_key.pem', 'wb') as f:
            f.write(public_pem)

    # Method for signing a message
    # Get a private key object and a message, return a hexadecimal signature
    def signing(self, private_key, message):
        if isinstance(private_key, str):
            # Crate a private key object from file
            with open(private_key, 'rb') as f:
                private_key = serialization.load_pem_private_key(f.read(), password=None)
        # Sign a message with the private key
        signature = private_key.sign(
            # Convert message to byte
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return signature.hex()

    # Method to verify a signature with a public key and a message
    # Get message and public key and signature
    # prints out the result whether the signature is valid or invalid.
    def verify(self, message, public_key, signature):
        # Crate a public key object from file
        if isinstance(public_key, str):
            with open(public_key, 'rb') as f:
                public_key = serialization.load_pem_public_key(f.read())
        try:
            # try to verify signature
            public_key.verify(
                # Convert signature and message to byte
                bytes.fromhex(signature),
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print("Signature is valid")
        # InvalidSignature exceptions will raise if verify method can not verify the signature
        except InvalidSignature:
            print("Signature is invalid")
