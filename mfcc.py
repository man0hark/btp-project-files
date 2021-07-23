# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:42:34 2021

@author: Sowrappa
"""

from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
import os 
for count, filename in enumerate(os.listdir("dataset")):
    src =os.path.join("dataset",filename)
    (rate,sig) = wav.read(src)
    sig=sig/np.abs(np.max(sig))
    mfcc_feat = mfcc(sig,rate)
    file=str(count+1)+".txt"
    dst=os.path.join("mfcc",file)
    np.savetxt(dst,mfcc_feat)