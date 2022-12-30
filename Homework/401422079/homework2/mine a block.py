from cryptography.hazmat.primitives import hashes

#create first block for mining
message = b'this is data for mining'
blocknumber=1
nonce=0

#function for create hash to mining
def mining_functhion(noncefuncthion):
    #convert data to bytes
    blocknumber_bytes=bytes(str(blocknumber),'utf-8')
    nonce_bytes=bytes(str(noncefuncthion),'utf-8')
    #hashing the data
    digest = hashes.Hash(hashes.SHA256())
    digest.update(blocknumber_bytes)
    digest.update(message)
    digest.update(nonce_bytes)
    hash_outpot= digest.finalize()
    return hash_outpot.hex() #return the hash of data

loop=True
#start mining
while loop:
    finallhash=mining_functhion(nonce) #create the hash
    check = str(finallhash).startswith('0000') #check the hash to start with 0000
    if check:
        loop=False # the end of mining
    else:
        nonce=nonce+1 #increse the nonce to create new hash
# print the data of mined block
print("----block----")
print("blocknumber :"+str(blocknumber))
print("message :"+str(message))
print("nonce :"+str(nonce))
print("hash of block :"+str(finallhash))
