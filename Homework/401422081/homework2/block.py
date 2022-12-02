
from hashlib import sha256
import json
from time import time


class Block:

    def __init__(self, blockNumber=0, data=None):
        self.blockNumber = blockNumber
        self.data = [] if data is None else data
        self.nonce = 0
        self.hash = self.getHash()

    def getHash(self):
        result = 'none'
        while (result[0]!='0' or result[1] != '0' or result[2] != '0' or result[3] != '0'):
            hash = sha256()
            hash.update(str(self.data).encode('utf-8'))

            hash.update(str(self.blockNumber).encode('utf-8'))
            hash.update(str(self.nonce).encode('utf-8'))
            result = hash.hexdigest()
            # print(result + '\n' + str(self.nonce))
            self.nonce += 1

        self.hash = result
        return result

    def mine(self):
        self.nonce = 0 #Resetting nonce 0 to find it again in mining process 
        while self.hash != self.getHash() :
            self.nonce += 1
        print('Found the nonce: ' + str(self.nonce))

print('Creating block with hash starting with 0000, please wait ... ')
block = Block(1, "kiarash")
print('Block hash: ' + block.hash)
print('Block nonce: ' + str(block.nonce))
print('Now mining the block, wait ...')
block.mine()
