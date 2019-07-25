from chunk import *
from pyglet.gl import *

class World():

    def __init__(self):
        self.chunks = []
        self.world_coords = []

        SHIFT = 9

        #self.chunks.append(Chunk((0,0,0),"desert"))
        #self.chunks.append(Chunk((0,0,0),"grassland"))
        #self.chunks.append(Chunk((0,0,SHIFT),"grassland"))
        #self.chunks.append(Chunk((-1*SHIFT,0,0),"grassland"))
        # self.chunks.append(Chunk((-1*SHIFT,0,-1*SHIFT),"grassland"))
        # self.chunks.append(Chunk((1*SHIFT,0,-1*SHIFT),"grassland"))
        # self.chunks.append(Chunk((2*SHIFT,0,1*SHIFT),"stone"))
        # self.chunks.append(Chunk((1*SHIFT,0,2*SHIFT),"snow"))

        for x in range(1):
            for z in range(1):
                for y in range(1):
                    self.chunks.append(Chunk((x*SHIFT,y*SHIFT,z*SHIFT), "grassland"))

        self.gen_world_coords()
        self.gen_exposed()

    def gen_world_coords(self):
        for chunk in self.chunks:
            self.world_coords.extend(chunk.get_coords())

    def gen_exposed(self):
        for chunk in self.chunks:
            chunk.gen_exposed(self.world_coords)

    def get_world_coords(self):
        return self.world_coords

    def draw(self):
        for chunk in self.chunks:
            chunk.draw(self.world_coords)
