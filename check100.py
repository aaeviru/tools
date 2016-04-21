import sys
import os
N = 1000
K = 61
num = 0
average = 0.0
length = 0
for root, dirs, files in os.walk(sys.argv[1]):
                for name in files:
			num = num + 1
                        filename = root + '/' + name
			fin = open(filename,"r")
			listall = []
			for line in fin:
				if line[4] != ':':
					continue
				doc = line[5:13]
				if doc not in listall:
					listall.append(doc)
			length = length + len(listall)
print num
print length
print length *1.0/num
