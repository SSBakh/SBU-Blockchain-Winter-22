# Homework 2

Homework 2 has two section:

in section 1 there are three function

- generate private/public key with res algorithm.
- sign a message with a private key
- verify a signature with public key and message

In section 2 there is a class for block mining

## section 1

- generating private/public keys:
  this function generates a pair of public/private key with rsa and save them in keys folder
- sign a message:
  this function gives a private key file path and a message. Then sign the message with the that key. The signature is saved in sign folder.
- verify a signature:
    this function give a signature file path and public key file path and a message. Then verify that the message is signed with that signature or not

## section 2
- mining block
    this class has two method:
    - mining 
        this method gives data and block number and then calculate the minimum nounce that match zero numbers in data's hash.
    - verify_hash
        this method gives a hash and a number for zero quantity then verify that the hash has zero condition or not.

# Demo
   With this file we can test out functions in section 1.
   Also mine a block and recive a nounc in section 2