from cryptography.hazmat.primitives import hashes

def hash_block(number, nonce, data, prev_hash):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(bytes(number))
    digest.update(bytes(nonce))
    digest.update(bytes(data, 'utf-8'))
    digest.update(prev_hash)
    return digest.finalize()

def mine_new_block(number, data, prev_hash):
    nonce = 0
    while True:
        nonce = nonce + 1
        block_hash = hash_block(number, nonce, data, prev_hash)
#        print(block_hash[0:2].hex())
#        print(bytearray(2).hex())
#        return nonce
        if(block_hash[0:2] == bytearray(2)):
            return nonce

non = mine_new_block(1, "Hello!", bytearray(32))
print(non)
print(hash_block(1, non, "Hello!", bytearray(32)).hex())

