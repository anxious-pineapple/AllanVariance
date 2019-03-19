import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

'''
N = 100         # Number of points taken into consideration
n = int(N/2)


output_x=[]

for i in range(N):
    output_x.append(random.randrange(0,3)/14.375)
#output_y=df['output_y']
#output_z=df['output_z']
#time    =df['time']

time=[]
tau_not = 1  #sec
with open('/home/yuktee/Documents/data_sh41.txt') as fie:
    output_x=fie.readlines()
output_x=[float(i.strip('\n')) for i in output_x]
#output_x=output_x[:2000]
N=len(output_x)
n = int(N/2)

for i in range(N+1):
    if i==0: 
        time.append(0)
    else:
        time.append(time[i-1]+tau_not)
    
print (output_x)
print()
print()
print(time)
'''

tau_not=0.05
N=2000
output_x=[]
time=[]

amp=10                                                              #Sine wave
time_period=5
t=0
for i in range(N):
    output_x.append(amp*math.sin(t*math.pi*2/time_period))
    time.append(t)
    t+=tau_not
output_x=np.array(output_x)
print (t)

def white_noise(f, N, time):
        noise=np.array([math.sqrt(1/f)*math.sin(t*math.pi*2*f) for t in time])
        return noise

def noise_adder(output_x,frequ_list,N,time):
    for i in frequ_list:
        output_x+=white_noise(i,N,time)
    return output_x
plt.subplot(221) 
plt.plot(time,output_x,'y-')   
    
fr=np.linspace(1,5)
plt.subplot(222)                                 #plotting noise
plt.plot(time,noise_adder(np.zeros(N),fr ,N,time),'g-')
output_x=noise_adder(output_x,fr ,N,time)

plt.subplot(223)                                 #plotting signal
plt.plot(time,output_x,'b-')
plt.show()


info=[N, tau_not, output_x] 

def theta(x):           #x is till what number we want the sum
    sum=0   
    mylist2 = list(range(x))
    for i in mylist2:
        sum = sum + output_x[i]*tau_not
    return sum


allan_dev_x=[]
tau_values = list(range(1,math.ceil((N-1)/2) ))                #changes 1+n to math.ceil((no_readings-1)/2
for i in tau_values :
    sum = 0
    mylist1 = list(range(1,N-2*i+1))
    for k in mylist1:
        sum = sum + ((theta(k+2*i) - 2*theta(k+i) + theta(k))**(2))/(2*(i*tau_not)**(2)*(N-2*i))
    adev_x = np.sqrt(sum)
    allan_dev_x.append( adev_x)
    print(i)
    
plt.subplot(224) 
plt.loglog(tau_values, allan_dev_x ,color='r', label='X-output')
plt.xlabel('Tau values')
plt.ylabel('Allan deviation')
plt.legend('X-output')
plt.grid()
plt.show()

