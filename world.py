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
            self.world_coords.extend(chunk.gen_coords())

    def gen_exposed_batches(self):
        for chunk in self.chunks:
            chunk.gen_exposed_batches(self.world_coords)

    def get_world_coords(self):
        return self.world_coords

    def update_neighbors(self,pos):
        x,y,z = pos
        for dx,dy,dz in SIDES:
            key = (x+dx,y+dy,z+dz)
            if key not in self.world_coords:
                continue
            for chunk in self.chunks:
                if key in chunk.get_coords():
                    chunk.update_neighbors(key,self.world_coords)

    def add_block(self,pos): #ADD TYPE VARIABLE
        if pos in self.world_coords:
            self.destroy_block(pos)
        #Conditionals to change block type

        added_block = Stone(pos)


        self.chunks[0].add_block(added_block) #CHUNK CHEESE HERE
        self.world_coords.append(added_block.get_pos())
        added_block.add_to_batch(added_block.gen_exposed_key(self.world_coords))
        self.update_neighbors(pos)

    def destroy_block(self,pos):
        for chunk in self.chunks:
            if pos in chunk.get_coords():
                #update_chunk = self.chunks.index(chunk)
                chunk.destroy_block(pos)
        self.world_coords.remove(pos)
        self.update_neighbors(pos)

    def draw(self):
        for chunk in self.chunks:
            chunk.draw(self.world_coords)
