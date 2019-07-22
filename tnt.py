from block import *

class Tnt(Block):

    def __init__(self,pos):
        self.top_tex = "textures/tnt_top.png"
        self.side_tex = "textures/tnt_side.png"
        self.bottom_tex = "textures/tnt_bottom.png"

        super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)
