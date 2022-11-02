#oscillatore armonico

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def periodo(m,k,x):
    return np.sqrt(8*m)*integrate.simpson(1/(np.sqrt(0.5*m*np.gradient(x)**2*k*x**6)),x)

xx0 = np.arange(10)
kk=10
mm=20
T=np.array([0])

for i in range(len(xx0)):
    T=np.append(T,periodo(mm,kk,xx0[i]))







'''
def V0_f(m,v,V):
    return 0.5*m*v**2 + V

def sqrt_f(V0,V):
    return np.sqrt(V0-V)

kk=0.5
mm=1

x0 = np.arange(-5,5)
xx = 
vv=np.gradient(xx)
V=V_f(kk,xx)
V0=V0_f(mm,vv,V)
f=sqrt_f(V0,V)
T=np.array([0])

for i in range(1,len(xx)):
    T=np.append(T,np.sqrt(8*mm)*integrate.simpson(f[:i],xx[:i]))

plt.plot(xx,T)
plt.xlabel('x')
plt.ylabel('V')
plt.show()
'''
