import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


no_readings=10000
gap=1                       #gap b/w each plotted time
start=0                     #starting value
mu=0                        #mean for random variable
sigma=10                #sigma for random variable




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
        

def fit_error_rms(actual,fit):
    error=np.empty([len(actual),], dtype=float)
    for i in range(len(actual)):
        error[i]=((actual[i]-fit[i])**2)
    return error
    


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
        fit[i]=7*(freqs1[i])**(-2)
    else:
        fit[i]=0

K_num=0
K_denom=0
for i in range(len(psd1)):
    if freqs1[i]!=0:
        K_denom+=(freqs1[i])**(-4)
        K_num+=((freqs1[i])**(-2))*psd1[i]
K=K_num/K_denom
fit3=np.empty([len(freqs1),], dtype=float)
for i in range(len(freqs1)):
    if freqs1[i]!=0:
        fit3[i]=K*(freqs1[i])**(-2)
    else:
        fit3[i]=0
print(K)

#e_guess= fit_error_rms(psd1,fit)
#e_calc= fit_error_rms(psd1,fit3)

plt.subplot(1,3,2)
plt.semilogx(freqs1, psd1,'r-')
plt.semilogx(freqs2, psd2,'b-')
#plt.semilogx(freqs1, fit,'go')                     #guessed coeff
plt.semilogx(freqs1, fit3,'mo')                        #calculated coeff
plt.title('PSD: power spectral density')
plt.xlabel('Frequency')
plt.ylabel('Power')


'''
plt.subplot(1,3,3)
plt.plot(freqs1, psd1,'r-')
plt.plot(freqs1, fit,'b-')'''

plt.show()