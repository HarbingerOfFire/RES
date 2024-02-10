# RES: Randomized Encryption Standard

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

RES is a simple symmetric key encryption algorithm designed to encrypt using randomization. It uses a [hashing algorithm](https://github.com/harbingeroffire/SXH) to generate random numbers from the input key. Then it goes through 3 stages of ciphers before before using key block encryption. This algorithm uses 128, 256, and 512 char blocksizes

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Other Notes](#other-notes)
- [Examples](#examples)
- [License](#license)

## Installation
This code is available on PyPI under the name `REScrypt`:
```bash
pip install REScrypt
```

## USAGE
Example For encrypting and decrypting using RES:
```python
import RES

cipher=RES.Cipher("RES-128", b"key")

ciphertext=cipher.encrypt(b"buffer")
plaintext=cipher.decrypt(ciphertext)

print("Encrypted: ",ciphertext)
print("Decrypted: ",plaintext)
```

## Other Notes
The code also has a built in function to encrypt and decrypt files using `fencrypt()` and `fdecrypt()` as well as outputing the encryption in hexadecimal using `hencrypt()` and `hdecrypt()`. Conviently I also combined them to encrypt and decrypt files with hexadecimal with `hfencrypt()` and `hfdecrypt()`.

## License
[MIT License](https://opensource.org/license/mit/), you all know what that is.

