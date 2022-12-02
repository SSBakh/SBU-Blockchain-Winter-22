from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

def generate_public_key():
    """ This function save a rsa pair public/private key in two seperate file.
    Returns:
        str: Generation alert
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    private_serialized = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_serialized = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("keys/pu.pem", "w") as public:
        public.write(public_serialized.decode())
    with open("keys/pr.pem", "w") as private:
        private.write(private_serialized.decode())
    
    return "The keys has been generated and save in files"


def sign_message(private_key, message):
    """ This function receives a message with a rsa private key file and sign the message with that key. 

    Args:
        private_key (str): the private key **file path**
        message (str): The message 

    Returns:
        str: the signing status
    """
    try:
        
        with open(f"{private_key}", "rb") as key_file:
            private_key_loaded = serialization.load_pem_private_key(
                key_file.read(),
                password=None,

            )
        signature = private_key_loaded.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        with open("sign/si", "wb") as sign:
            sign.write(signature)
            
        return "The Signature has been done and save in signature file"
    except Exception:
        return "The Signature has been failed"


def verify_sign(message, public_key, signature):
    """ This function receives a message, a public key file and a signature and verifeis
        that the signature is verified or not

    Args:
        message (str): the message
        public_key (str): the public key **file path**
        signature (str): the signature **file path**

    Returns:
        str: the verification result
    """
    try:
        with open(f"{public_key}", "rb") as key_file:
            public_key_loaded = serialization.load_pem_public_key(
            key_file.read(),
        )
            
        with open(f"{signature}", "rb") as sign_file:
            sign = sign_file.read()

        try:
            public_key_loaded.verify(
                sign,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return ("Signature is verified")
        except Exception:
            return("Signature is not verified")
    except Exception as e:
        return("Verification has problem : ", e)
        