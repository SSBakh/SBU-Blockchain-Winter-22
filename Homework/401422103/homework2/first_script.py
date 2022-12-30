import random
import string
import os

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# creating global variables as global
pr = None
pu = None
message = None
signature = None


def random_text(length):  # random text generator and convert it to bytes
    global message
    message = ''.join(random.choice(string.ascii_letters) for i in range(length)).encode()


def rsa_key_generator():
    global pr, pu
    pr = rsa.generate_private_key(public_exponent=65537, key_size=2048)  # Generating Private Key
    pu = pr.public_key()  # Generating Public Key
    return True


def signer():  # Signs The Message With Private Key. Both Message And Private Key are Global.
    return pr.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


def signature_validator():  # Verifies The Signature.
    global pu, message, signature
    if pu is None:
        print("You Have Not Generated A Private/ Public Key Pair Yet!!")
        return 0
    if message is None:
        print("you Don't Have A message!")
        return 0
    try:
        pu.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignature:
        return 1
    return 2


def option_a():  # Just Making Options Neat.
    os.system('cls')
    rsa_key_generator()
    # result = rsa_key_generator()  # Generate keys
    # pr = result[0]  # Private Key Holder
    # pu = result[1]  # Public Key Holder
    print("The Private/Public Key Pair Has Been Generated(!) And Stored!!")
    print("If You Want To See Them Type Yes or Else Type Anything you Want")
    temp_ans = input().lower()
    if temp_ans == 'yes':
        print(f"Your Private Key is {pr}")
        print(f"Your Public Key is {pu}")
    return True


def option_b():  # Just Making Options Neat.
    global message, pr, signature
    os.system('cls')
    print("We Will Create A Random Message Of 20 Characters.")
    print("If You Want To Write your Own Message Type Yes or Else Type Anything: ")
    temp_ans = input().lower()
    if temp_ans == 'yes':
        print("Type It: ")
        message = input().encode()
    else:
        random_text(20)
    print(f'The Message Is "{message}"')
    if pr is None:
        print("You Have Not Generated A Private/ Public Key Pair Yet!!")
        return False
    signature = signer()
    print("The Message Has Been Singed!")
    print("If You Want To See It Type Yes or Else Type Anything you Want")
    temp_ans = input().lower()
    if temp_ans == 'yes':
        print(f"Your Signature is {signature}")
    return True


while True:  # Creating a Simple Cute Interface For Ease of Use.
    print("what Do You Want To Do?")
    print("A. Generate A Private/Public Key Pair")
    print("B. Sign a Message With The Private Key")
    print("C. Check The Signature")
    print("D. Exit!")

    ans = input().lower()
    if ans == 'a':
        re = option_a()
        if re:
            pass
        else:
            print("Something Went Wrong!")
    elif ans == 'b':
        re = option_b()
    elif ans == 'c':
        os.system('cls')
        verify_signature = signature_validator()
        if verify_signature == 2:
            print('The Signature is OK.')
        elif verify_signature == 1:
            print('Wrong Signature!')
    elif ans == 'd':
        break
    else:
        os.system('cls')
        print("Wrong Answer. Please Type A or B or C")

