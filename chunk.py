
from grass import *
from dirt import *
from stone import *
from bedrock import *
from sand import *
from snow import *
from tnt import *
from pumpkin import *
from spruce import *
from leaves import *
from cactus import *
from ice import *

import random

SIDES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]

class Chunk:

    #ADD TO BLOCK LIST!!!
    def __init__(self,pos,biome):
        self.pos = pos
        self.biome = biome
        self.blocks = []

        if biome == "grassland":
            #tree1
            for y in range(4):
                self.blocks.append(Spruce((1+pos[0],y+1,1 + pos[2])))
            for i in range(2):
                self.blocks.append(Leaves((0+pos[0], 3+i , 2+ pos[2])))
                self.blocks.append(Leaves((0+pos[0], 3+i, 1+ pos[2])))
                self.blocks.append(Leaves((0+pos[0], 3+i, 0+ pos[2])))
                self.blocks.append(Leaves((1+pos[0], 3+i, 0+ pos[2])))
                self.blocks.append(Leaves((2+pos[0], 3+i, 0+ pos[2])))
                self.blocks.append(Leaves((2+pos[0], 3+i, 1+ pos[2])))
                self.blocks.append(Leaves((1+pos[0], 3+i, 2+ pos[2])))
                self.blocks.append(Leaves((2+pos[0], 3+i, 2+ pos[2])))
            self.blocks.append(Leaves((1 + pos[0], 5, 1+pos[2])))

            #tree2
            for y in range(4):
                self.blocks.append(Spruce((5,y+1,5)))
            for i in range(2):
                self.blocks.append(Leaves((4, 3+i , 6)))
                self.blocks.append(Leaves((4, 3+i, 5)))
                self.blocks.append(Leaves((4, 3+i, 4)))
                self.blocks.append(Leaves((5, 3+i, 4)))
                self.blocks.append(Leaves((6, 3+i, 4)))
                self.blocks.append(Leaves((6, 3+i, 5)))
                self.blocks.append(Leaves((5, 3+i, 6)))
                self.blocks.append(Leaves((6, 3+i, 6)))
            self.blocks.append(Leaves((5, 5, 5)))

            #tree3
            for y in range(4):
                self.blocks.append(Spruce((8,y+1,1)))
            for i in range(2):
                self.blocks.append(Leaves((7, 3+i , 2)))
                self.blocks.append(Leaves((7, 3+i, 1)))
                self.blocks.append(Leaves((7, 3+i, 0)))
                self.blocks.append(Leaves((8, 3+i, 0)))
                self.blocks.append(Leaves((9, 3+i, 0)))
                self.blocks.append(Leaves((9, 3+i, 1)))
                self.blocks.append(Leaves((8, 3+i, 2)))
                self.blocks.append(Leaves((9, 3+i, 2)))
            self.blocks.append(Leaves((8, 5, 1)))

            #tree4
            for y in range(4):
                self.blocks.append(Spruce((1,y+1,8)))
            for i in range(2):
                self.blocks.append(Leaves((0, 3+i , 9)))
                self.blocks.append(Leaves((0, 3+i, 8)))
                self.blocks.append(Leaves((0, 3+i, 7)))
                self.blocks.append(Leaves((1, 3+i, 7)))
                self.blocks.append(Leaves((2, 3+i, 7)))
                self.blocks.append(Leaves((2, 3+i, 8)))
                self.blocks.append(Leaves((1, 3+i, 9)))
                self.blocks.append(Leaves((2, 3+i, 9)))
            self.blocks.append(Leaves((1, 5, 8)))

            #random blocks
            self.blocks.append(Tnt((self.pos[0] + 1 ,1,self.pos[2] + 4)))
            self.blocks.append(Pumpkin((self.pos[0] + 5,1,self.pos[2] + 3)))
            self.blocks.append(Pumpkin((8,1,3)))
            self.blocks.append(Pumpkin((4,1,7)))
            self.blocks.append(Pumpkin((7,1,7)))

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
            for y in range(2):
                self.blocks.append(Cactus((13,y+1,6)))
            for y in range(3):
                self.blocks.append(Cactus((11,y+1,2)))
            for y in range(4):
                self.blocks.append(Cactus((16,y+1,2)))

            #creates base
            for x in range(9):
                for z in range(9):
                    for y in range(3):
                        if y <2:
                            self.blocks.append(Sand((self.pos[0] + x,-y,self.pos[2] + z)))
                        if y ==2:
                            self.blocks.append(Bedrock((self.pos[0] + x,-y,self.pos[2] + z)))

        elif biome == 'snow':

            for x in range(4):
                for z in range(4):
                    self.blocks.append(Ice((x+1,0,13+z)))

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
            for l in range(7):
                for p in range(7):
                    self.blocks.append(Stone((10+l, 1, 10+p)))

            for l in range(5):
                for p in range(5):
                    self.blocks.append(Stone((11+l, 2, 11+p)))

            for l in range(3):
                for p in range(3):
                    self.blocks.append(Stone((12+l, 3, 12+p)))

            self.blocks.append(Tnt((13,4,13)))

            for x in range(9):
                for z in range(9):
                    for y in range(3):
                        if y <2:
                            self.blocks.append(Stone((self.pos[0] + x,-y,self.pos[2] + z)))
                        elif y == 2:
                            self.blocks.append(Bedrock((self.pos[0] + x,-y,self.pos[2] + z)))

    def gen_coords(self):
        self.block_coords = []
        for block in self.blocks:
            self.block_coords.append(block.get_pos())
        return(self.block_coords)

    def gen_exposed_batches(self,world):
        for block in self.blocks:
            block.add_to_batch(block.gen_exposed_key(world))

    def update_neighbors(self,key,world):
        for block in self.blocks:
            if block.get_pos() == key:
                block.add_to_batch(block.gen_exposed_key(world))

    def add_block(self,added_block):
        self.blocks.append(added_block)
        self.block_coords.append(added_block.get_pos())

    def destroy_block(self,destroyed_block):
        for i in range(len(self.blocks)):
            if self.blocks[i].get_pos() == destroyed_block:
                self.blocks.remove(self.blocks[i])
                break

    def get_coords(self):
        return self.block_coords

    def draw(self,world):
        for block in self.blocks:
            block.draw()

    def __str__(self):
        return("Chunk Pos: {} Chunk Biome: {}".format(self.pos, self.biome))
