#This program simulates NumWalks random walks of tmax steps

from numpy import *
import matplotlib.pyplot as plt

numwalks = 1 #Play with this and see what it does to the quality of the graphs
tmax = 10**5 #Maximum number of steps in the walk

x2 = zeros(tmax)
y2 = zeros(tmax)
xave = zeros(tmax)
yave = zeros(tmax)
dxold = 1
dyold = 0
dxnew = 0
dynew = 0
random.seed(1) #This command seeds the random number generator.  If it's commented out,
#the seed is the clock time (i.e. different each run)
for j in range(numwalks):
        x = zeros([tmax]) #this stores the most recent walk.  We re-initialize it each time.
        y = zeros([tmax]) #same here
	t=0
	for t in range(tmax):
		p = random.rand() #Rolling the dice
		
		if p<=0.33:
			dxnew = -dyold
			dynew = dxold
		elif p<=0.66:
			dxnew = dyold
			dynew = -dxold
		else:
			dxnew = dxold
			dynew = dyold
		x[t] = x[t-1]+dxnew #update position
		y[t] = y[t-1]+dynew
		x2[t] = x2[t]+(x[t])**2 #update our running tally of x^2(t)
		y2[t] = y2[t]+(y[t])**2
		xave[t] = xave[t]+x[t]
		yave[t] = yave[t]+y[t]
		dxold = dxnew
		dyold = dynew


x2=x2/numwalks
y2=y2/numwalks
xave=xave/numwalks
yave=yave/numwalks
r2 = x2+y2

#We need file output for analysis
fout = open("RandomWalkOutput.dat","w")
fout.write("This file stores the positions of steps in a weakly self-avoiding random walk\n")
fout.write("The next line tells how many points are in the cluster, and after that it's in x, y format\n")
fout.write(str(tmax)+'\n')
for t in range(tmax):
    fout.write(str(x[t])+', '+str(y[t])+'\n')
fout.close()

plt.figure()
plt.plot(r2,label=r'$\langle r^2\rangle$')
plt.plot(yave,label=r'$\langle y\rangle$')
plt.legend(loc='upper right')
plt.show()
plt.figure()
plt.plot(x,y,label='One example walk')
plt.legend(loc='upper right')
plt.axis('equal')
plt.show()