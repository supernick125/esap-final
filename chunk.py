from grass import *
from dirt import *
from bedrock import *
from tree import *
from tnt import *

import random 

class Chunk:

    #ADD TO BLOCK LIST!!!
    def __init__(self):
        self.blocks = []
        self.blocks.append(Tree(randx, randy, randz))
        self.blocks.append(Tnt((0,1,0)))
        for x in range(3):
            for z in range(3):
                for y in range(3):
                    if y == 0:
                        self.blocks.append(Grass((x,-y,z)))
                    elif y >= 1 and y < 3:
                        self.blocks.append(Dirt((x,-y,z)))
                    elif y == 3:
                        self.blocks.append(Bedrock((x,-y,z)))
           

        
      

    def draw(self):
        for block in self.blocks:
            block.draw()
