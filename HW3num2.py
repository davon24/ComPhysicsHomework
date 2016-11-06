#This program shows how to use the Euler-Cromer method for a pendulum

from numpy import *
import matplotlib.pyplot as plt
import numpy.fft as fourier

def accelerations(variables,params,t): #Computes derivatives of momenta or velocities
	g=params[0]
	theta = variables[0]
	
	vdot = -g*(theta + theta**3 + (theta**5)/100)
	return vdot

def energy(coordinates,velocities,params,t):
    g=params[0]
    x = coordinates[0]
    omega = velocities[0]
    
    E = g*(-(x**2)/4 + (x**4)/4 - (x**6)/600)
    
    return E
						
#Variables that we'll need
g=4*pi**2
#The 4*pi**2 is because we work in units where omega = 2pi, so the period of small oscillations is 1
omega0 = 0
theta0 = 0.9
dt = 0.04
numtimes = 200
params=array([g])
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
energies[i] = energy(coordinates[i],velocities[i], params,0)

for i in range(1,numtimes):
	coordinates[i] = coordinates[i-1] + velocities[i-1]*dt + accelerations(coordinates[i-1],params,times[i-1])*(dt**2)/2
	
	velocities[i] = velocities[i-1] + (accelerations(coordinates[i-1],params,times[i-1])+accelerations(coordinates[i],params,times[i]))*dt/2
	
        energies[i] = energy(coordinates[i],velocities[i], params,times[i])

spectrum = fourier.fft(coordinates[:,0]/numtimes) #We are normalizing the spectrum
spectrum = fourier.fftshift(spectrum) #Shift things so that the center frequency is zero
freq = linspace(-0.5/dt,0.5/dt,numtimes) #Create an array for the frequency
	
plt.figure()
plt.plot(times,coordinates[:,0],label=r'$x$')  #Make a plot
plt.xlabel("Time")
plt.ylabel("X Value")
plt.legend(loc = 'upper right')

plt.show()