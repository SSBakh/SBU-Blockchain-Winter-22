import rsa
import base64

# private = rsa.PrivateKey(
#     int(input('enter your public key n\n')), 
#     int(input('enter your public key e\n')),
#     int(input('enter your public key d\n')),
#     int(input('enter your public key p\n')),
#     int(input('enter your public key q\n')))
# message = input('enter message to decrypt\n')


private = rsa.PrivateKey(
    241501871587765675465776746087674408421, 
    65537,
    170385637708090228290350384852892395561,
    230838663567051692903,
    1046193336315242707)
message = 'qbYWUicCuMpJWWwJ+7SkPA=='

ciphertext = rsa.decrypt(base64.b64decode(message),private)

print(ciphertext)
print("\n\n")
