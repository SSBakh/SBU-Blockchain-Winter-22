from Modules.Homemadersa import * 

# At first let's instantiate an object from the "MyRSA" class using its constructor.
rsa1 = MyRSA()

rsa1.print_private_key()
rsa1.print_public_key()

message = b"This is a test message!"

result = rsa1.sign(message)
print(result.hex())

verified_or_not = rsa1.verify(message)
print(verified_or_not)

anothermessage = b"This is another message!"

verified_or_not = rsa1.verify(anothermessage)
print(verified_or_not)



