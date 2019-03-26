# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 06:09:44 2018

@author: dell
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data_set = pd.read_csv('Mall_Customers.csv')

X= data_set.iloc[:,[2,3]].values
y= data_set.iloc[:,4].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size = 0.75, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train =sc.fit_transform(X_train)
X_test =sc.transform(X_test)

# create the svm model 

from sklearn.svm import SVC
classifier =SVC(kernel ="poly",degree =5 ,random_state=0)
classifier.fit(X_train,y_train)

y_pred =classifier.predict(X_test)
from sklearn.metrics import confusion_matrix
cm =confusion_matrix(y_test,y_pred)

# visualision the test set result 

from matplotlib.colors import ListedColormap
X_set , y_set  =X_test ,y_test 

X1 ,X2 = np.meshgrid(np.arange(start = X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01), np.arange(start = X_set[:,1].min()-1,stop=X_set[:,1].max()+1,step=0.01))

plt.contourf(X1,X2,classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha =0.75 ,cmap =ListedColormap(('red','green')))

plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],c=ListedColormap(('red','green'))(i),label=j)


plt.title("SVM(test,set)")
plt.xlabel("Age")
plt.ylabel("salary")
plt.legend()
plt.show()


















