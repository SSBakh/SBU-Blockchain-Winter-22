from cryptography.hazmat.primitives import hashes


class Block:

    def __init__(self, id, data):
        self.default_hash = hashes.SHA256()
        self.default_encoding = 'utf-8'

        self.id = id
        self.nounce = 0
        self.data = data
        self.hash = ''

    def __str__(self):
        return f"Id: {self.id}\nNounce: {self.nounce}\nData: {self.data}\nHash: {self.hash}"

    def mine(self) -> (str, int):
        while True:
            data = f"{self.id}{self.nounce}{self.data}"
            data_bytes = bytes(data, self.default_encoding)
            digest = hashes.Hash(self.default_hash)
            digest.update(data_bytes)
            hash_result = digest.finalize().hex()
            if hash_result[:4] == '0000':
                self.hash = hash_result
                break
            else:
                self.nounce += 1

        return self.nounce, self.hash
