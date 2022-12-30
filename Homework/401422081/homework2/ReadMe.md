This homework contains 6 files that I explain what each do. I used sha256, json, time, rsa, base64 libraries. I used python 3 for this project and I think these libraries are from python3 standard libraries and cryptography library.

generate.py 
This file generates keys. Using these keys I did the rest. It is good to mention that I used 2048 key to be able to sign with it as I got errors with shorter keys.

decrypt.py encrypt.py
These files encrypt and decrypt using public key and private key. I wrote these files for my own better understanding.

sign.py
This file gets a text input and signs it using private key. Private key in this file is hard coded as it was hard to enter it each time. :)

validate.py
This file gets public key and message and message signatures and validates if the key owner signed this message. If it was invalid you will get a python error and if it gets successful you will get a "result: MD5" output.

block.py
This file contains codes simulating a block. To get a hash starting with "0000" I created a loop with increasing nonce to get a hash like that. Then after creating the block I reset the none and created a funcion named "mine" to check nonce from zero to result to mine the block and find matching hash with proper nonce.

Thank you for your time
