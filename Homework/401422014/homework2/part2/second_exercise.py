
from cryptography.hazmat.primitives import hashes


def mineBlock():
    nonce = 0
    prefix = "0000"
    # Create a temp block with mock data
    block_number = 1
    block_data = "Hello python !"

    # Hash block base on nonce and block number and block data
    digest = hashes.Hash(hashes.SHA256())
    digest.update(str.encode(str(nonce)) + str.encode(str(block_number)) + str.encode(block_data))
    my_hash = digest.finalize().hex()

    # We check if my_hash doesn't start with 0000 , we increase the value of nonce by 1
    while my_hash[0:4] != prefix:

        digest = hashes.Hash(hashes.SHA256())
        digest.update(str.encode(str(nonce)) + str.encode(str(block_number)) + str.encode(block_data))
        my_hash = digest.finalize().hex()
        nonce = nonce + 1
    else:
        # Finally my_hash starts with 0000 , we print final value of nonce and my_hash
        print("Acceptable nonce is :", nonce)
        print("Final hash is :", my_hash)

if __name__ == '__main__':
    # Mine a block with block number = 1 and block data = 'Hello python !'
    mineBlock()
