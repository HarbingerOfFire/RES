'''Self Made Randomization module using SXH-128.py'''

import SXH128 as SXH
import time

class Random:
    def __init__(self, seed:bytes=None):
        self.SXH = SXH.SXH128()
        if seed is not None:
            self.bytes = self.seed=seed
        else:
            self.bytes = self.seed=int(time.time())

    def _generate_seed(self):
        seed = self.SXH.hash(self.bytes)
        self.bytes=seed
        self.seed = int.from_bytes(seed, byteorder='big')
        return self.seed
    
    def randrange(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        seed = self._generate_seed()
        return (seed % ((stop - start) // step)) * step + start
    
    def randint(self, a, b):
        return self.randrange(a, b + 1)
    
    def choice(self, seq):
        seed = self._generate_seed()
        return seq[seed % len(seq)]
    
    def shuffle(self, seq):
        seed = self._generate_seed()
        shuffled = list(seq)
        for i in range(len(shuffled) - 1, 0, -1):
            j = seed % (i+1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
    
    def r_shuffle(self, seq):
        seed = self._generate_seed()
        shuffled = list(seq)
        for i in range(len(shuffled) - 1, 0, -1)[::-1]:
            j = seed % (i+1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled

    def getrandbits(self, k):
        seed = self._generate_seed()
        return (seed >> (self.seed.bit_length() - k)) & ((1 << k) - 1)

    def randbytes(self, n):
        seed = self._generate_seed()
        return seed.to_bytes((seed.bit_length() + 7) // 8, byteorder='big')[:n]

if __name__=='__main__':
    random=Random(b"123")
    for i in range(100):
        print(random.randint(1, 100))