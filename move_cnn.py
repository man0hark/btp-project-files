# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:00:53 2021

@author: Sowrappa
"""

import shutil
import os
src="D:/extra_audio/cnn_feat2"
dst="D:/extra_audio/new_cnn"
for i in range(100000):
    file=str(i+1)+".csv"
    old=os.path.join(src,file)
    new=os.path.join(dst,file)
    shutil.move(old,new)
    
    