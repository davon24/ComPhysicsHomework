from numpy import *
import matplotlib.pyplot as plt

numpoints = 3000
theta0 = 70*pi/180
v0 = 30
dt= 0.001

vx0 = v0*cos(theta0)
vy0 = v0*sin(theta0)

x = zeros(numpoints)
y = zeros(numpoints)
times = array([dt*i for i in range(numpoints)])

for i in range(numpoints):
    x[i] = vx0*times[i]
    y[i] = vy0*times[i] - 9.8*(times[i]**2)
    if y[i] < 0:
        y[i] = 0
        x[i] = x[i-1]
print x
print y
plt.plot(x,y)
plt.show()