# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:07:46 2021

@author: Sowrappa

from shutil import copyfile
import os
ds="D:/extra_audio/test"
d = "D:/extra_audio/aac/id01418"
for (root,dirs,files) in os.walk(d, topdown='true'): 
    for filename in files:  
        #src=os.path.join(root,filename)
        #dst=os.path.join(ds,filename)
        #copyfile(src, dst)
        print(filename)
#str=root+dirs+files
#print(str)
"""  
import shutil
from shutil import copyfile
import glob
import os
import sys
ds="D:/extra_audio/cnn_data"
count=0
for name in glob.glob('aac/*'):
    print(name)
    print("...")
    for (root,dirs,files) in os.walk(name, topdown='true'): 
        for filename in files:
            if count==40000:
                sys.exit("40k done")
            filename1=str(count+1) + ".m4a"
            src=os.path.join(root,filename)
            dst=os.path.join(ds,filename1)
            copyfile(src, dst)
            print(count)
            count=count+1 
shutil.rmtree(name)