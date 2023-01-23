from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

# 1. Generate a private and public key with RSA

def generate_keys():
    private_key = rsa.generate_private_key( public_exponent=65537, key_size=1024)
    pub_key = private_key.public_key()
    return private_key, pub_key

# 2. Sign th message with the private key. 

def sign(private_key, message) :
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# 3. verifys the sign and returns the result from verfication

def verify(signature, public_key, message):
    result = public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    if result == None:
        result = "your message is verified"
    return result

# To test the code, these steps are followed:
private_key, pub_key = generate_keys()      #Generates a keypair with rsa 
test_message = input("Enter your message to sign it with your generated key:\n")        #Get an input message from the user
b_test_message = str.encode(test_message)       #Change the format from str to bytes
signature = sign(private_key, b_test_message)       #Sign the message with the generated private key
new_message = input("To verify, Enter your message again, otherwise it will be considered a tampered message:\n")       #User should enter the same message otherwise it wont be verified 
b_new_message = str.encode(new_message)

try:
    print(verify(signature, pub_key, b_new_message))    #Verifies the sign with the re-enterd message and prints the result
except:
    print("your message is tampered and is not verfied ")
