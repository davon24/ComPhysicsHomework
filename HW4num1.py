#This program shows how to use the Velocity Verlet method to model planetary motion

from numpy import *
import matplotlib.pyplot as plt

def acceleration(variables,params,t):
	[x,y]=variables	
	MG = params[0]
	alpha = params[1]
	
	r=sqrt(x**2+y**2) #Last night I got ^ and ** confused
	
	a = MG*(1+alpha/r**2)/(r**2)
	
	return array([-a*x/r,-a*y/r])
def E(variable,velocities,params):
    r = variable
    MG = params[0]
    alpha = params[1]
    v1 = velocities[0]
    v2 = velocities[1]
    U = - MG*(1+alpha/(3*r**2))/(r)
    KE = 0.5*(v1**2 + v2**2)
    Energy = U+KE
    
    return array([U,KE,Energy])
    
#Variables that we'll need
r0 = 1.0 #This is the initial distance, in units of AU
#Assume that we start from theta = 0, at least for one planet
vr0 = 0 #We start at aphelion or perihelion, so no radial velocity
vt0 = 2*pi/sqrt(r0) #All of the velocity is initially tangential
alpha = 0.006 #This is a parameter from General Relativity
MG = 4*pi**2 #In units of AU^3/year^2
params = array([MG,alpha],dtype='float')

dt = 0.0001 #In units of years
onehalfdtsquared = 0.5*dt**2 #We use this a lot so just calculate it once
tmax = 5
numtimes = int(tmax/dt)

#Initialize arrays
times = linspace(0,tmax,numtimes)
#Position and velocity arrays
coordinates = zeros([numtimes,2]) #Careful with the brackets for 2D arrays!
velocities = zeros([numtimes,2])
energies = zeros([numtimes,3]) #columns represent potential, kinetic, and total energy, respectively
angmomentum = zeros([numtimes])

coordinates[0] = array([r0,0])
velocities[0] = array([vr0,vt0])

aold = acceleration(coordinates[0],params,0)

#The main loop
for t in range(1,numtimes):
    coordinates[t] = coordinates[t-1]+velocities[t-1]*dt+onehalfdtsquared*aold
    anew = acceleration(coordinates[t],params,times[t-1])
    velocities[t] = velocities[t-1]+0.5*(anew+aold)*dt
    aold = anew #Why calculate two accelerations per iteration when I can recycle?



#If we want to monitor precession, we need to monitor r and  theta
r = zeros(numtimes)
theta = zeros(numtimes)
for t in range(0,numtimes):
    r[t] = sqrt(dot(coordinates[t],coordinates[t])) #Square root of r dot r
    theta[t] = arctan(coordinates[t,1]/coordinates[t,0]) #Arctangent of y over x

for i in range(numtimes):
    energies[i] = E(r[i],velocities[i],params)
    angmomentum[i] = r[i]*cos(theta[i])*velocities[i,1] - r[i]*sin(theta[i])*velocities[i,0]
    
#Time to show results
plt.figure()
plt.subplot(311)
plt.plot(times,energies[:,0])
plt.xlabel('Time')
plt.ylabel('Potential')
plt.subplot(312)
plt.plot(times,energies[:,1])
plt.xlabel('Time')
plt.ylabel('Kinetic')
plt.legend(loc = 'upper right')
plt.subplot(313)
plt.plot(times,angmomentum)
plt.xlabel('Time')
plt.ylabel('Angular Momentum')


plt.show()