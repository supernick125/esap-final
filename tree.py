from spruce import *
from pinkleaf import *

class Tree:
	def __init__(self):
		self.blocks = []
		for y in range(5):
			self.blocks.append(Spruce((1,y,1)))
		for z in range(10):
			self.blocks.append(Leaves((z, z, 1)))



	def draw(self):
		for block in self.blocks:
			block.draw()

                    

