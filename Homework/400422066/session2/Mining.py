from hashlib import sha256
import time as t

def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()

'''
what is mining ? mining is the process of guessing a nonce that generates hash with first x number of zeros

sha256 generate a 265bit number from a given text, it always gives a definite output for a definite input
what is our text here that is definite?
Block number, transition details and previous hash value as constant values and a new value as nonce

what is nonce? A nonce is just a number that we increment every single time we validate a guess
               and by changing that one number we are getting a completely different hash.

what is the goal of this code? find the Nonce value

'''

def mine(block_number,transaction,previous_hash,prefix_zeros):
  prefix_str='0'*prefix_zeros
  nonce=0
  # start with an infinite loop which will run till a break to find nonce
  while(1):
    text= str(block_number) + transaction + previous_hash + str(nonce)
    hash = SHA256(text)
    nonce=nonce+1
    if hash.startswith(prefix_str):
      print("Block mined with nonce value :",nonce)
      return hash
  print("Could not find a hash in the given range of upto")



# define input values : transactions (an arbitrary test as an example),difficult(# of zeros),blocknumber,previous hash)
transactions='''
Alice->Bob->10
Bob->Charlie->5
Charlie->Dan->15
'''
difficulty = 4
begin=t.time()
new_hash = mine(100,transactions,"000000000000000000006bd3d6ef94d8a04de84e171d3553534783b128f06aad",difficulty)
print("Hash value : ",new_hash)
# time taken;to understant why mining is difficult
time_taken=t.time()- begin
print("The mining process took ",time_taken,"seconds")
