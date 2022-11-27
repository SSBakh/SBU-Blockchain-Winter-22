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
