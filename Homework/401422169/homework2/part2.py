from cryptography.hazmat.primitives import hashes

# Defining a Block
class Block():
    block_number = 0

    def __init__(self, data):
        self.data = data
        self.hash = ''
        self.nonce = 0
        Block.block_number += 1

# This function hashes the block data
def hash_data(block):
    hash = hashes.Hash(hashes.SHA256())
    data = f"{block.nonce}{block.data}{block.block_number}"
    data = bytes(data, 'utf-8')
    hash.update(data)
    return hash.finalize().hex()

# This function mines the given block (finds correct nonce for hash to start with "0000")
def mine(block):
    hashed_data = hash_data(block)
    while hashed_data[0:4] != "0000":
        block.nonce +=1
        hashed_data = hash_data(block)

    block.hash = hashed_data

    return block

# Testing functions
block = Block("test data")
mined_block = mine(block)

print(f"block number: {mined_block.block_number}\n\
block data: {mined_block.data}\n\
block hash: {mined_block.hash}\n\
block nonce: {mined_block.nonce}")
