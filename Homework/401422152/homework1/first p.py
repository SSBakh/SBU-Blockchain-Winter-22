pip install pycryptodomex
pip install cryptography
import cryptography as Crpyto
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

############G##############GENERATE CERTIFICATE PAIR########################

new_key = RSA.generate(2048)

private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

################ENCRYPT/DECRYPT DATA WITH CERTIFICATE#######################

message = b'CODE EVERYDAY TO GET BETTER'

key = RSA.import_key(open('public_key.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
print(ciphertext)
print("\n\n")


key = RSA.import_key(open('private_key.pem').read())
cipher = PKCS1_OAEP.new(key)
plaintext = cipher.decrypt(ciphertext)
print (plaintext.decode("utf-8"))
