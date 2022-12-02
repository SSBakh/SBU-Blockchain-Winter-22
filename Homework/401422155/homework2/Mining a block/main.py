from hashlib import sha256
import time as t

def SHA256(text):
    """
    :param text: str, a string consist of block_number, transaction, previous hash and nonce
    :return: bytes, the hash of the mine in sha256
    """
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number,transaction,previous_hash,prefix_zeros):
    """
    :param block_number: int, number of the block
    :param transaction: str, a string consist of the sender's name, receiver's name & amount of value being sent
    :param previous_hash: str, hash from the previous block
    :param prefix_zeros: int, the number of zeros we want our hash to start with
    """
    prefix_str='0'*prefix_zeros
    nonce=0
    while(True):
        text= str(block_number) + transaction + previous_hash + str(nonce) 
        hash = SHA256(text)
        nonce=nonce+1
        print(hash , nonce)
        if hash.startswith(prefix_str):
            print("Block mined with nonce value :",nonce)
            return hash
#_____________________________________________

transactions='''
A->B->10
B->C->6
C->D->7
'''
difficulty = 4
previous_hash = "000000000000000000006bd3d6ef94d8a01de84e171d3553534783b128f06aad"
block_num = 684260
new_hash = mine(block_num,transactions,previous_hash,difficulty)
print("Hash value : ",new_hash)

begin=t.time()
time_taken=t.time() - begin
print("The mining process took ",time_taken,"seconds")
