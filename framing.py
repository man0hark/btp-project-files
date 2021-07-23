# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:53:02 2021

@author: Sowrappa
"""
import os
from scipy.io import wavfile
import numpy as np
from scipy.io.wavfile import write
import sys
j=1
full_data="D:/extra_audio/cnn_wav"
frame_data="D:/extra_audio/cnn_frame"
for i in range(40000):
    dst=str(i+1)+".wav"
    s_1=os.path.join(full_data,dst)
    sr, data = wavfile.read(s_1)
    f=int(sr*0.025) #no. of samples in a frame
    #pad the signal so that each frame has equal samples
    if len(data)%f != 0:
        pad=np.pad(data,(0,f-(len(data)%f)))
    else:
        pad=data
    num_frames=np.abs(len(pad))//np.abs(f)
    x=0
    y=400
    a = np.zeros(shape=(num_frames,f))
    i=0
    #frame signal
    for i in range(num_frames):
        a[i]=pad[x:y]
        x=x+400
        y=y+400
    for i in range(a.shape[0]):
        dst1=str(j)+".wav"
        name=os.path.join(frame_data,dst1)
        data=a[i]
        write(name, sr, data.astype(np.int16))
        j=j+1
    del data,sr,a,pad,num_frames 
    