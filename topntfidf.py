# -* coding: utf-8 -*-

#cal the sum of top n tfidf words of each session

import os
import sys
import re

if len(sys.argv) != 3:
    print 'input:floder,n'
    sys.exit(1)
n = int(sys.argv[2])

words = set()

for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
               	filename = root + '/' + name
               	if filename[-1] == '2' and name[1] >= '0' and name[1] <= '9':
			fin = open(filename,"r")
                        lines = fin.readlines()
                        limit = len(lines)
                        if limit > n:
                            limit = n
			for i in range(0,limit):
                            words.add(lines[i])
                        fin.close()

for word in words:
    print word.strip('\n')
