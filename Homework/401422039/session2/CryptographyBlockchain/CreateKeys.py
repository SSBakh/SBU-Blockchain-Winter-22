from CryptographyBlockchain.keys import PrivateKey,PublicKey
def Create_keys():
    private_k=PrivateKey.create_private_key()
    pem_private=PrivateKey.private_key_to_PEM(private_k)
    pem_public=PublicKey.Create_public_key(private_k)
    return pem_private,pem_public
