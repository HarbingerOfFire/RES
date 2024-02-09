"""RES Stage 2: Randomized Shuffle"""

import res_random

class shuffle:
    def __init__(self, buffer, key) -> None:
        self.key=key
        self.buffer=buffer

    def shuffle(self):
        self.random=res_random.Random(self.key)
        self.buffer=bytes(self.random.shuffle(self.buffer))

    def r_shuffle(self):
        self.random=res_random.Random(self.key)
        self.buffer=bytes(self.random.r_shuffle(self.buffer))

    def cipher(self):
        self.shuffle()
        return self.buffer

    def decipher(self):
        self.r_shuffle()
        return self.buffer


if __name__=='__main__':
    s=shuffle(b"buffer\n", b"key")
    print(s.cipher())
    print(s.decipher())