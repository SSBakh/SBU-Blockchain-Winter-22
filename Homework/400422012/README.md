## Overview

A simple python program that 1. generates an RSA key pair, signs and verifies a message and 2. simulates a simple block mining using [cryptography library](https://pypi.org/project/cryptography/).

## Features

* RSA signature scheme implementation
* Simple mining algorithms (mine and verify)

## Installation

Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cryptography.

```python
!pip install cryptography
```

## Import dependency
```python
- from cryptography.hazmat.primitives.asymmetric import rsa, padding
- from cryptography.hazmat.primitives import serialization, hashes
- from cryptography import exceptions
```

## Key generation
To make transactions in a blockchain system, a signature keypair is needed, where the private key is used to sign transactions and the public key to verify the signature.



```python
keygen()
```
## Signing and verification
Signature generation and verification of message m, respectively with private key private_key and public key public_key
```python
sign(m, private_key)
verify(m, public_key, signature)
```
### Example

```python
message = b"Hello world"
privkey, pubkey = keygen()
signature = sign(message,privkey)
verify(message, pubkey, signature)
```


## Block mining simulation
The function mine() takes a block number and some block data as input and returns a valid nounce (i.e., a nounce that yields a hash output starting with '0000')

```python
mine (block_num , block_data)
```


The function verify_nounce() checks if a given nounce is valid 
```python
verify_nounce (block_num, block_data, nounce)
```
