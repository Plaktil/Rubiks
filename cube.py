'''
Rubik's cube

[X] Implement Block class
[ ] Implement Rotations
[ ] Read user input from command line
[ ] Find a module for visual representation
[ ] 

'''

# Import modules
import numpy as np

# Create cube class	
class Cube:
	def __init__(self,size):
		
# Create a cube array containing layers i	
		cube=[]
		for z in range(size):
			
# Create a layer array containing rows j			
			for y in range(size):
				
# Create a row array containing blocks k
# Block is an array containing the position of the block and a vector containing parameters 
# representing the orientation of the colored face according to the coordinate and an encoding of its color as its norm
				for x in range(size):
					b = Block(z - ((size - 1) / 2), y - ((size - 1) / 2), x - ((size - 1) / 2), size)
					cube.append(b)
			
			self.cube = cube
	
	# Rotation matrixes
	yrot=np.array([
	[0, 0, 1],
	[0, 1, 0],
	[-1, 0, 0]])

	xrot=np.array([
	[1, 0, 0],
	[0, 0, -1],
	[0, 1, 0]])

	zrot=np.array([
	[0, -1, 0],
	[1, 0, 0],
	[0, 0, 1]])


class Block():
	def __init__(self, x, y ,z, size):
		self.pos = [x, y, z]
		self.colors = [0, 0, 0]

		if x==0:
			self.colors[0] = -5
		if x==size - 1:
			self.colors[0] = 2
		if y==0:
			self.colors[1] = 1
		if y==size - 1:
			self.colors[1] = -6
		if z==0:
			self.colors[2] = 3
		if z==size - 1:
			self.colors[2] = -4

	def draw():
		pass
				
a=Cube(3)
for b in a.cube: 
	print(b.pos, b.colors)
