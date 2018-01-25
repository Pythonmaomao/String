# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:42:09 2018

@author: kanjingli
"""
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,4*np.pi,0.01)
b = np.sin(a)

plt.plot(a,b)
plt.show()
