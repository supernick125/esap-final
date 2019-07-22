from grass import *
from dirt import *
from bedrock import *
from tree import *


class Chunk:
    def __init__(self):
        self.blocks = []
        self.blocks.append(Tree())
        for x in range(3):
            for z in range(3):
                for y in range(4):
                    if y == 0:
                        self.blocks.append(Grass((x,-y,z)))
                    elif y >= 1 and y < 3:
                        self.blocks.append(Dirt((x,-y,z)))
                    elif y == 3:
                        self.blocks.append(Bedrock((x,-y,z)))

    def draw(self):
        for block in self.blocks:
            block.draw()
