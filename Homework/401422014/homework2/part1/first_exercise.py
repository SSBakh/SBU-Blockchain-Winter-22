
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def generate_rsa_key():
    # Generate private key using rsa
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Generate public key base on private_key
    public_key = private_key.public_key()

    return public_key,private_key

def sign_message(private_key,message):

    message_bytes = str.encode(message)

    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signed_message(message,publicKey,signature):
    message_bytes = str.encode(message)
    try:
        # Check message is valid or not
        publicKey.verify(
            signature,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
    )
        # return this message if signature is valid
        print("Your signature is valid .")
    except InvalidSignature:
        # return this message if signature is not valid
        print("Your signature is not valid .")




if __name__ == '__main__':
    # Create a pair of public/private key with rsa
    rsa_key = generate_rsa_key()
    public_key = rsa_key[0]
    private_key = rsa_key[1]

    print("Public key is :",public_key)
    print("Private key is :",private_key)

    # Sign 'Hello' message with private key
    signed_message = sign_message(private_key,"Hello")

    print("Signature is :", signed_message.hex())

    # Verify 'Hello' message with public key and signature
    verify_signed_message("Hello",public_key,signed_message)

    # Verify 'Hello 1' message with public key and signature
    verify_signed_message("Hello 1", public_key, signed_message)


