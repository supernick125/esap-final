from chunk import *

class World():

    def __init__(self):
        #self.queue = deque()
        self.chunks = []

        SHIFT = 10

        for x in range(2):
            for z in range(2):
                self.chunks.append(Chunk((x*SHIFT,0,z*SHIFT),"grassland"))

    def draw(self):
        for chunk in self.chunks:
            chunk.draw()
