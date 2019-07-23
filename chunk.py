from grass import *
from dirt import *
from bedrock import *
from tree import *
from tnt import *
from pumpkin import *

import random

class Chunk:

    #ADD TO BLOCK LIST!!!
    def __init__(self):
        self.blocks = []
        self.blocks.append(Tree())
<<<<<<< HEAD
=======

>>>>>>> f225a1f4d79af6494bcca9ce73f5ab95aa4fe537
        self.blocks.append(Tnt((0,1,0)))


        #creates base
        for x in range(6):
            for z in range(5):
                for y in range(3):
                    if y == 0:
                        self.blocks.append(Grass((x,-y,z)))
                        self.blocks.append(Grass((-x,-y,z)))
                        self.blocks.append(Grass((x,-y,-z)))
                        self.blocks.append(Grass((-x,-y,-z)))
                    elif y >= 1 and y < 2:
                        self.blocks.append(Dirt((x,-y,z)))
                        self.blocks.append(Dirt((-x,-y,z)))
                        self.blocks.append(Dirt((x,-y,-z)))
                        self.blocks.append(Dirt((-x,-y,-z)))
                    elif y == 2:
                        self.blocks.append(Bedrock((x,-y,z)))
                        self.blocks.append(Bedrock((-x,-y,z)))
                        self.blocks.append(Bedrock((x,-y,-z)))
                        self.blocks.append(Bedrock((-x,-y,-z)))

        #creates pumpkin:
        self.blocks.append(Pumpkin((5,1,3)))

      

        

        


        

<<<<<<< HEAD
    # def get_pos(self):
    #     self.block_pos = []
    #     for block in self.blocks:
    #         self.block_pos.append(block.pos)
    #     print(self.block_pos)
=======
    '''def get_pos(self):
        self.block_pos = []
        for block in self.blocks:
            self.block_pos.app end(block.pos)
        print(self.block_pos)'''
>>>>>>> f225a1f4d79af6494bcca9ce73f5ab95aa4fe537

    def draw(self):
        for block in self.blocks:
            block.draw()
