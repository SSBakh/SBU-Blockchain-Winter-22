from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_public_private_key():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def sign_with_private_key(private_key, plain_text_byte):
    signature = private_key.sign(plain_text_byte,
                                 padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                                 hashes.SHA256())
    return signature


def verify_message(plain_text, public_key, signature):
    try:
        public_key.verify(signature, plain_text, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                             salt_length=padding.PSS.MAX_LENGTH),
                          hashes.SHA256())
        return True
    except:
        return False


def hash_block(block_number, data, nonce):
    hasher = hashes.Hash(hashes.SHA256())
    hasher.update(block_number.encode('utf-8'))
    hasher.update(data.encode('utf-8'))
    hasher.update(nonce.encode('utf-8'))
    digest = hasher.finalize()
    return digest


def mine(block_number, data):
    nonce = 0
    while True:
        hashed_block = hash_block(str(block_number), data, str(nonce))
        hex_data = hashed_block.hex()
        if hex_data[:4] == '0000':
            break
        nonce += 1
    return nonce

# Generating public and private key
private_key, public_key = generate_public_private_key()
print(f'Private Key is: {private_key}')
print(f'Public Key is: {public_key}')
print()

# Signing a message with the private key
signature = sign_with_private_key(private_key, b'crypto')
print(f'Result of signing \'crypto\' with private key is: {signature.hex()}')
print()

# Verifying the message using the message and, public key and signature
is_verified = verify_message(b'crypto', public_key, signature)
print(f'Result of verification is: {is_verified}')
print()

# Calculating nonce using block number and data
block_num = 1
data = 'crypto'
nonce = mine(block_num, data)
print(f'Nonce for block number: <{block_num}> and data: <{data}> is {nonce}')
print()
