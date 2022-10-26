#distanza percorsa in funzione del tempo

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate

df = pd.read_csv('vel_vs_time.csv')

plt.plot(df['t'],df['v'])
plt.xlabel('tempo')
plt.ylabel('velocità')
plt.show()

s= integrate.simpson(df['v'],df['t'])
print('s=',s)

array_vel = df['v']
array_t = df['t']
array_s = np.array([0])

for i in range(1,len(array_vel)):
    array_s =np.append(array_s, integrate.simpson(array_vel[:i],array_t[:i]))
    #print(array_s[i])

plt.plot(array_s, array_t)
plt.xlabel('tempo')
plt.ylabel('spazio')
plt.show()
