import os
import os.path
import re
import sys
filename = sys.argv[1]
print filename
fin = open(filename,"r")
dict = {}
line = fin.readline()
while line:
	if line[0] == '@':
		line = fin.readline()
	#	print sorted(dict.items(), key=lambda d: d[1], reverse = True)
	#        raw_input("input")
		continue
	ssplit = line.split()
	if dict.has_key(ssplit[1]):
		dict[ssplit[1]]=dict[ssplit[1]]+1
	else:
		dict[ssplit[1]]=1
	line = fin.readline()

fin.close()
fout = open(filename+".df","w")
dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
for i in range(0,1000):
	fout.write(dict[i][0] + " " + str(dict[i][1])+"\n")
fout.close()
