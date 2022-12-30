# import library
from hashlib import sha256

# define a function that receives a block number, data & difficulty in order to mine an arbitrary block
def mine(block_number,data,prefix_zeros):
# number of zeros to mine
  prefix_str='0'*prefix_zeros
# add a nonce in a range and go through to find the specific hash
  for nonce in range(MAX_NONCE):
    text= str(block_number)  + data + str(nonce)
    hash = sha256(text.encode("ascii")).hexdigest()
    #print(hash)
# compare the generated hash with condition that is ordered
    if hash.startswith(prefix_str):
      print("block mined with nonce value: ", nonce)
      return hash
# print the result
  print("Could not find a hash in the given range: ", MAX_NONCE)

#--------------- data initialization --------------

# maximum number of nonce
MAX_NONCE = 1000000

# block number
block_number = 684261

# data (i.e. string & ...) that hashed
data = ".sha256('some text').hex()."

# number of zero to find
difficulty = 4

#--------------- call the function to see the result --------------

mined_block = mine(block_number, data, difficulty)

print("Hash value : ",mined_block)
