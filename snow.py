from block import *

class Snow(Block):
	def __init__(self,pos):
		self.top_tex = "textures/snow.png"
		self.side_tex = "textures/grass_block_snow.png"
		self.bottom_tex = "textures/dirt.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)