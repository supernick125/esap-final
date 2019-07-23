from block import *

class Spruce(Block):
	def __init__(self,pos):
		self.top_tex = "textures/stripped_spruce_log_top.png"
		self.side_tex = "textures/spruce_log.png"
		self.bottom_tex = "textures/spruce_log.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)
