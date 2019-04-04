import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

no_readings=10000
gap=1                       #gap b/w each plotted time
start=0                     #starting value
mu=0                        #mean for random variable
sigma=20                     #sigma for random variable




time=np.linspace(0,gap*100,num=no_readings)
signal1=np.empty([no_readings,], dtype=float)
signal1[0]=start
signal2=np.empty([no_readings,], dtype=float)
signal2[0]=start


def random_walk(no_readings,signal):
    for i in range(1,no_readings):
        signal[i]=(signal[i-1]+np.random.normal(mu, sigma, 1))
def gaussian_walk(no_readings,signal):
    for i in range(1,no_readings):
        signal[i]=(np.random.normal(mu, sigma, 1))


random_walk(no_readings, signal1)
gaussian_walk(no_readings, signal2)

plt.subplot(1,3,1)
plt.plot(time,signal1,'r-')
plt.plot(time,signal2,'b-')
plt.title('Random and gaussian Walk')
plt.xlabel('Time')
plt.ylabel('SIgnal')
 



freqs1, psd1 = signal.welch(signal1)
freqs2, psd2 = signal.welch(signal2)



fit=np.empty([len(freqs1),], dtype=float)
for i in range(len(freqs1)):
    if freqs1[i]!=0:
        fit[i]=(freqs1[i])**(-2)
    else:
        fit[i]=0

plt.subplot(1,3,2)
plt.semilogx(freqs1, psd1,'r-')
plt.semilogx(freqs2, psd2,'b-')
plt.semilogx(freqs1, fit,'go')
plt.title('PSD: power spectral density')
plt.xlabel('Frequency')
plt.ylabel('Power')

'''
plt.subplot(1,3,3)
plt.plot(freqs1, psd1,'r-')
plt.plot(freqs1, fit,'b-')'''

plt.show()