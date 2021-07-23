# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 09:43:12 2021

@author: Sowrappa
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import numpy as np

y_train = pd.read_csv('D:/test_label.csv',header=None)
full_0=pd.read_csv('D:/extra_audio/only_0_label/only_0_label.csv',header=None)
full_0_feat=pd.read_csv('D:/extra_audio/only_0_feat/only_0_feat.csv',header=None)
x_train=pd.read_csv('D:/test/py_feat/test_feat_py.csv',header=None)
frames = [y_train, full_0]
f1 = [x_train,full_0_feat]
result = pd.concat(frames)
r1=pd.concat(f1)
x1=result.to_numpy()
x2=r1.to_numpy()
count=0
y=[]
for i in range(len(x1)):
  if x1[i]==1:
    y.append(i)
    count=count+1
    if count == 270000:
      break
a=np.delete(x1, y, axis=0)
b=np.delete(x2,y,axis=0)
a1=pd.DataFrame(a)
b1=pd.DataFrame(b)
a1.to_csv("balanced_test_label.csv",index=None,header=None)
b1.to_csv("balanced_test_feat.csv",index=None,header=None)