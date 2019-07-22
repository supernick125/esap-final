from block import *

class Dirt(Block):

    def __init__(self,pos):
        self.top_tex = "textures/dirt.png"
        self.side_tex = "textures/dirt.png"
        self.bottom_tex = "textures/dirt.png"

        super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)
