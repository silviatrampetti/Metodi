import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize
from scipy import integrate

df = pd.read_csv('fit_data.csv')
#print(df)

plt.plot(df['x'],df['y'], color= 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


def lognorm(x,sigma,mu):
	return (np.exp(np.e,-(np.log(x)-mu)**2)/(2*sigma**2))/(x*sigma*(2*np.pi)**0.5)

"""
#lognorm cumulativa
def lognorm(x,sigma,mu):
	int = np.array([0])
	for i in range(1,len(x)):
		int = np.append(int, integrate.simpson(1/x[:i]*np.exp(np.e, (-(np.log(x[:i])-mu)**2)/(2*sigma**2)), x[:i]))
	return 1/(sigma * 2*np.pi) * int 
"""

par, cov = optimize.curve_fit(lognorm, df['x'], df['y'])
yfit = lognorm(df['x'], par[0], par[1])

plt.plot(df['x'],df['y'], color='red')
plt.plot(df['x'],yfit, color= 'blue')
#plt.xscale('log')
#plt.yscale('log')
plt.show()

