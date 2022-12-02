from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


def GeneratePublicKey():
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048
        )
    public_key = private_key.public_key()
    pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
    )
    pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    private = pem_private
    public = pem_public
    text = (
        f'private key public key generation\n'
        f'private key bytes:\n{private}\npublic key bytes:\n{public}\nprivate key hex:\n{private.hex()}\npublic key hex:\n{public.hex()}\n'
        f'--------------------------------------------------------------------------------------------------------------------\n'
        )
    with open('RSA.txt', 'w') as f:
        f.write(text)
    return public, private


def Sign(key, mess):
    message_byte = bytes(mess, 'utf-8')
    key = bytes.fromhex(key)
    private_key = serialization.load_pem_private_key(
    key,
    password=None,
    )
    signature = private_key.sign(
        message_byte,
        padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )
    text = (
        f'signing a message\n'
        f'message:{mess}\nsignature bytes:\n{signature}\nsignature hex:\n{signature.hex()}\n'
        f'--------------------------------------------------------------------------------------------------------------------\n'
        )
    with open('RSA.txt', 'a') as f:
        f.write(text)
    return signature


def Verify(p_key, mess, signature):
    signature = bytes.fromhex(signature)
    message = bytes(mess, 'utf-8')
    key = bytes.fromhex(p_key)
    public_key = serialization.load_pem_public_key(
    key,
    )
    result = public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )
    if result == None:
        result = "verified"
        text = (
            f'verifying a message\n'
            f'message:{mess}\n'
            f'status:{result}\n'
            f'--------------------------------------------------------------------------------------------------------------------\n'
            )
        with open('RSA.txt', 'a') as f:
            f.write(text)
    return result

order = input("for generating public key type 1 or for signing a message type 2 or for verfying type 3 then press enter:\n")

if order == "1":
    public_key, private_key = GeneratePublicKey()
    print(f'public key hex: {public_key.hex()} \n private key hex: {private_key.hex()}')
elif order == "2":
    private_key = input("type your private key hex then press enter:\n")
    message = input("type your message then press enter:\n")
    signature = Sign(private_key, message)
    print(f'signature bytes: {signature}')
    print(f'signature hex: {signature.hex()}')
elif order == "3":
    public_key = input("type your public key hex then press enter:\n")
    message = input("type your message then press enter:\n")
    signature = input("type your signature hex then press enter:\n")
    result = Verify(public_key, message, signature)
    print(result)
else:
    print("Wrong input, try again")