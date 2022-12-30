# Blockchain Course |  Assignment 2 #


# RSA 
RSA means Rivest, Shamir, Adleman. These are the inventors of the popular RSA Algorithm. The RSA algorithm is based on public-key encryption technology which is a public-key cryptosystem for reliable data transmission.  
Run `RSA.py` :

## 1. Generating keys  
generate public and private keys and save them in your dir in pem format.  

## 2. Signing a message with your private key  
example input :   
- *PrivateKey.pem*  
- *this is a test message*  
        
example output :  *signiture in hex*  
*3760b966e5b4d3c00a04a14668fc45c4cb01ef7dab1712b59d09ef75bf6ab2493143e90f6ac4b2f004eb550a5eedba916510c5f1253458e73a705ceb4d2dea722251e35b9d9f0af9374e7ea4537cc28a57914811dd5b1acef3723c228d5b646382815f0c062257b231f97b27b68822ee404ce8301ec973eebbfb769884b2151e*  



## 3. Verifying your message with your public key and signiture 

example input :

- *this is a test message*  
- *PublicKey.pem*  
- *3760b966e5b4d3c00a04a14668fc45c4cb01ef7dab1712b59d09ef75bf6ab2493143e90f6ac4b2f004eb550a5eedba916510c5f1253458e73a705ceb4d2dea722251e35b9d9f0af9374e7ea4537cc28a57914811dd5b1acef3723c228d5b646382815f0c062257b231f97b27b68822ee404ce8301ec973eebbfb769884b2151e*
       
example output : *Signature verified!*  


# Mining
Mining generally refers to solving a computationally tough mathematical puzzle. Mining is achieved by finding the correct hash which has a preset number of zeros in the beginning and it also signifies the difficulty level.  
Run `Mining.py`:

example output:  
*Block mined with nonce value : 17526*  
*Hash value :  000097b24c02ae2fe449f459a2be1626c484d66c7fe363427caf063ed38763c7*  
*The mining process took  1.3758361339569092 seconds*   







# Note
The requirements.txt file should list all Python libraries that these notebooks depend on, and they will be installed using:  
```
pip install -r requirements.txt
```

