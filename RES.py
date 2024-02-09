"""RES: Randomized Encryption Standard"""
import cooc_sc
import shuffle
import grid_cipher
import key_block_cipher
import binascii as hex

class Cipher:
    def __init__(self, algorithm, key):
        self.algorithm=algorithm
        self.key=key

    def encrypt(self, buffer):
        cipher1=cooc_sc.cooc_sc(buffer, self.key).cipher()
        cipher2=shuffle.shuffle(cipher1, self.key).cipher()
        cipher3=grid_cipher.grid_cipher(cipher2, self.key).cipher()
        cipher4=key_block_cipher.key_block_cipher(self.algorithm, cipher3, self.key).cipher()
        return cipher4

    def decrypt(self, buffer):
        cipher4=key_block_cipher.key_block_cipher(self.algorithm, buffer, self.key).decipher()
        cipher3=grid_cipher.grid_cipher(cipher4, self.key).decipher()
        cipher2=shuffle.shuffle(cipher3, self.key).decipher()
        cipher1=cooc_sc.cooc_sc(cipher2, self.key).decipher()
        return cipher1
    
    def fencrypt(self, filename):
        with open(filename, "rb+") as infile:
            ciphertext=self.encrypt(infile.read())
        with open(filename, "wb+") as outfile:
            outfile.write(ciphertext)

    def fdecrypt(self, filename):
        with open(filename, "rb+") as infile:
            plaintext=self.decrypt(infile.read())
        with open(filename, "wb+") as outfile:
            outfile.write(plaintext)

    def hencrypt(self,buffer):
        return hex.hexlify(self.encrypt(buffer))
    
    def hdecrypt(self,buffer):
        return self.decrypt(hex.unhexlify(buffer))

    def hfencrypt(self, filename):
        with open(filename, "rb+") as infile:
            ciphertext=self.hencrypt(infile.read())
        with open(filename, "wb+") as outfile:
            outfile.write(ciphertext)

    def hfdecrypt(self, filename):
        with open(filename, "rb+") as infile:
            plaintext=self.hdecrypt(infile.read())
        with open(filename, "wb+") as outfile:
            outfile.write(plaintext)


if __name__=="__main__":
    cipher=Cipher("RES128", b"key")
    ciphertext=cipher.hencrypt(b"testing")
    plaintext=cipher.hdecrypt(ciphertext)
    print(ciphertext)
    print(plaintext)