from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


#generating a RSA key pair 
#and saving it in nykey.pem
def generate_key_pair():
    key = RSA.generate(2048) #generating key pair
    f = open('mykey.pem', 'wb')
    f.write(key.export_key('PEM')) #writing the key in a file
    f.close()     

def sign(key, message):
    hashed = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hashed)
    return signature

def verify_signature(message, key, signature):
    hashed = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(hashed, signature)
        print("signature is valid")
    except(ValueError, TypeError):
        print("signature not valid")


generate_key_pair()

#opening the key saved in mykey.pem 
#and giving it as an input to sign() function
f = open('mykey.pem', 'r')
key = RSA.import_key(f.read())
message_to_sign = b"Hello World!" 
signature=sign(key, message_to_sign) 

wronge_message = b"Hello World!!!"
#decide wether to choose the correct message or the wrong one:
message = message_to_sign 
#message = wronge_message
verify_signature(message, key, signature)



































