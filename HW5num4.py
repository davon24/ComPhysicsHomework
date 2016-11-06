#This code will solve Laplace's equation on 2D square grids with arbitrary boundaries.
#We will do the case of a circular object on the end
#This code uses Successive Over-Relaxation

from numpy import *
import matplotlib.pyplot as plt

ps = 50.0 #plate separation
H = 5*int(ps) #Height of window
W = H #Width of window
xc = 0.5*W #Position of circle center
yc = 0.5*H #Position of circle center
Plate1 = 1.0 #potential on circle
Plate2 = -1.0
Max_dV = 0.0001*Plate1 #I want to calculate this so that the changes from one iteration to the next are < MaxDeltaV
MinIterations = 0.4*(W+H-ps)#Mininum time to run
UpdateFrequency = 40 #How many iterations should go before we print an update?
alpha = 2*(1-1.00*pi/max([W,H])) #Over-relaxation parameter
BC = zeros([W,H])
V = zeros([W,H])

#Let's set up BC to have the potential equal Vcircle for  points less than R from (xc,yc)
numused = 0
for x in range(1, W-1): #We leave edge alone
    for y in range(1, H-1): #We leave edge alone
	if y == int(2*ps) and x >= int(2*ps) and x <= int(3*ps):
	   BC[x,y] = 1 #Set these points as untouchable
	   V[x,y] = Plate1 #Initialize these points
	if y == int(3*ps) and x>=int(2*ps) and x<=int(3*ps):
	   BC[x,y] = 1
	   V[x,y] = Plate2
	   numused+=1
	      
#Now we start iterating
AvgDeltaV = 2*Max_dV
i=0
while (AvgDeltaV>Max_dV) or (i<=MinIterations):
    Sum_dV=0
    
    for x in range(1,W-1):
        for y in range(1,H-1):
            if BC[x,y]==0:
                dV=alpha*(0.25*(V[x+1,y]+V[x-1,y]+V[x,y+1]+V[x,y-1])-V[x,y])
                V[x,y]=V[x,y]+dV
                Sum_dV+=abs(dV)
                
    #Calculate the average change
    AvgDeltaV = Sum_dV/numused
    
    if (1.0*i)/UpdateFrequency == i/UpdateFrequency:
        print('Iteration %d.  Average voltage change= %f' % (i, AvgDeltaV))
    i +=1
    
#print('System size: %d' % (H))
#print('Total iterations: %d' % (i))
#if i>MinIterations:
#    print('This exceeded the minimum number of iterations (%d).' % (MinIterations))
#else:
#    print('This was the minimum number of iterations.')
#print('Average voltage change in last iteration: %.3g' % (AvgDeltaV))

Ex = -(V[W/2,W/2+1] - V[W/2,W/2-1])/2
print(Ex)
print(ps)
plt.figure()

#plt.subplot(211)
plt.contour(V,50)
plt.axis('equal')
#plt.subplot(212)
#plt.imshow(BC)
#plt.axis('equal')
plt.show()