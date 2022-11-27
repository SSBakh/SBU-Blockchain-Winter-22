from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.exceptions import InvalidSignature

def key_pair_generator():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    pem_public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # Write to files
    private_key_file = open("rsa.pem", "w")
    private_key_file.write(pem_private_key.decode())
    private_key_file.close()

    public_key_file = open("rsa.pub", "w")
    public_key_file.write(pem_public_key.decode())
    public_key_file.close() 
    
    return pem_private_key,pem_public_key

def sign_message(input_private_key, input_message):
    private_key = load_pem_private_key(input_private_key, None)
    signature = private_key.sign(
        bytes(input_message, "utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def signature_validator(input_message, input_public_key, input_signature):
    try:
        public_key = load_pem_public_key(input_public_key) 
        public_key.verify(
            input_signature,
            bytes(input_message, "utf-8"),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    
def mine(input_data="sadra_balance=1000B", block_number=0):
    nonce=0
    generated_hash_hex = hashing(input_data, block_number, nonce).hex()
    while generated_hash_hex[0:4] != "0000":
        nonce += 1
        generated_hash_hex = hashing(input_data, block_number, nonce).hex()
    return generated_hash_hex, nonce

def hashing(input_data, block_number, nonce):
    generated_hash = hashes.Hash(hashes.SHA256())
    generated_hash.update(bytes(input_data, "utf-8"))
    generated_hash.update(bytes(str(block_number), "utf-8"))
    generated_hash.update(bytes(str(nonce), "utf-8"))
    return generated_hash.finalize()