
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
