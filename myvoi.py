#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:00:49 2019

@author: chenna
"""
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
fs,data=wav.read('/home/chenna/Desktop/Record_0002.wav')
fs=np.float(fs)
print(fs,len(data),data)
t=np.arange(0,len(data)/fs,1/fs)
plt.plot(data)
plt.show()
#wav.warite('new_myvoice.wav',0.5*fs)