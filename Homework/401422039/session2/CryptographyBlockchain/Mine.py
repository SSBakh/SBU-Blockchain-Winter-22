from cryptography.hazmat.primitives import hashes

#this fuction get hash of your list data
def get_hash_data(*args):
    digest=hashes.Hash(hashes.SHA256())

    for arg in args:
        digest.update(str.encode(arg))
    return digest.finalize().hex()

#this function have loop to find hash to start 0000
def min_data(data,hash_prev,block_number='1'):

    Nonce=0
    while True:
        data_hash=get_hash_data(block_number,str(Nonce),data,hash_prev,)
        if data_hash.startswith('0000'):
            return data_hash ,Nonce
        Nonce+=1


