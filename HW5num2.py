#This code will solve Laplace's equation on 2D square grids with arbitrary boundaries.
#We will do the case of a circular object on the end
#This code uses Successive Over-Relaxation

from numpy import *
import matplotlib.pyplot as plt

H = 100 #Height of window
W = H #Width of window
R = 24.0 
xc = 0.5*W #Position of circle center
yc = 0.5*H #Position of circle center
Vsquare = 1.0 #potential on circle
Max_dV = 0.0001*Vsquare #I want to calculate this so that the changes from one iteration to the next are < MaxDeltaV
MinIterations = 0.4*(W+H-R)#Mininum time to run
UpdateFrequency = 40 #How many iterations should go before we print an update?
alpha = 1.0*(1-1.00*pi/max([W,H])) #Over-relaxation parameter

BC = zeros([W,H]) #Identifies places to check for boundary condition
V = zeros([W,H])

#Let's set up BC to have the potential equal Vcircle for  points less than R from (xc,yc)
numused = 0
for x in range(1, W-1): #We leave edge alone
    for y in range(1, H-1): #We leave edge alone
        r = sqrt((x-xc)**2+(y-yc)**2)
	if r<=R:
	   BC[x,y] = 1 #Set these points as untouchable
	   V[x,y] = Vsquare #Initialize these points
	else:
	   V[x,y]=Vsquare*R/r
	   numused+=1
	      
#Now we start iterating
AvgDeltaV = 2*Max_dV
i=0
while (AvgDeltaV>Max_dV) or (i<=MinIterations):
    Sum_dV=0
    
    ##Put something in that goes along the 45 degree line
    #for x in range(W/2,W-1):
    #    V[x,x] += (2*V[x-1, y]+2*V[x,y+1])*alpha*0.25
    #    V[W/2,x]+=(V[x, y]+2*V[x+1,y]+V[x,y-1])*alpha*0.25
        
    for x in range(W/2,W-1):
        for y in range(x,W-1):
            if BC[x,y]==0:
                if x == y:
                    dV = alpha*(0.25*(2.0*V[x-1,y]+2.0*V[x,y+1])-V[x,y])
                elif x==W/2:
                    dV = alpha*(0.25*(2.0*V[x+1,y]+V[x,y+1]+V[x,y-1])-V[x,y])
                else:    
                    dV=alpha*(0.25*(V[x+1,y]+V[x-1,y]+V[x,y+1]+V[x,y-1])-V[x,y])
                    
                V[x,y]=V[x,y]+dV # 4th eighth
                V[y,x] = V[x,y] # 3rd eighth
                V[W-1-x,y] = V[x,y] #5th eighth
                V[W-1-y,x] = V[y,x] #6th eighth
                
                V[y,W-1-x] = V[y,x]
                V[W-1-x,W-1-y] = V[W-1-x,y]
                V[W-1-y,W-1-x] = V[W-1-y,x] #7th eighth
                V[x,W-1-y] = V[x,y] #1st eighth
                Sum_dV+=abs(dV)
    
    #Calculate the average change
    AvgDeltaV = Sum_dV/numused
    
    if (1.0*i)/UpdateFrequency == i/UpdateFrequency:
        print('Iteration %d.  Average voltage change= %f' % (i, AvgDeltaV))
    i +=1
    
print('System size: %d' % (H))
print('Total iterations: %d' % (i))
if i>MinIterations:
    print('This exceeded the minimum number of iterations (%d).' % (MinIterations))
else:
    print('This was the minimum number of iterations.')
print('Average voltage change in last iteration: %.3g' % (AvgDeltaV))

#plt.figure()
#plt.subplot(211)
#plt.contour(V,10)
#plt.axis('equal')
#plt.subplot(212)
#plt.imshow(BC)
#plt.axis('equal')
#plt.show()
