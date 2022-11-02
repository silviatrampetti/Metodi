#oscillatore armonico

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def V_func(x,k):
    return k*x**6

k=1
m=10
cost = np.sqrt(8*m)

x0=np.empty(0) #punto da cui parte
T=np.empty(0) #periodo

for i in np.arange(1,30,0.001):
    x0=np.append(x0,i)
    x=np.arange(0,i,0.001)
    V0=V_func(i,k)
    V=V_func(x,k)
    T=np.append(T,cost*integrate.simpson(1/np.sqrt(V0-V),x))

plt.plot(x[:len(T)],T)
plt.xlabel('x0')
plt.ylabel('T')
plt.show()
