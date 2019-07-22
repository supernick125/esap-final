from spruce import *

class Tree:
	def __init__(self):
		self.blocks = []
		for z in range(5):
			for y in range(5):
				self.blocks.append(Spruce((1,y,z)))



	def draw(self):
		for block in self.blocks:
			block.draw()

                    

