first, ensure you install the pycryptodomex  / cryptography module 
Let’s explain what is happening here:
1.	We do the usual imports to generate our RSA public/private certificate pair but this time we include an extra method PKCS1_OAEP which will be used to create the cipher object to encrypt our plaintext with the key -+that is in the certificate.
2.	We generate our public and private RSA certificates to disk as public_key.pem and private_key.pem respectively, as usual. These certificates contain our keys. Recall that a key is simply a string of text.
3.	We define the message to be encrypted in bytes as message. This message will be encrypted with the public key certificate public_key.pem as per the RSA algorithm. Ideally, the public certificate should be publicly available and the private certificate should be kept private.
4.	The RSA.import_key() method will import the public key to be used to encrypt, from the certificate on disk. We define the public key as parameter extern_key which is the RSA key to import. It will return an RSA key object key.
5.	The method PKCS1_OAEP.new() will accept the RSA key object as parameter key and return a cipher object of type PKCS1OAEP_Cipher that can be used to do the actual encryption or decryption of the data. The return value is stored as cipher.
6.	The method cipher.encrypt() takes one parameter message and it will actually encrypt it using the key previously specified. It will return the encrypted plaintext message as ciphertext.
7.	We simply print the ciphertext to the screen. It will look like gibberish because it is encrypted.
If all goes well, the code above will produce two new files on disk in the same folder as the script: public_key.pem and private_key.pem. 
 now we want to decrypt the message using our private key. Only someone who has access to the private key certificate that corresponds to the public key certificate used to encrypt the message, can decrypt it
What we are doing here is simply the reverse of the encryption process. The difference is that we are importing the private key from the private certificate. Also, we are using the cipher.decrypt() method, to decrypt the ciphertext. 
If all goes well, the plaintext should be exactly what the original message was. 
