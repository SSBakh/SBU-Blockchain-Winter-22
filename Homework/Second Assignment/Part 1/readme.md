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
