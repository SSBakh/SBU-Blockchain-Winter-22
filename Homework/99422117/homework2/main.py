from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding


# Task 1 - Creating a pair of private and public keys using RSA algorithm
def generate_key_pairs():
    # generating the private key using rsa built-in function (generate_private_key)
    # we have provided the documentation's recommended values
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        # less than 1024 is considered breakable
        key_size=2048
    )
    # public key can be derived from private key
    public_key = private_key.public_key()

    # Saving the private key into a pem file
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private_key.pem', 'wb') as f:
        f.write(pem)

    # Saving the public key into a pem file
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)

    return [private_key, public_key]


# Task 2 - Signing a message using private key
def sign_message(message, private_key):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


# Task 3 - Validating signature
def validate_signature(message, public_key, signature):
    return public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


# Reading Private and Public keys from file
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )


# signing message
message = b"You'll never walk alone"
signature = sign_message(message, private_key)

# validating the signed message
validate_signature(message, public_key, signature)
