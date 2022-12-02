from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

#CREATE PRIVATE KEY.
key=RSA.generate(2048)
prvkey = key.export_key()
private_key=RSA.import_key(prvkey)

# CREATE public KEY.
pubkey = key.publickey().export_key()
public_key = RSA.import_key(pubkey)

#create function to sign a message
def sign_message(prv_key,message):
    hash = SHA256.new(message) #hash the message
    signer = pkcs1_15.new(prv_key)
    Signature=signer.sign(hash) #signing the message
    return Signature

#create function to verify the message
def verify(message , pub_key , Signature):
    hash = SHA256.new(message) #hash a message to check
    try:
        pkcs1_15.new(public_key).verify(hash,Signature) #check a message with Signature
        print("the message was signed")
    except (ValueError , TypeError):
        print("the message was't signed")

#recive a message from user to sign it
inputmessage=input("send your message:")
inputmessage_bytes=bytes(inputmessage,'utf-8') #convert inputmessage to bytes
signedmessage = sign_message(private_key,inputmessage_bytes) #call sign_message to sign the message
verify(inputmessage_bytes,public_key,signedmessage) #verify the message was signed successfuly

# test with fake message
verify(b'fake massage',public_key,signedmessage)
verify(b'100',public_key,signedmessage)
