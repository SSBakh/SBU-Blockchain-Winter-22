***The Second Homework - Fatemeh Nazarmohammadi***

Link of first part in my Google Colab (https://colab.research.google.com/drive/1Gu6x1E9H72ZUdolH5oBgKi2ifN4u3bCd?usp=sharing)

*1/A - RSA keypair*

I use the pycryptodome library to create RSA key pairs:
```python
pip install pycryptodome
```
Also I need other calls:
As I am using the RSA algorithm, we need to import it from Crypto.PublicKey.
I am also using the OAEP-Padding scheme. We have imported PKCS1_OAEP from Crypto.cipher.
To convert binary to ASCII, I have imported binascii.
```python
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
import binascii 
```
Then I create keypair values using RSA.generate in this way:
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
***2***

***Mining a block***

Link of second part in my Google Colab (https://colab.research.google.com/drive/1SMWw44qmveQPjMzXFPxq3DoAIGlFLbzR?usp=sharing)

Start by simply enumerating an integer through our sha256 hash function until I find a hash with 4 leading zeros.

Use a while loop, passing the variable “y” through my hashing function each time the loop runs. I then inspect the first 4 digits [:4] of my hash value. If the first four digits equal 0000 then I exit the loop by setting the found variable to 1

```python
import hashlib 

y = 1
found = 0
string = 'this'
while found == 0:
  hashed == hashlib.sha256(string.encode('utf-8')).hexdigest()
  if hashed[:4] == '0000':
    found =1
  y +=1
print(hashed)
Print(y)
```
 Now combining the block number, nonce, data, and previous hash of my simulated block and passing it through my encryption function.  

the only value I change per iteration is the Nonce. I keep passing my block through the hashing function until I find the Nonce that gives me a hash below the target.
```python
# Simulation of mining a block

block = 123
NONCE = 0
data = 'Johh = $100'
previousHash = hh

# Combining the block number, nonce, data and previous hash of simulated block 
# Passing it through my encryption function
found = 0 
while found == 0:
  z = str(block)+str(NONCE)+data+previousHash
  newHash = hashlib.sha256(z.encode()).hexdigest()
  if newHash[:4] == '0000':
    found = 1
  NONCE +=1
print(newHash)
print(NONCE)
```






