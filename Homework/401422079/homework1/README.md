
# signing with RSA algorithm in python

we are here to sign a message with RSA algorithm in python,
for this situation we use [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/src/installation.html) library of python.

## Code execution process

first we create private and public key then create a function to sign the message what the user send it. after signing the message we create the function to check the signature .
so every thing ready for recive and sign message:
first in line 31 we take a message from user and call sign_message function,
after than we call verify function to verify the signuture .
For more certainty, we gave two test messages in lines 37 and 38 to verify function to measure the correctness of the program

## Installation

to install pycryptodome

```bash
  pip install pycryptodome
```


## Documentation

- [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/src/installation.html)
- [Crypto.PublicKey](https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html)
- [Crypto.hash](https://pycryptodome.readthedocs.io/en/latest/src/hash/sha256.html)
- [Crypto.signature](https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_v1_5.html)