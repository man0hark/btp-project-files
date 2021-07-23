# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:58:59 2021

@author: Sowrappa
"""

import numpy as np
import os
import pandas as pd
s1="D:/extra_audio/full_csv_label"
s2="D:/extra_audio/full_csv_feat"
a1="D:/extra_audio/full_0_label"
a2="D:/extra_audio/full_0_feat"
for i in range(60000):
    dst=str(i+1)+".csv"
    s_1=os.path.join(s1,dst)
    s_2=os.path.join(s2,dst)
    f1=pd.read_csv(s_1,header=None)
    f2=pd.read_csv(s_2,header=None)
    x1=f1.to_numpy()
    x2=f2.to_numpy()
    y1=[]
    y2=[]
    for i in range(len(x1)):
        if x1[i]==0:
            y1.append(x1[i])
            y2.append(x2[i])
    d1=pd.DataFrame(y1)
    d2=pd.DataFrame(y2)
    d1.to_csv(os.path.join(a1,dst), header=False, index=False) 
    d2.to_csv(os.path.join(a2,dst), header=False, index=False) 
    del f1,f2,x1,x2,y1,y2,d1,d2