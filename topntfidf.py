# -* coding: utf-8 -*-

#cal the sum of top n tfidf words of each session

import os
import os.path
import sys
import re


if len(sys.argv) != 3:
    print 'input:floder,n'
    sys.exit(1)
n = int(sys.argv[2])

dict = {}


words = set()
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
               	filename = root + '/' + name
               	if filename[len(filename)-1] == '2' and filename[len(filename)-2] == 'n':
			fin = open(filename,"r")
                        lines = fin.readlines()
                        limit = len(lines)
                        if limit > n:
                            limit = n
			for i in range(0,limit):
                            words.add(lines[i])
                        fin.close()

print len(words)

