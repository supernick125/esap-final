
from grass import *
from dirt import *
from stone import *
from bedrock import *
from sand import *
from snow import *
from tnt import *
from pumpkin import *

from tree import *

import random

class Chunk1:

    #ADD TO BLOCK LIST!!!
    def __init__(self,pos,biome):
        self.pos = pos
        self.biome = biome
        self.blocks = []

        if biome == "grassland":

            #self.blocks.append(Tree((self.pos[0] + 0,0,self.pos[2])))
            #self.blocks.append(Tnt((self.pos[0] + 0,1,self.pos[2] + 0)))
            self.blocks.append(Pumpkin((self.pos[0] + 5,1,self.pos[2] + 3)))

            #creates base
            for x in range(9):
                for z in range(9):
                    for y in range(3):
                        if y == 0:
                            self.blocks.append(Grass((self.pos[0] + x,-y,self.pos[2] + z)))
                        elif y >= 1 and y < 2:
                            self.blocks.append(Dirt((self.pos[0] + x,-y,self.pos[2] + z)))
                        elif y == 2:
                            self.blocks.append(Bedrock((self.pos[0] + x,-y,self.pos[2] + z)))
        elif biome == 'desert':
            for x in range(9):
                for z in range(9):
                    for y in range(3):
                        if y <2:
                            self.blocks.append(Sand((self.pos[0] + x,-y,self.pos[2] + z)))
                        if y ==2:
                            self.blocks.append(Bedrock((self.pos[0] + x,-y,self.pos[2] + z)))
        elif biome == 'snow':
            for x in range(9):
                for z in range(9):
                    for y in range(3):
                        if y == 0:
                            self.blocks.append(Snow((self.pos[0] + x,-y,self.pos[2] + z)))
                        elif y >= 1 and y < 2:
                            self.blocks.append(Dirt((self.pos[0] + x,-y,self.pos[2] + z)))
                        elif y == 2:
                            self.blocks.append(Bedrock((self.pos[0] + x,-y,self.pos[2] + z)))
        elif biome == 'stone':
            for x in range(9):
                for z in range(9):
                    for y in range(3):
                        if y <2:
                            self.blocks.append(Stone((self.pos[0] + x,-y,self.pos[2] + z)))
                        elif y == 2:
                            self.blocks.append(Bedrock((self.pos[0] + x,-y,self.pos[2] + z)))

    def __str__(self):
        return("Chunk Pos: {} Chunk Biome: {}".format(self.pos, self.biome))

    def get_coords(self):
        self.block_coords = []
        for block in self.blocks:
            self.block_coords.append(block.get_pos())
        return(self.block_coords)

    def gen_exposed(self,world):
        for block in self.blocks:
            block.set_exposed(world)

    def draw(self,world):
        for block in self.blocks:
            if block.get_exposed():
                block.draw()
