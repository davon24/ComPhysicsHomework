from numpy import *
import numpy as np
import matplotlib.pyplot as plt

numwalks = 6400

x=zeros([numwalks])
y=zeros([numwalks])

xcir=zeros([numwalks])
ycir=zeros([numwalks])

x[0]=0
y[0]=0

random.seed(1) 
for j in range(numwalks):
    p = random.rand()
    q = random.rand()
    theta1 = 2*pi*p
    theta2 = 2*pi*q
		
    dx = cos(theta1)
    dy = sin(theta2)
		
    x[j] = x[j]+dx
    y[j] = y[j]+dy
    if sqrt((x[j])**2 + (y[j])**2) < 1:
        xcir[j] = x[j]
        ycir[j] = y[j]
        
ratio = (np.count_nonzero(xcir)+0.0)/numwalks

print('There are %i points within the circle.' % np.count_nonzero(xcir))
print('The fraction of points that are in the circle is: %f' % ratio)

limaxes = [-1.0, 1.0, -1.0, 1]

plt.figure()
plt.scatter(x,y)
plt.axis(limaxes, 'equal')
plt.show()
plt.figure()
plt.scatter(xcir,ycir)
plt.axis(limaxes, 'equal')
plt.show()