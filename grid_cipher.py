"""RES Stage 3: Grid Cipher"""
import res_random as random

class grid(list):
    def to_grid(self:str):
        matrix=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                matrix[i][j]=self[i*4+j]
        return grid(matrix)

    def from_grid(self):
        bytestring=b""
        for i in range(4):
            for j in range(4):
                bytestring+=self[i][j].to_bytes()
        return bytestring

    def rand(self):
        gen=random.Random(bytes(self))
        rand_matrix=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                rand_matrix[i][j]=gen.randint(0,255)
        return grid(rand_matrix)

    def __xor__(self, Y):
        result = grid()
        for i in range(4):
            row = []
            for j in range(4):
                row.append(self[i][j] ^ Y[i][j])
            result.append(row)
        return grid(result)

class grid_cipher:
    def __init__(self, buffer, key) -> None:
        self.buffer=buffer
        self.key = key

    def __block_pad__(self):
        blocks=[self.buffer[i:i+16] for i in range(0, len(self.buffer), 16)]
        for i in range(len(blocks)):
            blocks[i]=blocks[i].ljust(16, b"0")
        self.blocks=blocks

    def cipher(self):
        result=b""
        self.__block_pad__()
        for block in self.blocks:
            X = grid(block).to_grid()
            Y = grid(self.key).rand()
            result+=(X ^ Y).from_grid()
        self.buffer=result
        return result
    
    def decipher(self):
        result=b""
        self.__block_pad__()
        for block in self.blocks:
            X = grid(block).to_grid()
            Y = grid(self.key).rand()
            result+=(X^Y).from_grid()
        self.buffer=result
        return self.buffer.rstrip(b"0")

if __name__=='__main__':
    gc=grid_cipher(b"abcdefghijklmnoph", b"key")
    print("Encrypted: ", gc.cipher())
    print("Decrypteed: ", gc.decipher())