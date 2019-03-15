import random
import numpy as np
#import pandas as pd
import math
import matplotlib.pyplot as plt


N = 500        # Number of points taken into consideration
n = int(N/2)


output_x=[]
for i in range(N):
#    output_x.append(random.randrange(-2,3)/14.375)
    output_x.append(5+random.random())
#output_y=df['output_y']
#output_z=df['output_z']
#time    =df['time']
time=[]
#tau_not = 0.034  #sec
tau_not=0.25
for i in range(N):
    if i==0: 
        time.append(tau_not)
    else:
        time.append(time[i-1]+tau_not)
    
print (output_x)
print()
print()
print (time)







x_var=output_x
no_readings=N
x_f=1/tau_not

x_var_xaxis=np.arange(0,no_readings/x_f,1/x_f)

x_readings=plt.figure(figsize=(40,10))
plt.subplot(221)
plt.plot(x_var_xaxis,x_var,'r-')
#plt.plot(x_var_xaxis,y_var,'g-')
#plt.plot(x_var_xaxis,z_var,'b-')
#x_readings.savefig('x_readings.pdf')

'''calculate and store Allan Variance'''
def allan(no_readings,x_var1):
    x_allan=[]
    x_allan_xaxis=[]
    for m in range(1,math.ceil((no_readings-1)/2)):               #changed plus to -
        variance=0
#        for i in range(0,no_readings-m+1):
#            variance+=((sum(x_var1[i:i+m])-sum(x_var1[i-1:i-1+m]))*x_f/(m))**2
#        variance/=2*no_readings/m
#        x_allan.append(variance/(no_readings-m))
        
        
        for j in range(1,no_readings-2*m+1):             #changed range to 1 onwards to include N-2m
            for i in range(j,j+m):                      #changed range
                variance+=(sum(x_var1[i:i+m+1])-sum(x_var1[i+m:i+2*m+1])*x_f/m)**2
        variance/=2*(m**2)*(no_readings-2*m)                ####SIMPLY PUT +1
        x_allan.append(variance**0.5)
        x_allan_xaxis.append(m/x_f)
    return x_allan,x_allan_xaxis
    
def allan_omega(no_readings,x_var1):
    x_allan=[]
    x_sum=[]
    x_allan_omega_xaxis=[]
    for y in range(1,len(x_var1)+1):
        x_sum.append(sum(x_var1[:y]))
    for m in range(1,math.ceil((no_readings-1)/2)):
        variance=0
        for i in range(1,no_readings-2*m+1):
            variance+=(x_sum[i+2*m-1]-2*x_sum[i+m-1]+x_sum[i-1])**2
            variance/=2*((m/x_f)**2)*(no_readings-2*m)
        x_allan.append(variance**0.5)
        x_allan_omega_xaxis.append(m/x_f)
    return (x_allan,x_allan_omega_xaxis)

x_allan, x_allan_xaxis=allan(no_readings,x_var)
x_allan_omega, x_allan_omega_xaxis=allan_omega(no_readings,x_var)
#y_allan=allan(no_readings,y_var)
#z_allan=allan(no_readings,z_var)

#x_allan_xaxis=np.arange(0,math.ceil((no_readings-1)/2)/x_f,1/x_f)
plt.subplot(223)

plt.loglog(x_allan_xaxis,x_allan,'r-')
plt.loglog(x_allan_omega_xaxis,x_allan_omega,'b-')
plt.show()
#plt.loglog(x_allan_xaxis,y_allan,'g-')
#plt.loglog(x_allan_xaxis,z_allan,'b-')
plt.grid(True)
#print(x_allan)

'''Check Frequency'''
