# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:56:57 2021

@author: Sowrappa
"""

import shutil
from shutil import copyfile
import glob
import os
import sys
import pandas as pd
s1="D:/extra_audio/100k_label.csv"
d1="D:/extra_audio/100k0"
d2="D:/extra_audio/cnn_frame"
d3="D:/extra_audio/100k1"
for i in range(100000):
    f1=pd.read_csv(s1,header=None)
    x1=f1.to_numpy()
    for i in range(len(x1)):
        if x1[i]==0:
            file=str(i+1)+".wav"
            dst=os.path.join(d1,file)
            src=os.path.join(d2,file)
            shutil.move(src, dst)
        else:
            file=str(i+1)+".wav"
            dst=os.path.join(d3,file)
            src=os.path.join(d2,file)
            shutil.move(src, dst)  