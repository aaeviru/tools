#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
if(len(sys.argv) < 3):
   print "input:input-folder ftype"
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
        if filename[len(filename)-1] == 'q':
            fin = open(filename,"r")
            lines = fin.readlines()
            fin.close()
            fout = open(filename,"w")
            for line in lines:
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
            fout.close()
