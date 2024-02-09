"""RES Stage 1: Substitution Ciphers"""

import res_random

class cooc_sc:
    def __init__(self, buffer, key) -> None:
        self.buffer=buffer
        self.random=res_random.Random(key)
        self.map=self.gen_map()

    def gen_map(self):
        original_chars=[byte for byte in range(256)]
        shuffled_chars=self.random.shuffle(original_chars)
        return dict(zip(original_chars, shuffled_chars))
    
    def sub_cipher(self):
        ciphertext=b""
        for byte in self.buffer:
            if byte in self.map:
                ciphertext+=self.map[byte].to_bytes()
            else:
                ciphertext+=byte.to_bytes()
        self.buffer=ciphertext

    def r_sub_cipher(self):
        map={v: k for k,v in self.map.items()}
        plaintext=b""
        for byte in self.buffer:
            if byte in map:
                plaintext+=map[byte].to_bytes()
            else:
                plaintext+=byte.to_bytes()
        self.buffer=plaintext

    def Cumulative_cipher(self):
        ciphertext=bytearray()
        shift =1
        for byte in self.buffer:
            shifted=(byte+shift)%256
            ciphertext.append(shifted)
            shift+=1
        self.buffer=bytes(ciphertext)
    
    def r_cumulative_cipher(self):
        plaintext=bytearray()
        shift=1
        for byte in self.buffer:
            shifted=(byte-shift)%256
            plaintext.append(shifted)
            shift+=1
        self.buffer=bytes(plaintext)
    
    def cipher(self):
        self.Cumulative_cipher()
        self.sub_cipher()
        return self.buffer
    
    def decipher(self):
        self.r_sub_cipher()
        self.r_cumulative_cipher()
        return self.buffer

if __name__=='__main__':
    cs=cooc_sc(b"HelloWorld123", b"key")
    print(cs.cipher())
    print(cs.decipher())