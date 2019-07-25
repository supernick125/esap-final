from chunk import *
from pyglet.gl import *

class World():

    def __init__(self):
        #self.queue = deque()
        self.batch = pyglet.graphics.Batch()
        self.chunks = []
        self.world_coords = []

        SHIFT = 9

        # self.chunks.append(Chunk((0,0,0),"desert"))
        self.chunks.append(Chunk((0,0,0),"grassland"))
        #self.chunks.append(Chunk((0,0,SHIFT),"grassland"))
        #self.chunks.append(Chunk((-1*SHIFT,0,0),"grassland"))
        # self.chunks.append(Chunk((-1*SHIFT,0,-1*SHIFT),"grassland"))
        # self.chunks.append(Chunk((1*SHIFT,0,-1*SHIFT),"grassland"))
        # self.chunks.append(Chunk((2*SHIFT,0,1*SHIFT),"stone"))
        # self.chunks.append(Chunk((1*SHIFT,0,2*SHIFT),"snow"))

        self.gen_world_coords()

    def gen_world_coords(self):
        for chunk in self.chunks:
            self.world_coords.extend(chunk.get_coords())

    def get_world_coords(self):
        return self.world_coords

    def draw(self):
        for chunk in self.chunks:
            chunk.draw(self.world_coords)
