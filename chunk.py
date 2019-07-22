from grass import *
from dirt import *

class Chunk:
    def __init__(self):
        self.blocks = []
        for x in range(3):
            for z in range(3):
                for y in range(3):
                    if y == 0:
                        self.blocks.append(Grass((x,-y,z)))
                    else:
                        self.blocks.append(Dirt((x,-y,z)))

    def draw(self):
        for block in self.blocks:
            block.draw()
