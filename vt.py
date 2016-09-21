#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp
import sys
print "start"
a = np.load('/home/ec2-user/data/classinfo/vt-kk.npy')	
print "load completed"
sys.stdout.flush()
a = np.transpose(a)
np.save('/home/ec2-user/data/classinfo/vt-kk-v.npy',a)
print "over"
