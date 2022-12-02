from S1Q1 import *
from S1Q2 import *

while(True):
    test_number = int(input(
        """
    select the test function: 
    1 --> generate rsa public key
    2 --> signing message
    3 --> verify signature
    4 --> mining block
    """
    ))
    if test_number not in [1, 2, 3, 4]:
        print("the number is not valid")
        break

    if test_number == 1:
        result = generate_public_key()

    elif test_number == 2:
        private_key = input("insert private_key file path: ")
        message = input("insert message : ")
        result = sign_message(private_key, message)

    elif test_number == 3:
        public_key = input("insert public key file path : ")
        message = input("insert message : ")
        signature = input("insert signature : ")
        result = verify_sign(message, public_key, signature)
    
    elif test_number == 4:
        data = input("insert block data : ")
        block_number = input("insert block number: ")
        zero_length = int(input("how many zero in fist of data hash ? "))
        mine = Mine(data, block_number, zero_length)
        nounce = mine.mining()
        result = (f"The minimum nounce is {nounce} for mining the block")

    print("*"*50)
    print(result)
    print("*"*50)

    cont = input("Do you want to continue : Y/N ")
    if cont.lower() != 'y':
        print("Thank you")
        break
