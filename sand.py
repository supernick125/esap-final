from block import *

class Sand(Block):
	def __init__(self,pos):
		self.top_tex = "textures/sand.png"
		self.side_tex = "textures/sand.png"
		self.bottom_tex = "textures/sand.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)