#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math

if(len(sys.argv) != 4):
    print "input:df-file,idf-file,N"
    sys.exit(0) 

fin = open(sys.argv[1],"r")
fout = open(sys.argv[2],"w")
N = int(sys.argv[3]) * 1.0


for line in fin:
    sp = line.split()
    sp[1] = math.log(N/int(sp[1]))
    fout.write(sp[0] + ' ' + str(sp[1])+'\n')
fin.close()
fout.close()
