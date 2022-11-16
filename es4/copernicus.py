import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import fft, optimize

#leggere dati da file
df = pd.read_csv('copernicus_PG_selected.csv')
print(df.columns)

#grafico dati
plt.plot(df['date'], df['mean_co_ug/m3'], label = 'CO', color = 'slategrey')
#plt.plot(df['date'], df['mean_nh3_ug/m3'], label = 'NH3', color = 'green')
#plt.plot(df['date'], df['mean_no2_ug/m3'], label = 'NO2', color = 'orange')
#plt.plot(df['date'], df['mean_o3_ug/m3'], label = 'O3', color = 'skyblue')
#plt.plot(df['date'], df['mean_pm10_ug/m3'], label = 'PM10', color = 'brown')
#plt.plot(df['date'], df['mean_pm2p5_ug/m3'], label = 'PM2.5', color = 'purple')
#plt.plot(df['date'], df['mean_so2_ug/m3'], label = 'SO2', color = 'red')
plt.yscale('log')
plt.legend()
plt.show()

#trasformata di Fourier e spettro di potenza CO
dati_CO = np.copy(df['mean_co_ug/m3'])
ft = fft.fft(dati_CO)
freq = fft.fftfreq(len(dati_CO),d=1)
freq2 = freq[1:len(freq)//2]
spot = np.absolute(ft)**2
spot2 = spot[1:len(spot)//2]

#grafico spettro di potenza vs frequenza
plt.plot (freq2, spot2,'o', color = 'slategrey')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('f')
plt.ylabel('|ck|^2')
plt.show()

#grafico spettro di potenza vs periodo
per = 1/freq2
plt.plot (per, spot2,'o', color = 'slategrey')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('f')
plt.ylabel('|ck|^2')
plt.show()

#filtri
ftmask1 = np.absolute(ft)**2 < 1.5e7
#ftmask2 = np.absolute(ft)**2 < 2e6

filtred_ft1 = ft.copy()
filtred_ft1[ftmask1] = 0
#filtred_ft2 = ft.copy()
#filtred_ft2[ftmask2] = 0

ft_filtred1 = fft.ifft(filtred_ft1)
#ft_filtred2 = fft.ifft(filtred_ft2)

#grafico trasformata inversa
plt.plot(df['date'], df['mean_co_ug/m3'], label = 'CO', color = 'slategrey')
plt.plot(df['date'], ft_filtred1, color = 'blue')
#plt.plot(df['date'], ft_filtred2, color = 'green')
plt.show()
