# Description

1. 
>  Generate Private key and Publick key with RSA algorithm.
>  
>  Sign a message with the private key.
>  
>  Verify a signature using a message, public key, and signature.
2. 
> Mining a block that contains block number, data (as string), and nonce.
> 
> Hash block must start with 4 zeros at the beginning.

# How it works!

just open it in *Colab* or *Jupyter Notebook* and run it :),  all the parts are seprated. You can also check the output without running it.

- All the parts are based on [Cryptography library manual](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa)
- Save and loading the keys are optional.
- In the mining part, I define a `difficulty` variable, which means the number of zeros at the beginning of the target hash.

# Dependencies

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads)
[![https://pypi.org/project/cryptography/](https://img.shields.io/pypi/v/cryptography)](https://pypi.org/project/cryptography/)
[![https://cryptography.io/en/latest/](https://img.shields.io/readthedocs/cryptography)](https://cryptography.io/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

Install [Cryptography](https://pypi.org/project/cryptography/) by using [pip](https://pip.pypa.io/en/stable/cli/pip_install/), `pip install cryptography` or `!pip install cryptography` in Colab.

