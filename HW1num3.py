from numpy import *
import matplotlib.pyplot as plt
N = 100
mu = 3.8
x = zeros(N)
narray = array([i for i in range(N)])
x[0] = 0.01

for i in range(N-1):
    x[i+1] = mu*x[i]*(1-x[i])
    
plt.plot(narray,x)
plt.show()