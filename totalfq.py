#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import string
import re
import sys
import unicodedata
import codecs
num = 0
w = []
dict = {}
fout =open("/mnt/nas2a/ko/totalfq.txt","w") 
fin = open("/mnt/nas2a/ko/NTCIR.txt","r")
for line in fin:
	num = num + 1
	if line[0] == '@':
		continue
	term = line.split()[1]
	if term in dict:
		dict[term] = dict[term] + int(line.split()[0])
	else:
		dict[term] = int(line.split()[0])
	print num
	sys.stdout.flush()
fin.close()
for term in dict:
	fout.write(term+" "+str(dict[term])+"\n")
fout.close()
