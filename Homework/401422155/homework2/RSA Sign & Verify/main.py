from Crypto.PublicKey import RSA
from hashlib import sha512


def key_gen(key_len=1024):
    """
    RSA generating a keypair
    n (integer) RSA modulus
    e (integer) RSA public exponent
    d (integer) RSA private exponent
    p (integer) First factor of the RSA modulus
    q (integer) Second factor of the RSA modulus
    u (integer) Chinese remainder component (p-1 mod q)
    :param key_len: int , number of bits of the RSA Keys
    :return: an RSA key object (RSAKey, with private key)
    """
    keyPair = RSA.generate(bits=key_len)
    return keyPair


def sign(msg,k_d,k_n):    
    """
    RSA signing
    :param msg: bytes , the message you want to sign in bytes
    :param k_d: int , RSA private exponent
    :param k_n: int , RSA modulus
    :return: <class 'int'> , sign the msg with private key
    """
    
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    signature = pow(hash, k_d, k_n)
    return signature


def verify(msg,k_e,k_n,signature):
    """
    RSA Verification
    :param msg: bytes , the message you want to verify in bytes
    :param k_e: int , RSA public exponent
    :param k_n: int , RSA modulus
    """
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    hashFromSignature = pow(signature, k_e, k_n)
    return hash == hashFromSignature

# ______________________________

message = b'This is a message for signing'
key_pair = key_gen()
final_sign = sign(message, key_pair.d, key_pair.n)
print(verify(message, key_pair.e, key_pair.n, final_sign))
