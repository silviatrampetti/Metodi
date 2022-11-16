import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import fft
from scipy import optimize

#leggere dati
df_w = pd.read_csv('data_sample1.csv')
df_p = pd.read_csv('data_sample2.csv')
df_r = pd.read_csv('data_sample3.csv')

#grafico segnali input
plt.plot(df_w['time'],df_w['meas'], color = 'slategrey')
plt.plot(df_p['time'],df_p['meas'], color = 'pink')
plt.plot(df_r['time'],df_r['meas'], color = 'red')
plt.show()

#trasformate di Fourier e spettri di potenza
#white
punti_w = np.copy(df_w['meas'])
ft_w = fft.fft(punti_w)
freq_w = fft.fftfreq(len(ft_w), d=1)
freq_w2 = freq_w[1:len(freq_w)//2]
spot_w = np.absolute(ft_w)**2
spot_w2 = spot_w[1:len(spot_w)//2]
#pink
punti_p = np.copy(df_p['meas'])
ft_p = fft.fft(punti_p)
freq_p = fft.fftfreq(len(ft_p), d=1)
freq_p2 = freq_p[1:len(freq_p)//2]
spot_p = np.absolute(ft_p)**2
spot_p2 = spot_p[1:len(spot_p)//2]
#red
punti_r = np.copy(df_r['meas'])
ft_r = fft.fft(punti_r)
freq_r = fft.fftfreq(len(ft_r), d=1)
freq_r2 = freq_r[5:len(freq_r)//2]
spot_r = np.absolute(ft_r)**2
spot_r2 = spot_r[5:len(spot_r)//2]

"""
#grafico spettri di potenza (prima metà)
fig,ax=plt.subplots(3,1, figsize=(5,15))
ax[0].plot(freq_w2, spot_w2, color = 'slategrey')
ax[1].plot(freq_p2, spot_p2, color = 'pink')
ax[2].plot(freq_r2, spot_r2, color = 'red')
ax[0].set_yscale('log')
ax[1].set_yscale('log')
ax[2].set_yscale('log')
plt.show()
"""

#definizione funzione fit
def fit(freq,a,b):
    return a/freq**b

#fit
par_w, cov_w = optimize.curve_fit(fit, freq_w2, spot_w2)
par_p, cov_p = optimize.curve_fit(fit, freq_p2, spot_p2)
par_r, cov_r = optimize.curve_fit(fit, freq_r2, spot_r2)
y_w = fit(freq_w2, par_w[0], par_w[1])
y_p = fit(freq_p2, par_p[0], par_p[1])
y_r = fit(freq_r2, par_r[0], par_r[1])

fig,ax=plt.subplots(3,1, figsize=(5,15))
ax[0].plot(freq_w2, spot_w2, color = 'slategrey')
ax[0].plot(freq_w2, y_w, color = 'blue')
ax[1].plot(freq_p2, spot_p2, color = 'pink')
ax[1].plot(freq_p2, y_p, color = 'blue')
ax[2].plot(freq_r2, spot_r2, color = 'red')
ax[2].plot(freq_r2, y_r, color = 'blue')
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
plt.show()

#parametri funzione fit
print(par_w[0], par_w[1])
print(par_p[0], par_p[1])
print(par_r[0], par_r[1])

#confronto rumori
plt.plot(freq_w2, spot_w2, color = 'slategrey', label = '1 set dati')
plt.plot(freq_p2, spot_p2, color = 'pink', label = '2 set dati')
plt.plot(freq_r2, spot_r2, color = 'red', label = '3 set dati')
plt.plot(freq_w2, y_w, color = 'black', label = 'fit white')
plt.plot(freq_p2, y_p, color = 'purple', label = 'fit pink')
plt.plot(freq_r2, y_r, color = 'orange', label = 'fit red')
#plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
