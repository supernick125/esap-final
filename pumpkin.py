
from block import *

class Pumpkin(Block):
	def __init__(self, pos):
		self.top_tex = "textures/pumpkin_top.png"
		self.side_tex = "textures/carved_pumpkin.png"
		self.bottom_tex = "textures/pumpkin_side.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)
