from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# This function generates public/private key using RSA algorithm
def generate_public_private_key_using_RSA():
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    )

    return private_key.public_key(), private_key

# This function signs a given messege with a given private key
def sign_message(message, private_key):
    signature = private_key.sign(
    bytes(message, 'utf-8'),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )

    return signature

# This function verifies a signature
def verify(message, public_key, signature):
    try:

        public_key.verify(
        signature,
        bytes(message, 'utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
        )

        return True
    except:
        return False

# Testing functions
public_key, private_key = generate_public_private_key_using_RSA()
test_message = "test message"
signature = sign_message(test_message, private_key)

print(f"correct message verification: message is '{test_message}' verify: {verify(test_message, public_key, signature)}")
print(f"wrong message verification: message is 'hello' verify: {verify('hello', public_key, signature)}")