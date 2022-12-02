import unittest
from block import Block


class Q02TestCase(unittest.TestCase):

    def test_mine(self):
        block_id = 1
        data = 'test'

        block = Block(block_id, data)
        block.mine()

        self.assertEqual(block.hash, '000062fcc42fc8cdeda00b882b9409fc9d2a013b6dcbf0f83a646b353b243760')
        self.assertEqual(block.nounce, 156384)


if __name__ == '__main__':
    unittest.main()
