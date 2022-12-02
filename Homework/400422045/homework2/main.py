# Import Block and Crypto Classes
import Block
import Crypto

# While loop for a menu
# If you enter 1 generate RSA key pair
# If you enter 2 Sign a text with private key
# If you enter 3 Verify message and signature
# If you enter 4 Mine single block
# If you enter 0 exit
while True:
    inp = int(input("""    1. Generate RSA key pair
    2. Sign a text with private key
    3. Verify message and signature
    4. Mine single block
    0. exit """))
    if inp == 1:
        Crypto.Crypto().generateRsaKeys()
    if inp == 2:
        private_key = input('Enter your private key file name: ')
        message = input('Enter your message: ')
        print(Crypto.Crypto().signing(private_key, message))
    if inp == 3:
        public_key = input('Enter your public key file name: ')
        message = input('Enter your message: ')
        signature = input('Enter your signature: ')
        Crypto.Crypto().verify(message, public_key, signature)
    if inp == 4:
        block = input("Enter block number: ")
        data = input("Enter data: ")
        mined = Block.Block().mine(block, data)
        print(f"Nonce is: {mined['nonce']}\nHash is {mined['hash']}")
    if inp == 0:
        break

