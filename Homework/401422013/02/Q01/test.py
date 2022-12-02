import unittest
from cryptography_helper import CryptographyHelper


class Q01TestCase(unittest.TestCase):

    def test_keys_not_none(self):
        private_key, public_key = CryptographyHelper().generate_keys()
        self.assertIsNotNone(private_key, "must not be none")
        self.assertIsNotNone(public_key, "must not be none")

    def test_sign_message_not_none(self):
        cryptography_helper = CryptographyHelper()
        message = 'test'

        private_key, public_key = cryptography_helper.generate_keys()
        sign_key = cryptography_helper.sign(private_key, message)

        self.assertIsNotNone(sign_key, "must not be none")

    def test_sign_and_validate_message(self):
        cryptography_helper = CryptographyHelper()
        message = 'test'

        private_key, public_key = cryptography_helper.generate_keys()
        sign_key = cryptography_helper.sign(private_key, message)

        is_valid = cryptography_helper.validate_sign(message, public_key, sign_key)

        self.assertEqual(is_valid, True)


if __name__ == '__main__':
    unittest.main()
