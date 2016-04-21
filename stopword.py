# -*- coding: utf-8 -*-
import os
import os.path
import sys
import re
dict = {}

for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
               	filename = root + '/' + name
               	if filename[len(filename)-1] == 'f':
			fin = open(filename,"r")
			print filename
			for line in fin.readlines():
        			ssplit = line.split()
			        if dict.has_key(ssplit[0]):
           			     dict[ssplit[0]]=dict[ssplit[0]]+int(ssplit[1])
  				else:
       				        dict[ssplit[0]]=int(ssplit[1])
			fin.close()

fout = open(sys.argv[1]+"stopword.txt","w")
for i in dict:
	fout.write(i +" "+ str(dict[i])+"\n")
fout.close()
