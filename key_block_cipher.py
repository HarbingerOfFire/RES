'''The final stage: XOR the input buffer by the hash of the key'''

import SXH128, SXH256, SXH512

class key_block_cipher:
    def __init__(self, algorithm, buffer, key) -> None:
        self.SXH128=SXH128.SXH128()
        self.SXH256=SXH256.SXH256()
        self.SXH512=SXH512.SXH512()
        self.algorithm = int(algorithm[-3:])
        self.buffer=buffer
        self.key=key
        self.og_key=key

    def hash(self):
        match self.algorithm:
            case 128:
                self.key=self.SXH128.hash(self.key)
            case 256:
                self.key=self.SXH256.hash(self.key)
            case 512:
                self.key=self.SXH512.hash(self.key)
    
    def __block_pad__(self):
        blocks=[self.buffer[i:i+self.algorithm] for i in range(0, len(self.buffer), self.algorithm)]
        for i in range(len(blocks)):
            blocks[i]=blocks[i].ljust(self.algorithm, b"0")
        self.blocks=blocks

    def cipher(self):
        self.__block_pad__()
        result=[]
        for block in self.blocks:
            self.hash()
            result.append(bytes([a^b for a,b in zip(block, self.key)]))
        self.buffer=b"".join(result)
        return self.buffer
    
    def decipher(self):
        self.key=self.og_key
        return self.cipher().rstrip(b"0")


if __name__=='__main__':
    cipher=key_block_cipher("RES256",b"buffer", b"key")
    print(cipher.cipher())
    print(cipher.decipher())