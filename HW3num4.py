#This program shows how to use the Euler-Cromer method for a pendulum

from numpy import *
import matplotlib.pyplot as plt
import numpy.fft as fourier

def accelerations(variables,velocities,params,t): #Computes derivatives of momenta or velocities
	g=params[0]
	gamma = params[1]
	F = params[2]
	theta = variables[0]
	v = velocities[0]
	vdot = -g*(theta - theta**2 + (theta**5)/100) - gamma*v + F*cos(2*pi*t)
	return vdot

						
#Variables that we'll need
g=4*pi**2
gamma = 0.5
F = 5
#The 4*pi**2 is because we work in units where omega = 2pi, so the period of small oscillations is 1
omega0 = 0
theta0 = 0.01
dt = 0.04
numtimes = 1000
params=array([g,gamma,F])
dof=1 #Number of coordinates, or "degrees of freedom" used to describe the system

#Establish some arrays
times = linspace(0, (numtimes-1)*dt, numtimes)
coordinates = zeros([numtimes,dof])
velocities = zeros([numtimes,dof])
energies=zeros(numtimes)


#initialize the arrays
i=0
coordinates[i] = theta0
velocities[i] = omega0
maxx = [log(theta0)]
maxtime = [0]
for i in range(1,numtimes):
	coordinates[i] = coordinates[i-1] + velocities[i-1]*dt + accelerations(coordinates[i-1],velocities[i-1],params,times[i-1])*(dt**2)/2
	
	velocities[i] = velocities[i-1] + (accelerations(coordinates[i-1],velocities[i-1],params,times[i-1])+accelerations(coordinates[i],velocities[i],params,times[i]))*dt/2
        
        #if i%25 == 0:
        #    maxx.append(log(coordinates[i]))
        #    maxtime.append(dt*i)
	
plt.figure()
plt.plot(times,coordinates,label=r'$gamma=0.5$')  #Make a plot
plt.xlabel("Time")
plt.ylabel("x value")
plt.legend(loc = 'upper right')
plt.show()