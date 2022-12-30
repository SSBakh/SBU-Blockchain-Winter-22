import rsa
import base64

publicKey = rsa.PublicKey(
    int(input('enter your public key n\n')), 
    int(input('enter your public key e\n')))

message = input('enter message to encrypt\n')

ciphertext = rsa.encrypt(message.encode(),publicKey)
cypherString = str(base64.b64encode(ciphertext),'utf-8')

print(cypherString)
print("\n\n")
