from chunk import *

class World():

    def __init__(self):
        #self.queue = deque()
        self.chunks = []

        SHIFT = 9 

       
        self.chunks.append(Chunk((0,0,9),"desert"))
        self.chunks.append(Chunk((1*SHIFT,0,1*SHIFT),"grassland"))
        self.chunks.append(Chunk((2*SHIFT,0,1*SHIFT),"stone"))
        self.chunks.append(Chunk((1*SHIFT,0,2*SHIFT),"snow"))
        self.chunks[0].get_pos()

    def draw(self):
        for chunk in self.chunks:
            chunk.draw()
