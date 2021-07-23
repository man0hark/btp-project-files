# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:50:39 2021

@author: Sowrappa
"""

import os 
import sys
for count, filename in enumerate(os.listdir("cnn_frame")): 
    dst =str(count+1) + ".wav"
    src =os.path.join("cnn_frame",filename) 
    dst =os.path.join("master_1",dst)
    os.rename(src, dst)
    if count==39999:
        sys.exit("done")
    