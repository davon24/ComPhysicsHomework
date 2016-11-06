#This program simulates NumWalks random walks of tmax steps

from numpy import *
import matplotlib.pyplot as plt

numwalks = 10**3 #10**2 #Play with this and see what it does to the quality of the graphs
tmax = 10**3 #Maximum number of steps in the walk

x2 = zeros(tmax)
y2 = zeros(tmax)
xave = zeros(tmax)
yave = zeros(tmax)

L=50
W=50

coordinates=zeros((L,W))

random.seed(1) #This command seeds the random number generator.  If it's commented out,
#the seed is the clock time (i.e. different each run)
for j in range(numwalks):
        x = zeros([tmax]) #this stores the most recent walk.  We re-initialize it each time.
        y = zeros([tmax]) #same here
        
        dxold = 1
        dyold = 0
        coordinates = zeros((L,W))

	t=0
	print j
	for t in range(tmax):
		p = random.rand()
		
		if t==0:
		    prx = dyold 
                    pry = dxold    
                    plx = dyold
                    ply = dxold
                    pfx = dxold
                    pfy = dyold
		else:
                    prx = x[t-1] + dyold 
                    pry = y[t-1] - dxold    
                    plx = x[t-1] - dyold
                    ply = y[t-1] + dxold
                    pfx = x[t-1] + dxold
                    pfy = y[t-1] + dyold      		
				
		if prx < 0:
		    prx = L + dyold
		elif pry < 0:
		    pry = L - dxold
		elif prx >= L:
		    prx = prx % L
		elif pry >= L:
		    pry = pry % L
		    
		if plx < 0:
                    plx = L - dyold
		elif ply < 0:
                    ply = L + dxold
		elif plx >= L:
		    plx = plx % L
		elif ply >= L:
		    ply = ply % L
		
		if pfx < 0:
		    pfx = L + dxold
		elif pfy < 0:
		    pfy = L + dyold
		elif pfx >= L:
		    pfx = pfx % L
		elif pfy >= L:
		    pfy = pfy % L
		    
		    
		nconstant = (1/(1+coordinates[pry,prx]) + 1/(1+coordinates[ply,plx]) + 1/(1+coordinates[pfy,pfx]))**-1
		
	        probright = nconstant*(1/(1+coordinates[pry,prx]))
	        probleft = nconstant*(1/(1+coordinates[ply,plx]))
	        probfor = nconstant*(1/(1+coordinates[pfy,pfx]))
	        
		if p <= probright:#RIGHT
			dxnew = dyold
			dynew = -1 * dxold
		elif p <= probright + probleft: #LEFT
			dxnew = -1 * dyold
			dynew = dxold
		else: #FORWARD
			dxnew = dxold
			dynew = dyold
			
		
		x[t] = x[t-1]+dxnew #update position
		y[t] = y[t-1]+dynew
		
		if x[t] >= L:
		    x[t] %= L
		elif x[t] < 0:
		    x[t] = L + x[t]
		
		if y[t] >= L:
		    y[t] %= L
		elif y[t] < 0:
		    y[t] = L + y[t]
		
		x2[t] = x2[t]+(x[t])**2 #update our running tally of x^2(t)
		y2[t] = y2[t]+(y[t])**2
		xave[t] = xave[t]+x[t]
		yave[t] = yave[t]+y[t]
		
                coordinates[y[t]][x[t]] += 1

                dxold = dxnew
                dyold = dynew
                	
x2=x2/numwalks
y2=y2/numwalks
xave=xave/numwalks
yave=yave/numwalks
r2 = x2+y2

time = zeros([tmax])

for i in range(tmax):
    time[i] = i + 1
    
time = log(time)    
r2 = log(r2)

plt.figure()
plt.plot(time, r2,label=r'$\langle r^2\rangle$')
plt.legend(loc='upper right')
plt.show()
plt.figure()
plt.plot(x,y,label='One example walk')
plt.legend(loc='upper right')
plt.axis('equal')
plt.show()
