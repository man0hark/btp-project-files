# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:10:00 2021

@author: Sowrappa
"""
from shutil import copyfile
import glob
import os
ds="D:/extra_audio/new_t"
for name in glob.glob('new_test/*'):
    print(name)
    print("...")
    count=0
    for (root,dirs,files) in os.walk(name, topdown='true'): 
        for filename in files:
            filename1=str(count+1) + ".m4a"
            src=os.path.join(root,filename)
            dst=os.path.join(ds,filename1)
            copyfile(src, dst)
            print(filename)
            count=count+1