***The Second Homework - Fatemeh Nazarmohammadi***

Link of first part in my Google Colab (https://colab.research.google.com/drive/1Gu6x1E9H72ZUdolH5oBgKi2ifN4u3bCd?usp=sharing)

*A - RSA keypair*

We use the pycryptodome library to create RSA key pairs:
```python
pip install pycryptodome
```
Also we need other calls:
As we are using the RSA algorithm, we need to import it from Crypto.PublicKey.
We are also using the OAEP-Padding scheme. We have imported PKCS1_OAEP from Crypto.cipher.
To convert binary to ASCII, we have imported binascii.
```python
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
import binascii 
```
Then we create keypair values using RSA.generate in this way:
```python
keyPair = RSA.generate(3072)
# Generating publickey value
pubKey = keyPair.publickey()  
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
# Generating privetkey value
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")  
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
```

*B - Signing a message with a private key*
Using the RSA private key {n, d}. Calculate its hash and raise the hash to the power d modulo n (encrypt the hash by the private key). I shall use SHA-512 hash. It will fit in the current RSA key size (1024). Have modular exponentiation as built in function pow(x, y, n):
```python
# Import sha256 from hashlib
from hashlib import sha256

# Define the message (As b)
msg = b'Aysan NazarMohammadi'

# Using the RSA private key {n, d} and Sign message 
hash = int.from_bytes(sha256(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))
```
*C - Signing a message with a public key and verify*






