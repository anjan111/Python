# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 07:32:32 2019

@author: dell
"""
# import data science libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_file = pd.read_csv('data_with_headers.csv')
time =data_file['time']
sensors =data_file.ix[:,'s1':'s4']
time =time -time[0]
avg =np.mean(sensors,1) # 2D
avg1 =np.mean(sensors,0)
new_data =[time,sensors,avg]
result =pd.concat(new_data,axis =1)
result.to_csv('result.csv')
result.to_excel('result.xlsx')

plt.figure(1)
plt.plot(time,sensors['s3'],'r-')
plt.plot(time,avg,'b.')
plt.legend(['sensor 2','avg'])
plt.xlabel('time in sec')
plt.ylabel('sensor')
plt.savefig("my_pandas_fig.png")
plt.show()