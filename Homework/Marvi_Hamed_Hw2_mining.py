from Crypto.Hash import SHA256

# data of the block consists of block_num and data
# you can change these two variables
block_num = 4 
data = b'this is the data of the block'

h = SHA256.new()
block_num = bytes(block_num) #hash function doesn't accept type int

#now we have a loop to find a nonce so that the hash of these 3 
#variables (block_num, data and nonce) would start with four zeros
h.update(block_num)
h.update(data)
nonce = 0
state = True
while state:
    h2 = h
    nonce_bytes = bytes(nonce) #hash function doesn't accept int type
    h2.update(nonce_bytes)
    hashed = h2.hexdigest() 
    first_four = hashed[0:4]
    if(first_four=='0000'):
        print("found the nonce: ", nonce)
        print("hash of current block: ", hashed)
        state = False
    nonce = nonce+1
        

