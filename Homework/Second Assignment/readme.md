# Assignments

## Part 1
### By using the Python **Cryptography** Library write functions that:

**a)** Generate **Private/Public** keys by using the **RSA** algorithm.

First of all by using the package manager [pip](https://pip.pypa.io/en/stable/), install the **Cryptography** Library.

```bash
pip install cryptography
```
After that run below codes:

```python

# import library
import cryptography

# import rsa from cryptography library
from cryptography.hazmat.primitives.asymmetric import rsa

#--------------- generate private key --------------

# generate private key
private_key = rsa.generate_private_key(

    public_exponent=65537,

# size of the key
    key_size=2048,
)

#--------------- generate public key --------------

public_key = private_key.public_key()


```

**b)** Sign a message by using a **private** key.

**Note**: this function uses the **private key** that produced by the **previous function** in part (a), so before running this part you must run **part (a)** or you can use **your** private key as an input.

```python

# import library
import cryptography

# import hashes & padding form cryptography library
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# define a function that receives message & private key in order to sign a message
def sign_message(message,private_key):

# signature defined as a global variable because we want use it in the next function  
    global signature
    signature = private_key.sign(
        message,
# add padding & salt for hashing
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
# print signature as a hex code
    print(signature.hex())

#--------------- call the function to see the result --------------

sign_message(b"Payam man jahat emza",private_key)


```
**c)** Receive a **message**, verify the validation of **signature** by using **public** key.

**Note**: this function uses **signature** and **public key** that produced by the **previous functions** in parts (a) & (b), so before running this part you must run **parts (a) & (b)** or you can use **your** own **signature** and **public key** as inputs.


```python

# import library
import cryptography

# import hashes & padding form cryptography library
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# define a function that receives message, public key & signature in order to verify the validation of signature
def verify_signature(public_key,message,signature):  
    try:
        public_key.verify(
            signature,
            message,
# add padding & salt for hashing
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
# raise a message when the signature is invalid
    except cryptography.exceptions.InvalidSignature:
        print('signature is invalid.')
# raise a message when the signature is valid
    else:
        print('signature is valid.')

#--------------- call the function to see the result --------------

verify_signature(public_key,b"Payam man jahat emza",signature)



```

##

## Part2

### Mine a block that includes a block number, data & nonce. The block hash must start with four zeros (0000).

First of all by using the package manager [pip](https://pip.pypa.io/en/stable/), install the **hashlib** Library (if not installed).

```bash
pip install hashlib

```
After that run below codes:

```python

# import library
from hashlib import sha256

# define a function that receives a block number, data & difficulty in order to mine an arbitrary block
def mine(block_number,data,prefix_zeros):
# number of zeros to mine
  prefix_str='0'*prefix_zeros
# add a nonce in a range and go through to find the specific hash
  for nonce in range(MAX_NONCE):
    text= str(block_number)  + data + str(nonce)
    hash = sha256(text.encode("ascii")).hexdigest()
    #print(hash)
# compare the generated hash with condition that is ordered
    if hash.startswith(prefix_str):
      print("block mined with nonce value: ", nonce)
      return hash
# print the result
  print("Could not find a hash in the given range: ", MAX_NONCE)

#--------------- data initialization --------------

# maximum number of nonce
MAX_NONCE = 1000000

# block number
block_number = 684261

# data (i.e. string & ...) that hashed
data = ".sha256('some text').hex()."

# number of zero to find
difficulty = 4

#--------------- call the function to see the result --------------

mined_block = mine(block_number, data, difficulty)

print("Hash value : ",mined_block)



```

## End
