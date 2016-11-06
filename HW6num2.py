#This program simulates NumWalks random walks of tmax steps

from numpy import *
import matplotlib.pyplot as plt

numwalks = 5*10**3 #Play with this and see what it does to the quality of the graphs
tmax = 10**2 #Maximum number of steps in the walk

x2 = zeros(tmax)
y2 = zeros(tmax)
xave = zeros(tmax)
yave = zeros(tmax)

random.seed(1) #This command seeds the random number generator.  If it's commented out,
#the seed is the clock time (i.e. different each run)
for j in range(numwalks):
        x = zeros([tmax]) #this stores the most recent walk.  We re-initialize it each time.
        y = zeros([tmax]) #same here
	t=0
	while t<tmax:
		p = random.rand()
		
		if p<=0.3:
			dx = 1
			dy = 0
		elif p<=0.5:
			dx = -1
			dy = 0
		elif p<=0.8:
			dx = 0
			dy = 1
		else:
			dx = 0
			dy = -1
		x[t] = x[t-1]+dx #update position
		y[t] = y[t-1]+dy
		x2[t] = x2[t]+(x[t])**2 #update our running tally of x^2(t)
		y2[t] = y2[t]+(y[t])**2
		xave[t] = xave[t]+x[t]
		yave[t] = yave[t]+y[t]
		t=t+1
	

x2=x2/numwalks
y2=y2/numwalks
xave=xave/numwalks
yave=yave/numwalks
r2 = x2+y2
xdiff = x2-(xave)**2
ydiff = y2-(yave)**2

plt.figure()
plt.plot(xave,label=r'$\langle x\rangle$')
plt.plot(yave,label=r'$\langle y\rangle$')
plt.plot(x2,label=r'$\langle x^2\rangle$')
plt.plot(y2,label=r'$\langle y^2\rangle$')
plt.plot(xdiff,label=r'$\langle x^2\rangle$ - $\langle x\rangle^2$')
plt.plot(ydiff,label=r'$\langle y^2\rangle$ - $\langle y\rangle^2$')
plt.legend(loc='upper right')
plt.show()
#plt.figure()
#plt.plot(x,y,label='One example walk')
#plt.legend(loc='upper right')
#plt.axis('equal')
#plt.show()