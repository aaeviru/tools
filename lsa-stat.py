import re
import os
import sys
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp

a = np.load('/home/ec2-user/data/classinfo/vt.npy')
print len(a)
print a.shape[1]
for i in range(0,a.shape[0]):
    print a[i].mean(),a[i].max()
    
