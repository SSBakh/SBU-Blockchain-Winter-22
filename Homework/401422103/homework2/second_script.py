import random
import string
import os
from cryptography.hazmat.primitives import hashes
import hashlib

block = random.randint(0, 1024)
message = None
nonce = 0
found = 0


def random_text(length):  # random text generator and convert it to bytes
    global message
    message = ''.join(random.choice(string.ascii_letters) for i in range(length))


def hashlib_method():
    global block, message, nonce
    while True:
        z = str(block) + message + str(nonce)
        new_hash = hashlib.sha256(z.encode()).hexdigest()
        if new_hash[:4] == '0000':
            print(f'The Nonce is {nonce} and The Hash is {new_hash}')
            return
        nonce += 1


def cryptography_method():
    global block, message, nonce
    while True:
        data = str(block) + message + str(nonce)
        bdata = data.encode()
        digest = hashes.Hash(hashes.SHA256())
        digest.update(bdata)
        res = str(digest)
        if res[:4] == '0000':
            digest.finalize()
            print(nonce)
            return
        nonce += 1


while True:
    random_text(20)
    print("Which Library Do You Want? ")
    print("A: hashlib (Works Really Fast.)")
    print("B: Cryptography (For Gods Sake, This Library Takes Too Long And I Never Reached The Goal, TO Be Honest. "
          "Please Don't Choose This")
    print("C: Exit!")
    temp_ans = input().lower()
    if temp_ans == 'a':
        os.system('cls')
        hashlib_method()
    elif temp_ans == 'b':
        os.system('cls')
        cryptography_method()
    elif temp_ans == 'c':
        break
    else:
        os.system('cls')
        print("Wrong Input")
