from numpy import *
import matplotlib.pyplot as plt

def derivatives(variables,params,t): #We are defining a function that returns derivatives

    x=variables[0]
    y=variables[1]
    vx=variables[2]
    vy=variables[3]
    
    vt=params[0]

    dx = vx
    dy = vy
    dvx = -vx*sqrt(vx**2 + vy**2)/vt
    dvy = (-vy*sqrt(vx**2 + vy**2)/vt) - 1
        
    return array([dx, dy, dvx, dvy])

    
dt=0.000001
numtimes = 100000
vt = 1
g = 1
tau = vt/g    
times = array([i*dt/tau for i in range(numtimes)])

variables = zeros([numtimes,4])
variables1 = zeros([numtimes,4])
variables2 = zeros([numtimes,4])

x0=0
y0=1
v0=1
theta0 = 20*pi/180.0
vx0=v0*cos(theta0)
vy0=v0*sin(theta0)

theta01 = 19*pi/180.0
vx01=v0*cos(theta01)
vy01=v0*sin(theta01)

theta02 = 21*pi/180.0
vx02=v0*cos(theta02)
vy02=v0*sin(theta02)

variables[0] = array([x0,y0,vx0,vy0])
variables1[0] = array([x0,y0,vx01,vy01])
variables2[0] = array([x0,y0,vx02,vy02])
params = array([vt])
for t in range(1,numtimes):
    df = derivatives(variables[t-1], params, times[t-1])
    df1 = derivatives(variables1[t-1], params, times[t-1])
    df2 = derivatives(variables2[t-1], params, times[t-1])
    variables[t] = variables[t-1]+df*times[t]
    variables1[t] = variables1[t-1]+df1*times[t]
    variables2[t] = variables2[t-1]+df2*times[t]
    if variables[t,1] <= 0.000001:
        variables[t] = variables[t-1]
    if variables1[t,1] <= 0.000001:
        variables1[t] = variables1[t-1]
    if variables2[t,1] <= 0.000001:
        variables2[t] = variables2[t-1]

plt.figure()
plt.subplot(111)
plt.plot(variables[:,0],variables[:,1],label = "theta = 20")
plt.plot(variables1[:,0],variables1[:,1],label = "theta = 19")
plt.plot(variables2[:,0],variables2[:,1],label = "theta = 21")
plt.legend(loc = 'upper right')

plt.show() 
