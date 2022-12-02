import unittest

from main import generate_key_pair, sign, verify, mine_block


class TestSum(unittest.TestCase):

    def test_generate_key_pair(self):
        secret = 'secrettt'
        private_key, public_key = generate_key_pair(secret)
        self.assertTrue("-----BEGIN ENCRYPTED PRIVATE KEY-----" in private_key.decode("utf-8"))
        self.assertTrue("-----BEGIN PUBLIC KEY-----" in public_key.decode("utf-8"))

    def test_sign_and_verify(self):
        secret = 'secret'
        private_key, public_key = generate_key_pair(secret)
        plain_text = "I'm a plain text, sign me if you can haahaa"
        signed = sign(private_key, secret, plain_text)
        self.assertIsNotNone(signed)
        is_sign_valid = verify(public_key, plain_text, signed)
        self.assertTrue(is_sign_valid)

    def test_sign_and_verify_fail_scenario(self):
        # We sign with private key but try to validate it with another public key
        secret = 'secret'
        private_key, _ = generate_key_pair(secret)
        plain_text = "I'm a plain text, sign me if you can haahaa"
        signed = sign(private_key, secret, plain_text)
        self.assertIsNotNone(signed)
        _, another_public_key = generate_key_pair(secret)
        is_sign_valid = verify(another_public_key, plain_text, signed)
        self.assertFalse(is_sign_valid)

    def test_mine_block(self):
        block_hash, nonce = mine_block('Block data', 231)
        self.assertEqual(nonce, 43809)
        self.assertTrue(block_hash.startswith("0000"))


if __name__ == '__main__':
    unittest.main()
