#!/usr/bin/env python
# -*- coding: utf-8 -*-

#group words with nearest dist

import os
import sys
import math
import re
from os import path
import numpy as np
from scipy import spatial

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from pythonlib import semantic as sm
from sortedcontainers import SortedDict

if len(sys.argv) != 3:
    print 'input:semantic-flie,output-file'
    sys.exit(1)

a = np.load(sys.argv[1])
a = np.transpose(a)
fout = open(sys.argv[2],'w')
l = len(a)
limit = l/2
tempp = SortedDict()
upwords = set()
l1 = []
l2 = []

while len(upwords) < l - 2:
    for i in range(0,l):
        if i in upwords:
            continue
        for j in range(i+1,l):
            if j in upwords:
                continue
            dist = spatial.distance.cosine(a[i],a[j])
            tempp[dist] = (i,j)
            if len(tempp) > limit:
                tempp.popitem()
    dicl = len(tempp)
    for i in range(0,dicl):
        tmp = tempp.popitem(last=False)
        if tmp[1][0] not in upwords and tmp[1][1] not in upwords:
            l1.append(tmp[1])
            upwords.add(tmp[1][0])
            upwords.add(tmp[1][1])
    print 'l1len:',len(l1)
    sys.stdout.flush() 

l = len(l1)
upwords = set()

while len(upwords) < l - 2:
    for i in range(0,l):
	ii = l1[i]
        if ii in upwords:
            continue
        for j in range(i+1,l):
            jj = l1[j]
            if jj in upwords:
                continue
            dist = spatial.distance.cosine(a[ii[0]]+a[ii[1]],a[jj[0]]+a[jj[1]])
            tempp[dist] = (ii,jj)
            if len(tempp) > limit:
                tempp.popitem()
    dicl = len(tempp)
    for i in range(0,dicl):
        tmp = tempp.popitem(last=False)
        if tmp[1][0] not in upwords and tmp[1][1] not in upwords:
            l2.append(tmp[1])
            upwords.add(tmp[1][0])
            upwords.add(tmp[1][1])
    print 'l2len:',len(l2)
    sys.stdout.flush() 
for i in l2:
    fout.write(' '.join(map(str,i[0]+i[1]))+'\n')
