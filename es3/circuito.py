import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def fode(Vin,Vout):
    return (Vin-Vout)

Vout0=0
RC1 = 1
RC2 = 0.1
RC3 = 0.01

t=np.linspace(0,10,50)
t_int = np.linspace(0,10,50, dtype=int)
Vin = np.empty(0)

for i in range(len(t)):
    if (t_int[i]%2==0):
        Vin = np.append(Vin, 1)
    else:
        Vin = np.append(Vin,-1)

