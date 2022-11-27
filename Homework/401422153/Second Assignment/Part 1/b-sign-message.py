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
