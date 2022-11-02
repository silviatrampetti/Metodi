import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize

df = pd.read_csv("fit_data.csv")
print(df)

y_err= np.sqrt(df['y'])

plt.plot(df['x'],df['y'], color = 'tomato')
plt.xlabel('x')
plt.ylabel('y')
#plt.xscale("log")
#plt.yscale('log')
plt.show()

def lognorm(x,mu,sigma,A):
    z = np.log(x)
    p = A*(np.pi*sigma)*np.exp(-0.5*((z-mu)/sigma)**2)
    return p

par, cov = optimize.curve_fit(lognorm, df['x'],df['y'],sigma = y_err,absolute_sigma = True)
yfit = lognorm(df['x'],par[0],par[1],par[2])

print('mu =', par[0], 'sigma =', par[1], 'A=' , par[2])

plt.errorbar(df['x'],df['y'],yerr = y_err, fmt='o',label = 'dati', color = 'tomato')
plt.errorbar(df['x'],yfit, label = 'fit', color = 'blue')
#plt.xscale('log')
#plt.yscale('log')
plt.legend()
plt.show()



chi2 = np.sum((yfit-df['y'])**2/df['y'])
ni = len(df['x'])-len(par)
chi_r=chi2/ni

print("chi2 =", chi2, "gradi di libertà=", ni, "chi2 ridotto=", chi_r)

