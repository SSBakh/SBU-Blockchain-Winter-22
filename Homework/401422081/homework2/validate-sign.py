import rsa
import base64

publicKey = rsa.PublicKey(
    int(input('enter your public key n\n')), 
    int(input('enter your public key e\n')))

message = input('enter message\n')
signature = input('enter message sign\n')

signature += "=" * ((4 - len(signature) % 4) % 4)
result = rsa.verify(message.encode(), base64.b64decode(signature), publicKey)

print('result: ' + result)
print("\n\n")
