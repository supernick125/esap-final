from spruce import *
from leaves import *

class Tree:
	def __init__(self, pos):
		self.pos = pos
		self.blocks = []

		for y in range(5):
			self.blocks.append(Spruce((1+pos[0],y,1 + pos[2])))
		for i in range(2):
			self.blocks.append(Leaves((0+pos[0], 3+i , 2+ pos[2])))
			self.blocks.append(Leaves((0+pos[0], 3+i, 1+ pos[2])))
			self.blocks.append(Leaves((0+pos[0], 3+i, 0+ pos[2])))
			self.blocks.append(Leaves((1+pos[0], 3+i, 0+ pos[2])))
			self.blocks.append(Leaves((2+pos[0], 3+i, 0+ pos[2])))
			self.blocks.append(Leaves((2+pos[0], 3+i, 1+ pos[2])))
			self.blocks.append(Leaves((1+pos[0], 3+i, 2+ pos[2])))
			self.blocks.append(Leaves((2+pos[0], 3+i, 2+ pos[2])))

		self.blocks.append(Leaves((1 + pos[0], 5, 1+pos[2])))

	def draw(self):
		for block in self.blocks:
			block.draw()
