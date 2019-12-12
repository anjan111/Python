# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 07:45:06 2019

@author: dell
"""
import numpy as np

data_file = np.genfromtxt('data_file.txt',delimiter=',')

time = data_file[:,][:,0]

time =time-time[0]

sensors=data_file[:,][:,1:5]

avg = np.mean(sensors,axis =1)

avg2 =np.mean(sensors,axis =0)

print(time.shape,time.ndim)

print(sensors.shape,sensors.ndim)

print(avg.shape,avg.ndim)

print(avg2.shape,avg2.ndim)

time_col =time.reshape(-1,1)

print(time_col.shape,time_col.ndim)

avg_col =avg.reshape(-1,1)

print(avg_col.shape,avg_col.ndim)

# export 
export_data = np.concatenate((time_col,sensors,avg_col),axis=1)
np.savetxt('export_data_numpy.txt',export_data,delimiter=",")

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(time,sensors[:,][:,0],'r*')
plt.plot(time,avg,'b.')
plt.legend(['sensor 1','avg'])
plt.xlabel('time in sec')
plt.ylabel('sensor1')
plt.savefig("my_senso1.png")
plt.show()