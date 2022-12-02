## Requirements
```
from hashlib import sha256
```

## New block with a certain difficulty and transaction


```
mine(block_num,transactions,previous_hash,difficulty)

```

## Finding the nonce
In this loop we are trying to find nonce with certain difficulty(amount of zeros we want our hash to start with), this loop continues unitl we find the unique number that our hash start with certain amount of zeros we want.
```
    while(True):
        text= str(block_number) + transaction + previous_hash + str(nonce)
        hash = SHA256(text)
        nonce=nonce+1
        if hash.startswith(prefix_str):
            print("Coin mined with nonce value :",nonce)
            return hash
```

## Time taken to mine a block
```
begin=t.time()
t.time() - begin
```
