# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import math


'''Read data from file'''
with open("gyroreadings3(s1).txt") as g_read:
    read=g_read.readlines()
#print (read)
x_var=[]
y_var=[]
z_var=[]
no_readings=len(read)
print(no_readings)
for line in read:
    line=line.strip('\n')
    line=line.split('.')
    x_var.append(14.375*int(line[0]))
    y_var.append(14.375*int(line[1]))
    z_var.append(14.375*int(line[2]))
#print(x_var)
#print(y_var)
#print(z_var)  
#x_var1=[14.375*i for i in x_var]
#y_var1=[14.375*i for i in y_var]
#z_var1=[14.375*i for i in z_var]

x_f=100  #change frequency
x_var_xaxis=np.arange(0,no_readings/x_f,1/x_f)
#plt.plot(x_var[:20])
x_readings=plt.figure(figsize=(40,10))
plt.subplot(221)
plt.plot(x_var_xaxis,x_var,'r-')
plt.plot(x_var_xaxis,y_var,'g-')
plt.plot(x_var_xaxis,z_var,'b-')
#x_readings.savefig('x_readings.pdf')

'''calculate and store Allan Variance'''
def allan(no_readings,x_var1):
    x_allan=[]
    for m in range(1,math.ceil((no_readings+1)/2)):
        variance=0
#        for i in range(0,no_readings-m+1):
#            variance+=((sum(x_var1[i:i+m])-sum(x_var1[i-1:i-1+m]))*x_f/(m))**2
#        variance/=2*no_readings/m
#        x_allan.append(variance/(no_readings-m))
        
        
        for j in range(no_readings-2*m):
            for i in range(j+m-1):
                variance+=(sum(x_var1[i:i+m])-sum(x_var1[i+m:i+2*m]))**2
        variance/=2*m**2*(no_readings-2*m)
        x_allan.append(variance/(no_readings-m))
    return x_allan
    
def allan_omega(no_readings,x_var1):
    x_allan=[]
    x_sum=[]
    for y in range(len(x_var1)):
        x_sum.append(sum(x_var1[:y]))
    for m in range(1,math.ceil((no_readings+1)/2)):
        variance=0
        for i in range(no_readings-2*m):
            variance+=(x_sum[i+2*m]-2*x_sum[i+m]+x_sum[i])**2
        x_allan.append(variance)
    return x_allan

x_allan=allan(no_readings,x_var)
y_allan=allan(no_readings,y_var)
z_allan=allan(no_readings,z_var)

x_allan_xaxis=np.arange(0,math.ceil((no_readings-1)/2)/x_f,1/x_f)
plt.subplot(223)

plt.loglog(x_allan_xaxis,x_allan,'r-')
plt.loglog(x_allan_xaxis,y_allan,'g-')
plt.loglog(x_allan_xaxis,z_allan,'b-')
plt.grid(True)
#print(x_allan)

'''Check Frequency'''






