from spruce import *
from pinkleaf import *

class Tree:
	def __init__(self, randx, randy, randz):
		self.blocks = []
		for y in range(5):
			self.blocks.append(Spruce((1,y,1)))
		for i in range(2):
			self.blocks.append(Leaves((0, 4+i , 2)))
			self.blocks.append(Leaves((0, 4+i, 1)))
			self.blocks.append(Leaves((0, 4+i, 0)))
			self.blocks.append(Leaves((1, 4+i, 0)))
			self.blocks.append(Leaves((2, 4+i, 0)))
			self.blocks.append(Leaves((2, 4+i, 1)))
			self.blocks.append(Leaves((1, 4+i, 2)))
			self.blocks.append(Leaves((2, 4+i, 2)))
		
		
			


			
			


	def draw(self):
		for block in self.blocks:
			block.draw()

                    

