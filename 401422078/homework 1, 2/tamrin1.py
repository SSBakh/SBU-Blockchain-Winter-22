# neccessary imports 
from Crypto.PublicKey import RSA  # we will use this module for create public and private key 
from Crypto.Hash import SHA512, SHA256 # when i read document, i found that there is different algorithm hashing 
from Crypto import Random # we will use this module in generating public and private key
from Crypto.Cipher import PKCS1_OAEP # we will use this module for encrypting 
from Crypto.Signature import PKCS1_v1_5 # we will use this module for creaing signer based on privatekey



# we will use below function for generating private and random key 
def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   private, public = key, key.publickey()
   return public, private


# we will use below function for passing private_key and then getting pair public key 
def getpublickey(priv_key):
   return priv_key.publickey()


# we will use below function for encryption input message with public key 
def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)
 
 
# we will use below function for decryption input cipher with private key
def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

hash = "SHA-256" # our global variable that we use it in sign and verify function 

# we will use below function for signing input message with private key and selected hash algorithms 
def sign(message, priv_key, hashAlg = "SHA-256"):
   global hash # our default algorithm 

   hash = hashAlg
   signer = PKCS1_v1_5.new(priv_key)
   
   if (hash == "SHA-512"):
      digest = SHA512.new()
   elif (hash == "SHA-256"):
      digest = SHA256.new()
   else:
      pass
   digest.update(message)
   return signer.sign(digest)
 
 
# we will use below function for for checking validation of signature with input message and public_key and sinature
def verify(message, signature, pub_key):
   signer = PKCS1_v1_5.new(pub_key)
   if (hash == "SHA-512"):
      digest = SHA512.new()
   elif (hash == "SHA-256"):
      digest = SHA256.new()
   else:
      pass
   digest.update(message)
   return signer.verify(digest, signature)
 

# our tests ...

print('''
                                                  ###############
                                                  ### test1  ###
                                                  #############
                                                  ''')
# create first private key and public key and check methods of encryption and decryption and signing and verifying 
print("-----------------------------------------------------------------------------------------------------")
print("generating public and private key ... ")
public_sample, private_sample = newkeys(1024)
print(f"after calling newkeys(), public key and private key is : \n {public_sample} \n {private_sample}")
print("-----------------------------------------------------------------------------------------------------")
# this is our text for testing 
text = b"this is a test1"

print(f"generating cipher text ... for text {text} ")
cipher_text = encrypt(text, public_sample)
print(f"after calling encrypt(), cipher text is : \n {cipher_text} ")
print("-----------------------------------------------------------------------------------------------------")
print("decrypting cipher text ... ")
decrypt_text = decrypt(cipher_text, private_sample)
print (f"after calling decrypt(), decrypt message is : \n {decrypt_text}")
print("-----------------------------------------------------------------------------------------------------")
print("getting signature of message with private key ...")
signature_sample = sign(text, private_sample)
print(f"after calling sign() function, signature is : \n {signature_sample}")
print("-----------------------------------------------------------------------------------------------------")
print("we verify the validation of signature .... ")
bool = verify(text, signature_sample, public_sample) # because we used 2 same sgnature and pulic key, the result must be true
print(f"verification is : \n {bool}")
print("-----------------------------------------------------------------------------------------------------")



print('''
                                                  ###############
                                                  ### test2  ###
                                                  #############
                                                  ''')
# create other public key and private key
print("-----------------------------------------------------------------------------------------------------")
print("generating public and private key ... ")
public_sample2, private_sample2 = newkeys(1024)
print(f"after calling newkeys(), public key and private key is : \n {public_sample} \n {private_sample}")
print("-----------------------------------------------------------------------------------------------------")
# this is our text for testing 
text2 = b"this is a test2"
print("-----------------------------------------------------------------------------------------------------")
print("getting signature of message with private key ...")
signature_sample2 = sign(text2, private_sample2)
print(f"after calling sign() function, signature is : \n {signature_sample2}")
print("-----------------------------------------------------------------------------------------------------")
print("we verify the validation of signature .... ")
bool2 = verify(text2, signature_sample2, public_sample2) # because we used 2 same sgnature and pulic key, the result must be true
print(f"verification is : \n {bool2}")
print("-----------------------------------------------------------------------------------------------------")


print('''
                                                  ###############
                                                  ### test3  ###
                                                  #############
                                                  ''')
# test different publickey and signature that comes from "test1" and "test2" and check sign method 
print("we verify the validation of signature and it's message with other public_sample! ")
bool3 = verify(text2, signature_sample2, public_sample) # because we used 2 different sgnature and pulic key, the result must be false
print(f"verification is : \n {bool3}")
print("-----------------------------------------------------------------------------------------------------")

