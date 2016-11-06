#This program simulates NumWalks random walks of tmax steps

from numpy import *
import matplotlib.pyplot as plt

numwalks =10**4 #Play with this and see what it does to the quality of the graphs
tmax = 2*10**2 #Maximum number of steps in the walk
a = 4

x2 = zeros(tmax)
y2 = zeros(tmax)
xave = zeros(tmax)
yave = zeros(tmax)

#random.seed(1) #This command seeds the random number generator.  If it's commented out,
#the seed is the clock time (i.e. different each run)
for j in range(numwalks):
        x = zeros([tmax]) #this stores the most recent walk.  We re-initialize it each time.
        y = zeros([tmax]) #same here
	t=0
	while t<tmax:
		p = a*random.rand()
		angle = random.randint(0,2*pi)
		
		dx = a*cos(angle)
		dy = a*sin(angle)
		
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
r2 = x2+y2 - xave**2 - yave**2

plt.figure()
plt.plot(r2,label=r'$\langle r^2\rangle$')
plt.plot(y,label=r'$\langle y\rangle$')
plt.legend(loc='upper right')
plt.show()
plt.figure()
plt.plot(x,y,label='One example walk')
plt.legend(loc='upper right')
plt.axis('equal')
plt.show()