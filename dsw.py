#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

if(len(sys.argv) != 4):
    print "input:sourefile,outputfile,type[0/1]"
    sys.exit(0) 

wd = set()

fsw = open("/home/ec2-user/git/statresult/wordslist_dsw.txt","r")
for line in fsw:
    wd.add(line.strip('\n'))
fsw.close()
fin = open(sys.argv[1],"r")
fout = open(sys.argv[2],"w")
ftype = int(sys.argv[3])


for line in fin:
    if ftype == 1:
        term = line.strip('\n')
        if term in wd:
            fout.write(line)
    else:
        sp = line.split()
        if(len(sp) < 2):
            fout.write(line)
        elif (sp[ftype] in wd):
            fout.write(line)
fin.close()
fout.close()
