***The Second Homework - Fatemeh Nazarmohammadi***

Link of first part in my Google Colab (https://colab.research.google.com/drive/1Gu6x1E9H72ZUdolH5oBgKi2ifN4u3bCd?usp=sharing)

*1/A - RSA keypair*

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

*1/B - Signing a message with a private key*
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
*1/C - Signing a message with a public key and verify*
Verify the signature, by decrypting the signature using the public key (raise the signature to power e modulo n) and comparing the obtained hash from the signature to the hash of the originally signed message:
```python
# RSA verify signature
msg = b'Aysan NazarMohammadi'
hash = int.from_bytes(sha256(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)  # Raise the signature to power e modulo n
print("Signature valid:", hash == hashFromSignature) # Comparing obtained hash from the signature to the hash of the originally signed message
```




