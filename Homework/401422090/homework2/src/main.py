from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa
import hashlib
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes


def generate_key_pair(private_key_pass):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#generation
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(bytes(private_key_pass, 'utf-8'))
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem


def sign(private_key_pem, private_key_pass, message):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#signing
    private_key = serialization.load_pem_private_key(
        private_key_pem, password=bytes(private_key_pass, 'utf-8'), backend=default_backend())
    prehashed = hashlib.sha256(bytes(message, 'utf-8')).hexdigest()
    sig = private_key.sign(
        bytes(prehashed.encode('ascii')),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256())

    return base64.b64encode(sig).decode("utf-8")


def verify(public_key_pem, message, signed):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#verification
    try:
        public_key = serialization.load_pem_public_key(
            public_key_pem, backend=default_backend())
        prehashed = hashlib.sha256(bytes(message, 'utf-8')).hexdigest()
        sig = bytes(signed, 'utf-8')
        decoded_sig = base64.b64decode(sig)
        public_key.verify(
            decoded_sig,
            bytes(prehashed.encode('ascii')),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
        return True
    except InvalidSignature as error:
        print(error)
        return False


def hash_block(block_data, block_number, nonce):
    # https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/#module-cryptography.hazmat.primitives.hashes
    digest = hashes.Hash(hashes.SHA256())
    digest.update(bytes(block_data, 'utf-8'))
    digest.update(bytes(str(block_number), 'utf-8'))
    digest.update(bytes(str(nonce), 'utf-8'))
    return digest.finalize().hex()


def mine_block(block_data, block_number):
    nonce = 0
    block_hash = hash_block(block_data, block_number, nonce)

    while not block_hash.startswith("0000"):
        nonce = nonce + 1
        block_hash = hash_block(block_data, block_number, nonce)
        print(block_hash, nonce)
    return block_hash, nonce
