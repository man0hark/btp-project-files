# -*- coding: utf-8 -*-
"""
Created on Thu May  6 00:47:26 2021

@author: Sowrappa
"""

from multiprocessing import Process
from scipy.io import wavfile
import numpy as np
import os
import python_speech_features
import glob
d="D:/extra_audio/cnn_frame"
e="D:/extra_audio/cnn_feat2"
count=1
def pro():
    for count, filename in enumerate(os.listdir("cnn_frame")):
        dst=str(count+1)+".wav"
        dst_1=str(count+1)+".csv"
        dst1=os.path.join(d,dst)
        sr, y = wavfile.read(dst1)
        y1=y/np.abs(np.max(y))
        mfcc_speech = python_speech_features.mfcc(signal=y1, samplerate=sr)
        dst1=os.path.join(e,dst_1)
        np.savetxt(dst1,mfcc_speech, delimiter=',')
        print(count+1)

if __name__=='__main__':
    p =Process(target=pro)
    p.start()
    p.join()