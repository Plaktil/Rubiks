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
	# Rotation matrixes
	_xrot=np.array([
	[1, 0, 0],
	[0, 0, -1],
	[0, 1, 0]])
	_inv_xrot=np.array([
	[1, 0, 0],
	[0, 0, 1],
	[0, -1, 0]])
	
	_yrot=np.array([
	[0, 0, 1],
	[0, 1, 0],
	[-1, 0, 0]])
	_inv_yrot=np.array([
	[0, 0, -1],
	[0, 1, 0],
	[1, 0, 0]])

	_zrot=np.array([
	[0, -1, 0],
	[1, 0, 0],
	[0, 0, 1]])
	_inv_zrot=np.array([
	[0, 1, 0],
	[-1, 0, 0],
	[0, 0, 1]])

	def __init__(self,size):

# Defines the coordinate value of each faces according to "size"
		self.MIN = -((size - 1) / 2)
		self.MAX = ((size - 1) / 2)
		
# Create a cube array containing layers i	
		cube=[]
		for z in range(size):
			
# Create a layer array containing rows j			
			for y in range(size):
				
# Create a row array containing blocks k
# Block is an array containing the position of the block and a vector containing parameters 
# representing the orientation of the colored face according to the coordinate and an encoding of its color as its norm
				for x in range(size):
					b = Block(x - ((size - 1) / 2), y - ((size - 1) / 2), z - ((size - 1) / 2), size)
					cube.append(b)
			
			self.cube = cube

	def rotation(self, move):
		rotation_mat = np.array([])
		side = 0
		if move == "L":
			side = self.MIN
			rotation_mat = self._xrot
		elif move == "L'":
			side = self.MIN
			rotation_mat = self._inv_xrot
		elif move == "R":
			side = self.MAX
			rotation_mat = self._inv_xrot
		elif move == "R'":
			side = self.MAX
			rotation_mat = self._xrot
		elif move == "U":
			side = self.MIN
			rotation_mat = self._yrot
		elif move == "U'":
			side = self.MIN
			rotation_mat = self._inv_yrot
		elif move == "D":
			side = self.MAX
			rotation_mat = self._inv_yrot
		elif move == "D'":
			side = self.MAX
			rotation_mat = self._zrot
		elif move == "B":
			side = self.MIN
			rotation_mat = self._zrot
		elif move == "B'":
			side = self.MIN
			rotation_mat = self._inv_zrot
		elif move == "F":
			side = self.MAX
			rotation_mat = self._inv_zrot
		elif move == "F'":
			side = self.MAX
			rotation_mat = self._zrot

		for b in self.cube:
			if b.x == self.MIN:
				print(b.pos, b.colors)
				b.pos = np.matmul(b.pos, self._xrot)
				b.colors = np.matmul(b.colors, self._xrot)
				print(b.pos, b.colors)
				print("-=-=-=-=-=-=")

class Block():
	def __init__(self, x, y ,z, size):
		self.pos = np.array([x, y, z])
		self.colors = np.array([0, 0, 0])
		self.x = self.pos[0]
		self.y = self.pos[1]
		self.z = self.pos[2]

		max_coord = ((size - 1) / 2)

		if x == -max_coord:
			self.colors[0] = -5
		if x == max_coord:
			self.colors[0] = 2
		if y == -max_coord:
			self.colors[1] = -1
		if y == max_coord:
			self.colors[1] = 6
		if z == -max_coord:
			self.colors[2] = -3
		if z == max_coord- 1:
			self.colors[2] = 4

	def draw():
		pass
				
		
# Test section
a=Cube(3)
for b in a.cube: 
	print(b.pos, b.colors)


