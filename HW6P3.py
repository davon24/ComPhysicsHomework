#This program simulates NumWalks random walks of tmax steps

from numpy import *
import matplotlib.pyplot as plt

numwalks = 10**5
random.seed(4)
L = 50

coordinates = zeros((2*L,2*L,2*L))


for j in range(numwalks):
        
        x=0
        y=L
        z=L

        coordinates[0][L][L]+=1
        
	t=0
	
	while x >= 0 and x < 2*L and y >= 0 and y< 2*L and z >= 0 and z < 2*L:
		p = random.rand() #rolling the dice
		
		
		if p<=0.167:
			dx = 1
			dy = 0
			dz = 0
		elif p<=0.334:
			dx = -1
			dy = 0
			dz = 0
		elif p<=0.501:
			dx = 0
			dy = 1
			dz = 0
		elif p<=0.668:
			dx = 0
			dy = -1
			dz = 0
		elif p<=0.835:
			dx = 0
			dy = 0
			dz = 1
		else:
			dx = 0
			dy = 0
			dz = -1
		
		x += dx #update position
		y += dy
		z += dz
		
		
		
                if x >= 0 and x < 2*L and y >= 0 and y < 2*L and z >= 0 and z < 2*L:
		    coordinates[x][y][z] += 1

	
		
	
	
x = zeros(2*L)

for i in range(2*L):
    x[i] = i + 1
    

plt.figure()
plt.plot(log(x), log(coordinates[:,L,L]))
plt.xlabel("Log(x+1)")
plt.ylabel("Log N")
plt.show()
plt.figure()
plt.contour(coordinates[:,:,L],20)
plt.axis('equal')
plt.show()