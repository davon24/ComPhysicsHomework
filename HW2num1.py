from numpy import *
import matplotlib.pyplot as plt

numtimes = 15
a = 1
b1 = 0.25
b2 = 0.40
b3 = 0.75
b4 = 0.9
params1 = array([a,b1])
params2 = array([a,b2])
params3 = array([a,b3])
params4 = array([a,b4])
times = array([i for i in range(numtimes)])
N = zeros(numtimes)
N2 = zeros(numtimes)
N3 = zeros(numtimes)
N4 = zeros(numtimes)

N[0] = 0.5
N2[0] = 0.5
N3[0] = 0.5
N4[0] = 0.5

def dN(N,params):
    a = params[0]
    b = params[1]
    dN = a*N - b*N**2
    return dN

for i in range(1,numtimes):
    N[i] = N[i-1] + dN(N[i-1],params1)
    N2[i] = N2[i-1] + dN(N2[i-1],params2)
    N3[i] = N3[i-1] + dN(N3[i-1],params3)
    N4[i] = N4[i-1] + dN(N4[i-1],params4)


plt.semilogy(times,N,label ="b = 0.25")
plt.plot(times,N2,label ='b = 0.4')
plt.plot(times,N3,label ='b = 0.75')
plt.plot(times,N4,label ='b = 0.9')
plt.legend(loc = 'upper left')
plt.xlabel('time')
plt.show()