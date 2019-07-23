from spruce import *
from pinkleaf import *

class Tree:
	def __init__(self):
		self.blocks = []
		for y in range(5):
			self.blocks.append(Spruce((1,y,1)))
		for i in range(2):
<<<<<<< HEAD
			self.blocks.append(Leaves((0, 4+i , 2)))
			self.blocks.append(Leaves((0, 4+i, 1)))
			self.blocks.append(Leaves((0, 4+i, 0)))
			self.blocks.append(Leaves((1, 4+i, 0)))
			self.blocks.append(Leaves((2, 4+i, 0)))
			self.blocks.append(Leaves((2, 4+i, 1)))
			self.blocks.append(Leaves((1, 4+i, 2)))
			self.blocks.append(Leaves((2, 4+i, 2)))
=======
			self.blocks.append(Leaves((0, 3+i , 2)))
			self.blocks.append(Leaves((0, 3+i, 1)))
			self.blocks.append(Leaves((0, 3+i, 0)))
			self.blocks.append(Leaves((1, 3+i, 0)))
			self.blocks.append(Leaves((2, 3+i, 0)))
			self.blocks.append(Leaves((2, 3+i, 1)))
			self.blocks.append(Leaves((1, 3+i, 2)))
			self.blocks.append(Leaves((2, 3+i, 2)))

		self.blocks.append(Leaves((1, 5, 1)))
		
		
			
>>>>>>> f225a1f4d79af6494bcca9ce73f5ab95aa4fe537









	def draw(self):
		for block in self.blocks:
			block.draw()
