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
fout =open("/mnt/nas2a/ko/totaldf.txt","w") 
fin = open("/mnt/nas2a/ko/NTCIR.txt","r")
print("start")
for line in fin:
	num = num + 1
	if line[0] == '@':
		continue
	term = line.split()[1]
	if term in dict:
		dict[term] = dict[term] + 1
	else:
		dict[term] = 1
fin.close()
for term in dict:
	fout.write(term+" "+str(dict[term])+"\n")
fout.close()
print("over")
