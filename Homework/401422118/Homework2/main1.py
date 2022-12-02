from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

def GeneratePairKeys():
    PrivateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    PublicKey = PrivateKey.public_key()

    with open("public.pem", "w") as Public:
        PublicSerialized = PublicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        Public.write(PublicSerialized.decode())
    with open("private.pem", "w") as Private:
        PrivateSerialized = PrivateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        Private.write(PrivateSerialized.decode())
    return "Save Private/Public Keys"

def SignMessage(PrivateKey, Message):
    with open(f"{PrivateKey}", "rb") as KeyFile:
        LoadedPrivateKey = serialization.load_pem_private_key(
            KeyFile.read(),
            password=None,
            )
    with open("sign", "wb") as Sign:
        Sign.write(LoadedPrivateKey.sign(
        Message.encode(),        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    ))

    return "Save Signature File"

def VerifySignMessage(Message, PublicKey, Signature):
    try:
        with open(f"{PublicKey}", "rb") as KeyFile:
            public_key_loaded = serialization.load_pem_public_key(
            KeyFile.read(),
        )

        with open(f"{Signature}", "rb") as SignFile:
            sign = SignFile.read()

        try:
            public_key_loaded.verify(
                sign,
                Message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return ("Verified")
        except Exception:
            return("Not verified")
    except Exception as Error:
        return("ERROR: ",Error)

#Test Runnig
if __name__ == "__main__":
    print(GeneratePairKeys())
    print(SignMessage("private.pem", "Hello World"))
    print(VerifySignMessage("Hello World", "public.pem", "sign"))
