from spruce import *
from pinkleaf import *

class Tree:
	def __init__(self):
		self.blocks = []
		for y in range(5):
			self.blocks.append(Spruce((1,y,1)))
		for z in range(6):
			self.blocks.append(Leaves((z, 5, 1)))
			self.blocks.append(Leaves((1, z, 1)))
		for x in range(7):
			self.blocks.append(Leaves((1, 5, x)))
			self.blocks.append(Leaves((1, 5, x*(-1))))


			
			


	def draw(self):
		for block in self.blocks:
			block.draw()

                    

