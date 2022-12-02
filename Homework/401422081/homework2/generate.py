import rsa

publicKey, privateKey = rsa.newkeys(2048)

print(publicKey)
print(privateKey)
