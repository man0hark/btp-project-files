# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:09:04 2021

@author: Sowrappa
"""
from shutil import copyfile
import glob
import sys
import os
ds="D:/extra_audio/100k1_final"
count=1
for name in glob.glob('D:/extra_audio/100k1/*.wav'):
    if count == 4960:
        sys.exit("done")
    new=str(count)+".wav"
    dst=os.path.join(ds, new)
    copyfile(name, dst)
    count=count+1
    