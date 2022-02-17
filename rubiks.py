'''
Rubik's cube

[ ] Implement Block class
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
		for i in range(size):
			
# Create a layer array containing rows j			
			for j in range(size):
				
# Create a row array containing blocks k
# Block is an array containing the position of the block and a vector containing parameters 
# representing the orientation of the colored face according to the coordinate and an encoding of its color as its norm
				for k in range(size):
					block=[[i - ((size-1)/2), j - ((size-1)/2), k - ((size-1)/2)]]
					colors=[0,0,0]
					if k==0:
						colors=[-5,0,0]
					if k==size-1:
						colors=[2,0,0]
					if j==0:
						colors[1]=1
					if j==size-1:
						colors[1]=-6
					if i==0:
						colors[2]=3
					if i==size-1:
						colors[2]=-4
					block.append(colors)
					cube.append(block)
			
			self.array=np.array(cube)
	
	# Rotation matrixes
	yrot=np.array([
	[0,0,1],
	[0,1,0],
	[-1,0,0]])

	xrot=np.array([
	[1,0,0],
	[0,0,-1],
	[0,1,0]])

	zrot=np.array([
	[0,-1,0],
	[1,0,0],
	[0,0,1]])


class Block:
	def init(self, x, y ,z):
		self.pos = [x, y, z]
		self.colors = [0, 0, 0]
				
a=Cube(3)
print(a.array)
