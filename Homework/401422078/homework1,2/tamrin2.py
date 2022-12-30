# import neccessary libraries
# we don't need external library. we will just use a bunch of standard library
import time # we will use this module for setting time of transaction
import json # we will use this module for formatting content of our block
from hashlib import sha256 # we will use this module for hashing the content of block



# the best data structure for saving content of each block is json format
# we can use json format like below : 
                                              # {   
                                              #     "author": "name of author",
                                              #     "timestamp": "the time of transaction", 
                                              #     "data": "content of transaction"
                                              # }



# first of all we need to create a block class and in the future, we will create objects from this block and then chain them
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
      # in this function we need to set some attribute for our block 
      # we also pass the previous hash block and use it in current block!( because of protecting integrity of chain)
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    # in below function we hash the content of block. because we don't want anyone can read the content of block or write sth on it
    # each block has this fucntion and with calling this function, we get the hash of block's content
    def compute_hash(self):

        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
      
      

# create blockchain class that we can handle the chain and add or mine blocks
class Blockchain:
    # below parameter, adjust the difficulty of our algorithm, and in excercise, mentioned that set this paramer to 4 ( means 4 zero)
    difficulty = 4   
     
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    
    # we use this function for initializing the blockchain. actaully this function creates an initial block with an index of 0 and a previous hash of 0, and then add this to the chain. actually this genesis block is the name of block the bitcoin used it! 
    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]


    # the adding block mechanism is used when we mine the blocks. actually in mining we check the verification of transaction.
    # in this function, first of all we check the hash of last block in the chain with the hash of the "previous hash" of block that saved in the block that we want to add to the chain. they must be the same!. after that we check other validiy with is_valid_proof() function. that we will comment about it in future
    def add_block(self, block, proof):

        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    # as i said before, we used this function in add_block() function. actually this function checks whether the block_hash is valid hash of block and has the difficulty ( that is 4 zero! in excercise)
    def is_valid_proof(self, block, block_hash):

        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    # this function tries different values for nonce to get a hash that has our difficulty( that is 4 zero! in excercise), and we call it when we are creating new block in mine() function
    def proof_of_work(self, block):

        block.nonce = 0

        computed_hash = block.compute_hash()
        # as said in tamrin : we start with 4 zero
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    # use this function for adding new transaction and then use mine function to mine it 
    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)



# below function add transactions to the blockchain, but before adding them, create a blcok object and then evaluate proof_of_work of that block 
    def mine(self):

        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []
        return new_block.index




# before testing we just need to create an empty blockchain and initialize it 
blockchain = Blockchain()
# create a function for getting content of chain with json format 
def chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data), "chain": chain_data})
    
    
# test 
print("-----------------------------------------------------------------------------------------------------")
print(f"the early chain is : \n {chain()}")
print("-----------------------------------------------------------------------------------------------------")
blockchain.add_new_transaction(["ali paid to amir 10000 rials"])
print("adding pending transaction and mining chain .... ")
print(f"block.mine() : {blockchain.mine()}")
print(f"the chain is : \n {chain()}")
print("-----------------------------------------------------------------------------------------------------")
blockchain.add_new_transaction(["hamid paid to parisa 200000 rials"])
print("adding pending transaction and mining chain .... ")
print(f"block.mine() : {blockchain.mine()}")
print(f"the chain is : \n {chain()}")
print("-----------------------------------------------------------------------------------------------------")
blockchain.add_new_transaction(["reza paid to sadegh 800000 rials"])
print("adding pending transaction and mining chain .... ")
print(f"block.mine() : {blockchain.mine()}")
print(f"the chain is : \n {chain()}")
print("-----------------------------------------------------------------------------------------------------")
blockchain.add_new_transaction(["yasam paid to sadegh 9000 rials"])
print("adding pending transaction and mining chain .... ")
print(f"block.mine() : {blockchain.mine()}")
print(f"the chain is : \n {chain()}")
print("-----------------------------------------------------------------------------------------------------")
