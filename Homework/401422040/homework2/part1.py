from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_key(size=2048):
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=size)
    return (key, key.public_key())

def sign(private_key, message):
    signature = private_key.sign(
        bytes(message, 'utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256())
    return signature

def verify(message, public_key, signature):
    try:
        public_key.verify(
            signature,
            bytes(message, 'utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
        return True
    except:
        return False

(prv, pub) = generate_key()
message = "Hello!"
sgn = sign(prv, message)
print(verify("hello!", pub, sgn))
print(verify(message, pub, sgn))
