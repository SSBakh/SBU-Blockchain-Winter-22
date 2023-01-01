from cryptography.hazmat.primitives import hashes

class Block():  # Creates a class for attributes of an assumptive block.
    last_block_number = 0
    def __init__(self, data):
        self.data = user_data
        self.hash = None
        self.nonce = 0
        Block.last_block_number += 1

#Creates a block instance

def hashing():
    h = hashes.Hash(hashes.SHA256())    #Generate a SHA256 hash
    hash_concat = str.encode(   #Concatenate the info of the block
    str(block.nonce) +
    str(block.data) +
    str(block.last_block_number))
    h.update(bytes(str(hash_concat), "utf-8"))  #Encode the hash in utf-8 Format(for Hash Computational Process)
    return h.finalize().hex()   #Convert the hash to hex format

def mining(block):  #Increases the nonce if the hash was not starting with 0000. 
    hash = hashing()
    while hash[0:4] != "0000":
        block.nonce += 1
        hash = hashing()
    block.hash = hash
    return "Block Hash: " + str(block.hash) + "\nBlockNo: " + str(block.last_block_number) + "\nBlock Data: " + str(block.data) + "\nNonce: " + str(block.nonce) + "\n--------------"

#######################################################
user_data = input("Enter any data to create the block:\n") #Get the data section of the block
block=Block(user_data) #Create the block
print(mining(block))
#######################################################
