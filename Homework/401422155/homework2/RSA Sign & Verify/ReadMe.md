
## Requirements
```
pip install pycryptodome
from Crypto.PublicKey import RSA
from hashlib import sha512
```

### To generate key pair: 
```
key_pair = key_gen()
```

### To Sign a message:
```
sign(message, key_pair.d, key_pair.n)
```

### To Verify a message:
```
verify(message, key_pair.e, key_pair.n, final_sign)
```
