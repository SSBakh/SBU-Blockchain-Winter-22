import hashlib

# Task 4 - Mining a hypothetical block using the number of the block, data, and nonce
# nonce will be started at 0 and using a while loop we increment it 1 in each iteration
# till the specified condition met (hash starts with 4 zeros)

def mine(block_number, data):
    nonce = 0
    # variable to check whether we have found a hash that starts with 4 zeros
    # as long as It is zero (found variable) We continue to generate new hashes
    # and check the specifed condition against the generated hash
    found = 0
    while found == 0:
        # before we generate the hash, we concatenate block number, current nonce and block data
        concat = str(block_number) + str(nonce) + data
        # we use SHA256 hashing algorithm to hash our string then we convert it to hexadecimal
        hash = hashlib.sha256(concat.encode()).hexdigest()
        # if the generated hash starts with four leading zero we stop the loop by setting
        # the found variable to one
        #otherwise we increment nonce by one. (A brute force approach)
        if hash[:4] == '0000':
            found = 1
        nonce += 1
    print("block hash: " + str(hash))
    print("nonce: " + str(nonce))

block_number = 10
data = "You'll never walk alone"
mine(block_number, data)