from block import *

class Tnt(Block):

    def __init__(self,pos):
        self.top_tex = "textures/grass_top.png"
        self.side_tex = "textures/grass_side.png"
        self.bottom_tex = "textures/dirt.png"

        super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)
