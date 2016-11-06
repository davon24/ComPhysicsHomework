#This program simulates NumWalks random walks of tmax steps

from numpy import *
import matplotlib.pyplot as plt

numwalks = 10**3 #Play with this and see what it does to the quality of the graphs
tmax = 10**3 #Maximum number of steps in the walk
gridsize = 50

x2 = zeros(tmax)
y2 = zeros(tmax)
xave = zeros(tmax)
yave = zeros(tmax)
visitcounts = zeros([gridsize,gridsize])
dxold = 1
dyold = 0
dxnew = 0
dynew = 0
random.seed(1) #This command seeds the random number generator.  If it's commented out,
#the seed is the clock time (i.e. different each run)
for j in range(numwalks):
	a = random.rand()
	x = zeros([tmax]) #this stores the most recent walk.  We re-initialize it each time.
	y = zeros([tmax]) #same here
	t=0
	x[t]=int(0.5*gridsize)
	y[t]=int(0.5*gridsize)
	visitcounts[y[t]][x[t]] += 1

	if a > 0.25:
		dxold = 1
		dyold = 0
	elif a > 0.5:
		dxold = 0
		dyold = 1
	elif a > 0.75:
		dxold = -1
		dyold = 0
	else:
		dxold = 0
		dyold = -1

	for t in range(1,tmax):
		p = random.rand() #Rolling the dice


		prevx = x[t-1]
		prevy = y[t-1]

		leftx = prevx - dyold
		lefty = prevy + dxold
		rightx = prevx + dyold
		righty = prevy - dxold
		forx = prevx + dxold
		fory = prevy + dyold

		if leftx < 0 or leftx == gridsize:
			leftx %= gridsize

		if lefty < 0 or lefty == gridsize:
			lefty %= gridsize

		if rightx < 0 or rightx == gridsize:
			rightx %= gridsize

		if righty < 0 or righty == gridsize:
			righty %= gridsize

		if forx < 0 or forx == gridsize:
			forx %= gridsize

		if fory < 0 or fory == gridsize:
			fory %= gridsize

		leftvisits = visitcounts[lefty][leftx] #change this to account for wrapping

		rightvisits = visitcounts[righty][rightx]

		forvisits = visitcounts[fory][forx] # normal case
        
		leftprob = 1/(1 + leftvisits)
		rightprob = 1/(1 + rightvisits)
		forprob = 1/(1 + forvisits)
        
		c=(leftprob + rightprob + forprob)**-1
        
		leftprob *= c
		rightprob *= c
		forprob *= c
		
		if p<=leftprob:
			dxnew = -dyold #left
			dynew = dxold
		elif p<=leftprob + rightprob:
			dxnew = dyold #right
			dynew = -dxold
		else:
			dxnew = dxold #forward
			dynew = dyold
			
			
		x[t] = x[t-1]+dxnew #update position
		y[t] = y[t-1]+dynew
		
		if x[t]<0 or x[t] >= gridsize:
		    x[t] = x[t]%gridsize
		    
		if y[t]<0 or y[t] >= gridsize:
		    y[t] = y[t]%gridsize
		    
		x2[t] = x2[t]+(x[t])**2 #update our running tally of x^2(t)
		y2[t] = y2[t]+(y[t])**2
		xave[t] = xave[t]+x[t]
		yave[t] = yave[t]+y[t]

		visitcounts[y[t],x[t]] += 1

		dxold = dxnew
		dyold = dynew


x2=x2/numwalks
y2=y2/numwalks
xave=xave/numwalks
yave=yave/numwalks
r2 = x2 + y2 - xave**2 - yave**2
r2 = log(r2)

time = zeros(tmax)
for i in range(tmax):
    time[i] = i+1
time = log(time)

#We need file output for analysis
fout = open("RandomWalkOutput.dat","w")
fout.write("This file stores the positions of steps in a weakly self-avoiding random walk\n")
fout.write("The next line tells how many points are in the cluster, and after that it's in x, y format\n")
fout.write(str(tmax)+'\n')
for t in range(tmax):
    fout.write(str(x[t])+', '+str(y[t])+'\n')
fout.close()


plt.figure()
plt.plot(time,r2, label=r'log$\langle r^2\rangle$')
#plt.plot(yave,label=r'$\langle y\rangle$')
plt.legend(loc='upper right')
plt.show()
plt.figure()
plt.axis([0,gridsize,0,gridsize])
plt.plot(x,y,label='One example walk')
plt.legend(loc='upper right')
plt.axis('equal')
plt.show()