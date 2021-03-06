#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import re
import sys


if len(sys.argv) != 2:
    print "input:topic-folder"
    sys.exit(1)

sw = set() 
def printls(ls):
	for i in ls:
		print i
sw.add("EOS")
fin = open("/home/ec2-user/git/statresult/stopword4.txt","r")
for line in fin:
	sw.add(line.split()[0])
fin.close()
path = sys.argv[1]
for root, dirs, files in os.walk(path):
	for name in files:
		filename = root + '/' + name
		if (filename[len(filename)-3] == 's'):
			query = []

			fin = open(filename,"r")
			fout = open(path+name[0:4]+".txt","w")
			for line in fin:
                                if len(line.split()) == 3:
                                    print line
                                    continue
				if len(line.split()) < 3 or (re.match(r'名詞',line.split()[3]) and re.search(r'数',line.split()[3]) == None):
					keyword = line.split()[0]
					if (keyword in sw) or (keyword in query) or (keyword[0:1].isdigit()):
						continue
					fout.write(keyword+"\n")
					query.append(keyword)
			fin.close()
			fout.close()
