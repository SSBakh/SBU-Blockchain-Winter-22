from cryptography.hazmat.primitives import hashes
import time
import json

def Mine(block):
    digest = hashes.Hash(hashes.SHA256())
    #block_number
    block_number = block["block number"]
    message_byte = bytes(str(block_number), 'utf-8')
    digest.update(message_byte)
    #transactions
    for trx in block["transactions"]:
        message_byte = bytes(trx, 'utf-8')
        digest.update(message_byte)
    #previous_hash
    message_byte = bytes(block["previous_hash"], 'utf-8')
    digest.update(message_byte)
    for i in range(10000000000000):
        digest1 = digest.copy()
        #nonce
        block["nonce"] = str(i)
        message_byte = bytes(block["nonce"], 'utf-8')
        digest1.update(message_byte)
        output = digest1.finalize()
        output = output.hex()
        if output[:4] == "0000":
            timestamp = time.time()
            break
    return(output, timestamp, i)


with open('block.txt') as f:
    block = f.read()
block = json.loads(block)

hash, timestamp, nonce = Mine(block=block)
print(f'hash:{hash}, timestamp:{timestamp}, nonce:{nonce}\n block:\n{block}')