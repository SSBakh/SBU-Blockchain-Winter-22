"""
This module consists of "Block" class.
(In correspondance with the "block mining" exercise)

Classes
-------

Block:
   A class to represent a block 
"""

from cryptography.hazmat.primitives import hashes


class Block():

    """
    A class to represent a block

    ...

    Attributes
    ----------
    blocknumber : bytes
        The block number
    data : bytes
        Data field in the block
    nonce : bytes
        The number by which we are willing to mine the block
    digest : obj from hashes.Hash class
        Object from hashes.Hash class
    finalhash: str
        Hash of the block(blocknumber + nonce + data)

    Methods
    -------
    blockdigestfunction():
        Hashes the entire block based upon SHA256.

    mine():
        Computes the nonce by which the block's digest starts with "0000"
        Returns the nonce.
    """

    def __init__(self,blocknumber:int ,data:str ,nonce:int = 0):
        
        """
        Constructs all the necessary attributes for the block object.

        Parameters
        ----------
        blocknumber : int
            The block number
        data : str
            Data field in the block
        nonce : int
            The number by which we are willing to mine the block
        """

        self.blocknumber = bytes(str(blocknumber),encoding='utf-8')
        self.data = bytes(str(data),encoding='utf-8')
        self.nonce = bytes(str(nonce),encoding='utf-8')


    def blockdigestfunction(self) -> str:

        """
        Hashes the entire block based upon SHA256.

        Parameters
        ----------
        None

        Returns
        -------
        finalhash : str
            Hash of the block(blocknumber + nonce + data)
        """

        self.digest = hashes.Hash(hashes.SHA256())
        self.digest.update(self.blocknumber)
        self.digest.update(self.nonce)
        self.digest.update(self.data)
        self.finalhash = self.digest.finalize().hex()
        return self.finalhash


    def mine(self) -> bytes:

        """
        Computes the nonce by which the block's digest starts with "0000"

        Parameters
        ----------
        None

        Returns
        -------
        nonce : bytes
            The number by which we are were able to complete the mining,resulting in a hash starting with "0000"
  
        """

        self.blockdigestfunction()

        while str(self.finalhash)[0:4] != "0000" :
            self.nonce = bytes(str(int(self.nonce) + 1),encoding = 'utf-8')
            self.blockdigestfunction()

        return self.nonce