import json

from cryptography.hazmat.primitives import hashes

NUM = 1
DATA = 'Hello World'
FROM_NONCE = 0
REQUIRED_DOUBLE_ZEROS = 2


class Block:
    def __init__(self, num: int, data: str, nonce: int):
        self.__num = num
        self.__data = data
        self.nonce = nonce

    def hash(self) -> bytes:
        data = json.dumps(self.dict()).encode('utf-8')
        digest = hashes.Hash(hashes.SHA256())
        digest.update(data)
        return digest.finalize()

    def dict(self) -> dict:
        return {
            'num': self.__num,
            'data': self.__data,
            'nonce': self.nonce,
        }


def mine(block: Block):
    while not block.hash().startswith(bytes.fromhex('0' * (2 * REQUIRED_DOUBLE_ZEROS))):
        block.nonce += 1


def main():
    block = Block(num=NUM, data=DATA, nonce=FROM_NONCE)
    mine(block)
    print(block.nonce)
    print(block.hash().hex())


main()
