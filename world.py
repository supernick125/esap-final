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

    def add_block(self,pos): #ADD TYPE VARIABLE
        if pos in self.world_coords:
            self.destroy_block(pos)
        added_block = Dirt(pos)
        self.chunks[0].add_block(added_block)
        self.world_coords.append(added_block.get_pos())
        added_block.add_to_batch(added_block.gen_exposed_key(self.world_coords))

    def destroy_block(self,pos):
        self.world_coords.remove(pos)
        #CHECK NEIGHBORS EXPOSED

    def draw(self):
        for chunk in self.chunks:
            chunk.draw(self.world_coords)
