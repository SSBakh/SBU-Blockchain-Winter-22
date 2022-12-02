"""
This module consists of "MyRSA" class.
(In correspondance with the "RSA public/private key + sign + verify" exercise)

Classes
-------

MyRSA:
   A class to represent a public-key scheme.
"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class MyRSA():
    
    """
    A class to represent a public-key scheme.

    ...

    Attributes
    ----------
    public_exponent : int
        More details on https://en.wikipedia.org/wiki/RSA_(cryptosystem)
    key_size : int
        More details on https://en.wikipedia.org/wiki/RSA_(cryptosystem)
    private_key : obj from RSAPrivateKey class
        More details on https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
    public_key : obj from RSAPublicKey class
        More details on https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
    private_bytes: bytes
        More details on https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
    public_bytes: bytes
        More details on https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
    signaure: bytes
        More details on https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

    Methods
    -------
    print_private_key():
        Prints the private key in PEM format.
    print_public_key():
        Prints the public key in PEM format.
    sign(message):
        Signs a message using the private key. Returns the signature.
    verify(message):
        Checks if the right message is signed with the right private key,using the public key. Returns True/False respectively.
    """
    
    def __init__(self,public_exponent=65537,key_size=2048):

        """
        Constructs all the necessary attributes for an RSA scheme.

        Parameters
        ----------
        public_exponent : int, optional
            More details on https://en.wikipedia.org/wiki/RSA_(cryptosystem), by default 65537
        key_size : int, optional
            More details on https://en.wikipedia.org/wiki/RSA_(cryptosystem), by default 2048
        """

        self.public_exponent = public_exponent
        self.key_size = key_size
        self.private_key = rsa.generate_private_key(self.public_exponent,self.key_size,backend=default_backend())
        self.public_key = self.private_key.public_key()
        

    def print_private_key(self):
        """
        Prints the private key in PEM format.
        """
        self.private_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        print(self.private_bytes)


    def print_public_key(self):
        """
        Prints the public key in PEM format.
        """
        self.public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        print(self.public_bytes)


    def sign(self , message : str) -> bytes:

        """
        Signs a message using the private key.

        Parameters
        ----------
        message : str
            Raw message

        Returns
        -------
        bytes
            Returns the signature.
        """

        self.signature = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return self.signature


    def verify(self , message : str) -> bool:

        """
        Checks if the right message is signed with the right private key,using the public key. 

        Parameters
        ----------
        message : str
            Raw message

        Returns
        -------
        bool
            Returns True/False respectively.
        """
        try:
            self.public_key.verify(
            self.signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        except:
            return False
        
        else:
            return True
        
