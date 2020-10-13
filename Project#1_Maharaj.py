#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:11:51 2020

@author: jarvis
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np
import numpy.linalg as npl  

einstein_image = imread('einstein.jpg')
                        
X,Y,Z = np.linalg.svd(einstein_image)
for i in [1,10,20,30,40,50,500]:
    Headline1= "Einstein (n= %s)" %i
    newimage1 = np.matrix(X[:, :i])* np.diag(Y[:i])* np.matrix(Z[:i,:])
    plt.imshow(newimage1, cmap='gray')
    plt.title(Headline1)
    plt.savefig('Ein_%s' %i)
