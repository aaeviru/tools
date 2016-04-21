# -*- coding: utf-8 -*-
import os
import os.path
import sys
import re
dict = {}

for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
               	filename = root + '/' + name
               	if filename[len(filename)-1] == 'b' and filename[len(filename)-2] == '.':
			fin = open(filename,"r")
			print filename
			for line in fin.readlines():
        			ssplit = line.split()
			        if dict.has_key(ssplit[0]):
           			     dict[ssplit[0]]=dict[ssplit[0]]+int(ssplit[1])
  				else:
       				        dict[ssplit[0]]=int(ssplit[1])
			fin.close()
dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
fout = open(sys.argv[1]+"toptf.txt","w")
for i in range(0,len(dict)):
	fout.write(dict[i][0] + " " + str(dict[i][1])+"\n")
fout.close()

dict = {}

for root, dirs, files in os.walk(sys.argv[1]):
        for name in files:
                filename = root + '/' + name
                if filename[len(filename)-1] == 's' and filename[len(filename)-2] == '.':
                        fin = open(filename,"r")
                        print filename
                        for line in fin.readlines():
                                if dict.has_key(line):
                                     dict[line]=dict[line]+1
                                else:
                                        dict[line]=1
                        fin.close()

fout = open(sys.argv[1]+"onlyonce.txt","w")
fout.write(str(len(dict))+"\n")
for i in dict:
	if dict[i] == 1:
        	fout.write(i)
fout.close()

dict = {}
for root, dirs, files in os.walk(sys.argv[1]):
        for name in files:
                filename = root + '/' + name
                if filename[len(filename)-1] == 'f' and filename[len(filename)-2] == 'd':
                        fin = open(filename,"r")
                        print filename
                        for line in fin.readlines():
                                ssplit = line.split()
                                if dict.has_key(ssplit[0]):
                                     dict[ssplit[0]]=dict[ssplit[0]]+int(ssplit[1])
                                else:
                                        dict[ssplit[0]]=int(ssplit[1])
                        fin.close()
dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
fout = open(sys.argv[1]+"topdf.txt","w")
for i in range(0,len(dict)):
        fout.write(dict[i][0] + " " + str(dict[i][1])+"\n")
fout.close()

