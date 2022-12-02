import rsa
########## functions #############

def generate_keys(): # generate private and public key with rsa method and save them in pem format
    (pubKey, privKey) = rsa.newkeys(1024)
    with open('pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))


def load_prv_key(): # load the keys from the files
    with open(privKeyu , 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return privKey  

def load_pub_key(): # load the keys from the files
    with open(pubKeyu , 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    return pubKey  




def sign_sha1(msg, key): # rsa.sign(message: bytes, priv_key: rsa.key.PrivateKey, hash_method: str) → bytes
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

def verify_sha1(msg, signature, key): # rsa.verify(message: bytes, signature: bytes, pub_key: rsa.key.PublicKey) → str
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False



######################### app ###########################

while(1):
    user=int(input('''
        enter:
        1:Generating keys
        2:Signing a message with your private key
        3:Verifying your message with your public key and signiture
        0:exit
    '''))
    if user==1:
        generate_keys()
        print("they keys are saved in your dir")
    if user==2:
        privKeyu = input('enter ur private key file name(e.g. example.pem):')
        message = input('Enter a message:')
        privKey = load_prv_key()
        ###
        signature = sign_sha1(message, privKey)
        print(f'Signature: {signature}')
        print(signature.hex())

    if user==3:
        message = input('Enter a message:')
        pubKeyu = input('enter ur public key file name(e.g. example.pem):')
        signature_u=input('enter your signature in hex:')
        signature_u = bytes.fromhex(signature_u)
        pubKey = load_pub_key()
        ###
        if verify_sha1(message , signature_u, pubKey):
            print('Signature verified!')
        else:
            print('Could not verify the message signature.')
            
    if user=='exit':
        break





