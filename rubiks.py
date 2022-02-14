'''
Rubik's cube

'''

# Import modules
import numpy as np

# Create cube class	
class cube:
	def __init__(self,size):
		
# Create a cube array containing layers i	
		cube=[]
		for i in range(size):
			layer=[]
			
# Create a layer array containing rows j			
			for j in range(size):
				row=[]
				
# Create a row array containing blocks k
# Block is an array containing the position of the block and a vector containing parameters 
# representing the orientation of the colored face according to the coordinate and an encoding of its color as its norm
				for k in range(size):
					atom=[[i,j,k]]
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
					atom.append(colors)
					row.append(atom)
				layer.append(row)
			cube.append(layer)
			
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
				
a=cube(3)
print(a.array)
