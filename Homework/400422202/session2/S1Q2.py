from cryptography.hazmat.primitives import hashes


class Mine:
    """_summary_

    Returns:
        _type_: _description_
    """
    
    zero_length = 4
    
    def __init__(self, data, block_number, zero_length) -> None:
        self.data = data
        self.block_number =block_number
        self.zero_length = zero_length

    def mining(self, nounce=0):

        digest = hashes.Hash(hashes.SHA256())
        block_number_bytes = bytes(self.block_number, 'utf-8') 
        data_bytes = bytes(self.data, 'utf-8')
        while(True):
            nounce_bytes = bytes(str(nounce), 'utf-8')
            digest.update(block_number_bytes)
            digest.update(data_bytes)
            digest.update(nounce_bytes)
            final_hash_hex = digest.copy().finalize().hex()
            print(final_hash_hex, "," ,nounce)
            if self.verify_hash(final_hash_hex):
                break
            nounce += 1
        return nounce


    def verify_hash(self, input_hash):
        return input_hash[:self.zero_length] == ("0" * self.zero_length)


if __name__ == "__main__":
    block_number = input("enter block_number: ")
    data = input("enter data: ")
    result = Mine.mining(block_number, data)
    print( f"The final nounce is : {result}" )
