
import random

from block import *

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
        """Initialize Chunk object and generate block list"""
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

            #Base
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

            #Base
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

            #Base
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

            #Base
            for x in range(9):
                for z in range(9):
                    for y in range(3):
                        if y <2:
                            self.blocks.append(Stone((self.pos[0] + x,-y,self.pos[2] + z)))
                        elif y == 2:
                            self.blocks.append(Bedrock((self.pos[0] + x,-y,self.pos[2] + z)))

    def gen_coords(self):
        """Generate block coordinates list"""
        self.block_coords = []
        for block in self.blocks:
            self.block_coords.append(block.get_pos())
        return(self.block_coords)

    def gen_exposed_batches(self,world):
        """Generate initial exposure states"""
        for block in self.blocks:
            block.add_to_batch(block.gen_exposed_key(world))

    def update_neighbors(self,key,world):
        """Update exposure state for block at key position"""
        for block in self.blocks:
            if block.get_pos() == key:
                block.add_to_batch(block.gen_exposed_key(world))

    def add_block(self,added_block):
        """Add block at specified position"""
        self.blocks.append(added_block)
        self.block_coords.append(added_block.get_pos())

    def destroy_block(self,destroyed_block):
        """Destroy block at specified position"""
        for i in range(len(self.blocks)):
            if self.blocks[i].get_pos() == destroyed_block:
                on_destroy = self.blocks[i].on_destroy()
                self.blocks.remove(self.blocks[i])
                return on_destroy

    def get_coords(self):
        """Return block coordinates list"""
        return self.block_coords

    def get_block(self,pos):
        """Return block object with given position"""
        for block in self.blocks:
            if block.get_pos() == pos:
                return block

    def draw(self,world):
        """Chunk draw function draws all Blocks in list"""
        for block in self.blocks:
            block.draw()

    def __str__(self):
        """Stringify overwrite function"""
        return("Chunk Pos: {} Chunk Biome: {}".format(self.pos, self.biome))
