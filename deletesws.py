#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
if(len(sys.argv) < 3):
   sys.exit(0) 

sw = set()

fsw = open("/home/ec2-user/git/statresult/stopword4.txt","r")
for line in fsw:
    sw.add(line.strip('\n'))
fsw.close()
#fin = open(sys.argv[1],"r")
#fout = open(sys.argv[2],"w")
ftype = int(sys.argv[2])

for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        filename = root + '/' + name
        if filename[len(filename)-2] == 'x':
            fin = open(filename,"r")
            fout = open(filename+".dsw","w")
            for line in fin:
                if ftype > 1:
                    term = line.strip('\n')
                    if term not in sw:
                        fout.write(line)
                else:
                    sp = line.split()
                    if(len(sp) < 2):
                        fout.write(line)
                    elif (sp[ftype] not in sw):
                        fout.write(line)
            fin.close()
            fout.close()
