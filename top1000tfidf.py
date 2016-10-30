# -* coding: utf-8 -*-

#cal the sum of top 1000 tfidf words of each session

import os
import os.path
import sys
import re
dict = {}


words = set()
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
               	filename = root + '/' + name
               	if filename[len(filename)-1] == '2' and filename[len(filename)-2] == 'n':
			fin = open(filename,"r")
			for line in fin:
                            words.add(line)
                        fin.close()

print len(words)

