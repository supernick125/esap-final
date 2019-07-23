from block import *

class Cactus(Block):
	def __init__(self,pos):
		self.top_tex = "textures/cactus_top.png"
		self.side_tex = "textures/cactus_side.png"
		self.bottom_tex = "textures/cactus_bottom.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)