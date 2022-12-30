from cryptography_helper import CryptographyHelper

cryptography_helper = CryptographyHelper()
private_key, public_key = cryptography_helper.generate_keys()

message = input('Please enter a message: ')

print('\nResult:')

sign_key = cryptography_helper.sign(private_key, message)
print("Sign key: ", sign_key)

is_valid = cryptography_helper.validate_sign(message, public_key, sign_key)
print("Is valid: ", is_valid)
