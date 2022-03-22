'''
Rubik's cube

[X] Implement Block class
[X] Implement Rotations (3x3 only for now)
[ ] Implement notation/rotations for all sizes
[ ] Read user input from command line
[ ] Find a module for visual representation
[ ] 

'''
import numpy as np
import random


class Cube:
	# Allowed moves
	moves = ("L", "L'", "R", "R'", "U", "U'", "D", "D'", "F", "F'", "B", "B'")
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
		
# Create a cube array containing every atoms called "blocks"
		cube=[]
		for z in range(size):		
			for y in range(size):
				for x in range(size):
					b = Block(x - ((size - 1) / 2), y - ((size - 1) / 2), z - ((size - 1) / 2), size)
					cube.append(b)
			
			self.cube = cube

	def rotation(self, move):

# Current moves only support outer edges of a 3x3		
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
		else:
			print(move + " is not a recognized move. \n")

		for b in self.cube:
			if b.x == side:
				"""
				visual confirmation

				print(b.pos, b.colors)
				"""
				b.colors = np.matmul(b.colors, rotation_mat)
				"""
				of the rotations

				print(b.pos, b.colors)
				print("-=-=-=-=-=-=")
				"""

	"""
	This method is only used until the GUI picks up the job of representating the cube visually
	"""
	def _draw(self):
		for b in self.cube:
			b._draw()

	def getCube(self):
		blockList = []
		for b in self.cube:
			blockList.append((b.pos, b.colors))
	
		return blockList

	"""
	Any 3x3x3 Rubiks can theoretically be solved in 20 moves. Therefore a shuffle does not need to be more than
	20 (somewhat thoughtfully chosen) moves. This implementation follows this concept.
	"""
	def shuffle(self):
		allowedMoves = dict(zip(self.moves, [True for i in range(0, len(self.moves)-1)]))
		print(allowedMoves)
		moveList = []
		moveCount = 0

		while moveCount < 20:
			nextMove = self.moves[random.randint(0, len(self.moves)-1)]
			print(nextMove)

			"""
			If the move is not directly undoing another move and if it not the third time it is repeated,
			it is elligible to be the next move of the shuffle.
			"""
			if allowedMoves[nextMove] :
				# If it does L, R, L then it will still go through as 3 separate moves for now
				if len(moveList) >= 1 and moveList[-1] == nextMove:
					moveList[-1] = nextMove[0] + "2"
					allowedMoves[nextMove] = False
				else :
					moveList.append(nextMove)
					moveCount += 1
				self.rotation(nextMove)


				if "'" in nextMove: # Remove the "'" (prime)
					counterMove = nextMove[0]
				else:
					counterMove = nextMove + "'" # Add a "'" (prime)
				allowedMoves[counterMove] = False

				if nextMove[0] == "L" or nextMove[0] == "R":
					trueMoves = "U U' D D' F F' B B'"
				elif nextMove[0] == "U" or nextMove[0] == "D":
					trueMoves = "L L' R R' F F' B B'"
				elif nextMove[0] == "F" or nextMove[0] == "B":
					trueMoves = "L L' R R' D D' U U'"

				for move in trueMoves.split():
					allowedMoves[move] = True

		return moveList

				
				

class Block():
	def __init__(self, x, y ,z, size):
# Position of the block in the cube: (-1, -1, -1) is top left back and (0, 0, 0) is the middle block which is non-existent.
		self.pos = np.array([x, y, z])
# Color values {1, 2, 3, 4, 5, 6} and orientation {-1, 1} of the colored faces of a block in a 3x1 vector
		self.colors = np.array([0, 0, 0])
		self.x = self.pos[0]
		self.y = self.pos[1]
		self.z = self.pos[2]

		max_coord = ((size - 1) / 2)

# For example, face towards negative x
		if x == -max_coord:
# is colored 5
			self.colors[0] = -5
# Face towards positive x
		if x == max_coord:
# is colored 2
			self.colors[0] = 2
		if y == -max_coord:
			self.colors[1] = -1
		if y == max_coord:
			self.colors[1] = 6
		if z == -max_coord:
			self.colors[2] = -3
		if z == max_coord- 1:
			self.colors[2] = 4

	def _draw(self):
		print(self.pos, self.colors)
				
		
# Test section
if __name__ == "main":
	a=Cube(3)
	for b in a.cube: 
		print(b.pos, b.colors)
