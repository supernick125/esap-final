from block import *

class Bedrock(Block):

    def __init__(self,pos):
        self.top_tex = "textures/bedrock.png"
        self.side_tex = "textures/bedrock.png"
        self.bottom_tex = "textures/bedrock.png"

        super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)
