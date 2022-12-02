# Import hash library
import hashlib

# Define crypto class with one method
class Block:
    # Method for mine a block
    # Get a block and date and previous hash(can be None - for future features)
    # Return correct nonce and hash
    def mine(self, block, data, previous_hash=None):
        # Initialize nonce
        nonce = 0
        # look for correct nonce with greedy algorithm
        while True:
            # create a string from data to be hashed
            hashingData = str(block) + str(nonce) + data
            if previous_hash is not None:
                hashingData += previous_hash
            # hash data using sha256 algorithm and get the hex of hashed value
            hash = hashlib.sha256(hashingData.encode()).hexdigest()
            # check if hash hexadecimal value starts with 4 zeros
            if hash[:4] == '0000':
                # nonce is correct, and we will return the nonce and the hash
                return {"hash": hash, "nonce": nonce}
            nonce += 1
