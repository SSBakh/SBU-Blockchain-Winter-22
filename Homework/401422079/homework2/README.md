
# mine one block
we are here to mine  a block that contain blocknumber,message and nonce.
the hash of this block should start with four zero.
For this we used the [cryptography](https://pypi.org/project/cryptography/) library
## Code execution process

first we initialized nonce to zero and then we create mining_function to create the hash of created blocks. so we start mining in line 22. first we create a loop to pass between the blocks.
in step one we call mining_function with nonce parameter
this function return us a hash of the block
if the hash start with four zero the loop is break and mined the block .
so we print the hash and other dateails of block in line 31 to 35.
## Installation

to install cryptography

```bash
  pip install cryptography
```


## Documentation

- [cryptography](https://cryptography.io/en/latest/)
- [cryptography.hazmat.primitives](https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/)