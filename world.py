from chunk import *
from pyglet.gl import *

class World():

    def __init__(self):
        self.chunks = []
        self.world_coords = []

        #Making world out of chunks
        SHIFT = 9

        self.chunks.append(Chunk((0,0,0), "grassland"))
        self.chunks.append(Chunk((1*SHIFT,0,0), "desert"))
        self.chunks.append(Chunk((0,0,1*SHIFT), "snow"))
        self.chunks.append(Chunk((1*SHIFT,0,1*SHIFT), "stone"))

        #Generating world list
        self.gen_world_coords()
        #Generating block exposure
        self.gen_exposed_batches()

    def gen_world_coords(self):
        for chunk in self.chunks:
            self.world_coords.extend(chunk.get_coords())

    def gen_exposed_batches(self):
        for chunk in self.chunks:
            chunk.gen_exposed_batches(self.world_coords)

    def get_world_coords(self):
        return self.world_coords

    def draw(self):
        for chunk in self.chunks:
            chunk.draw(self.world_coords)
