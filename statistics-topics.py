# -*- coding: utf-8 -*-
import os
import os.path
import sys
import re
dict = {}
num = filenum = nnum = 0
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
		list = []
               	filename = root + '/' + name
               	if filename[len(filename)-1] == 't':
			filenum = filenum + 1
			fin = open(filename,"r")
			for line in fin:
				line = line.strip()
				num = num + 1
			        if dict.has_key(line):
           			     dict[line]=dict[line]+1
  				else:
       				        dict[line]=1
				if line not in list:
					nnum = nnum + 1
					list.append(line)
			fin.close()
dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
fout = open("topic-statics.txt","w")
print filenum
print num*1.0/filenum
print nnum*1.0/filenum
print len(dict)
for i in range(0,len(dict)):
	fout.write(dict[i][0] + " " + str(dict[i][1])+"\n")
fout.close()


