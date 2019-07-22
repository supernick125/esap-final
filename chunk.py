from block import *

class Chunk:
    def __init__(self):
        self.blocks = []
        for i in range(16):
            for j in range(16):
                self.blocks.append(Block((i,0,j)))

    def draw(self):
        for block in self.blocks:
            block.draw()
