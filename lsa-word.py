import re
import os
import sys
import numpy as np
from numpy import linalg as nplg
from scipy import linalg as sclg
from scipy.sparse import linalg
from scipy import sparse as sp

fwl = open("/home/ec2-user/git/statresult/wordslist_dsw.txt","r")
wtol = {}
itow = {}
i = 0
for line in fwl:
    line = line.strip('\n')
    wtol[line] = i
    itow[i] = line
    i = i + 1
fwl.close()


a = np.load('/home/ec2-user/data/classinfo/vt.npy')

while True:
    w = ''
    c = 0
    w = raw_input('w:')
    c =  int(raw_input('c:'))
    print w
    print a[c][wtol[w]]
    print a[:,wtol[w]].max()
    print a[:,wtol[w]].average()
