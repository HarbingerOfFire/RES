'''Adapted from SXH-512 https://github.com/harbingeroffire/SXH'''

import string

class SXH512:
    def __init__(self) -> None:
        self.alphabet = string.printable.encode()
        self.block=512
        self.alphabet_block = self.__block_pad__(self.alphabet)

    def __block_pad__(self, string:bytes):
        blocks=[string[i:i+self.block] for i in range(0, len(string), self.block)]
        for i in range(len(blocks)):
            blocks[i]=blocks[i].ljust(self.block, b"0")
        return blocks
    
    def xor_chars(self, block):
        result = b''
        for i in range(len(block)-1):
            result += bytes([block[i]^block[i+1]])
        return result
    
    def xor_strings(self, string_list):
        result = string_list[0]
        for s in string_list[1:]:
            result = bytes([a^b for a,b in zip(result, s)])
        return result

    def hash(self, buffer):
        self.buffer=(buffer+self.alphabet)*200
        blocks=[]
        for block in self.__block_pad__(self.buffer)+self.alphabet_block:
            blocks.append(self.xor_chars(block))
        self.buffer=self.xor_chars(self.xor_strings(blocks))
        return self.buffer
    
    def hexidigest(self, hash:bytes):
        hexidigest=""
        for byte in hash:
            hexidigest+=hex(byte%16).removeprefix("0x")
        return hexidigest

if __name__=='__main__':
    hash_gen=SXH512()
    hash=hash_gen.hash(b"b")
    print(hash_gen.hexidigest(hash))