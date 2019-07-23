from block import *

class Leaves(Block):
	def __init__(self,pos):
		self.top_tex = "textures/leaves_oak.png"
		self.side_tex = "textures/leaves_oak.png"
		self.bottom_tex = "textures/leaves_oak.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)