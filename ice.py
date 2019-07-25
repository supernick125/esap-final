from block import *

class Ice(Block):
	def __init__(self,pos):
		self.top_tex = "textures/frosted_ice_0.png"
		self.side_tex = "textures/ice.png"
		self.bottom_tex = "textures/ice.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)