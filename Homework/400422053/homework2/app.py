from functions import key_pair_generator, sign_message, signature_validator, mine

while True:
    print("Welcome to RSA Key Generator/Miner Application, You can choose from the options:")
    print("1) Generate a pair of private/public keys")
    print("2) Sign a message with a private key")
    print("3) Signature validator")
    print("4) Minner")
    print("5) Exit")

    input_choice = input("Enter Choice: ").strip()

    if input_choice == "1":
        pem_private_key, pem_public_key = key_pair_generator()
        print("--------------")
        print("Private Key Hex:")
        print(pem_private_key.hex())
        print("--------------")
        print("Public Key Hex:")
        print(pem_public_key.hex())
        print("--------------")

    elif input_choice == "2":
        print("--------------")
        input_private_key = input("Enter Your Private Key Hex: ").strip()
        input_private_key = bytes.fromhex(input_private_key)
        input_message = input("Enter Your Message: ").strip()
        signature = sign_message(input_private_key, input_message)
        print("Signature Hex: ")
        print(signature.hex())
        print("--------------")

    elif input_choice == "3":
        print("--------------")
        input_message = input("Enter Your Message: ").strip()
        input_public_key = input("Enter Your Public Key Hex: ").strip()
        input_public_key = bytes.fromhex(input_public_key)
        input_signature = input("Enter Your Signature Hex: ").strip()
        input_signature = bytes.fromhex(input_signature)
        isValid = signature_validator(input_message, input_public_key, input_signature)
        if isValid:
            print("Your Signature Is VALID")
        else:
            print("Your Signature Is INVALID")
        print("--------------")

    elif input_choice == "4":
        try:
            print("--------------")
            input_data = input("Enter Your Data (Default = sadra_balance=1000B): ").strip()
            input_block_number = input("Enter Your Block Number (Default = 0): ").strip()
            if int(input_block_number) < 0:
                print("--------------")
                print("Block Number Should Be A Positive Integer!") 
                print("--------------")
                continue 
            generated_hash_hex, nonce = mine(input_data, input_block_number)
            print("--------------")
            print("generated_hash_hex: " + generated_hash_hex)
            print("nonce: " + str(nonce))
            print("--------------")
        except ValueError:
            print("--------------")
            print("Block Number Should Be A Positive Integer!")
            print("--------------")
            
    elif input_choice == "5":
        break
    else:
        print("Invalid Option. Please Try Again!")
