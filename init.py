import os
import os.path
import re
import sys
num = 0
fout = open("/mnt/nas2a/ko/"+sys.argv[1][len(sys.argv[1])-6:len(sys.argv[1])-1]+".freqfile","w")
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
		filename = root + '/' + name
		if (filename[len(filename)-2] == 'f'):
			num = num + 1
			fin = open(filename,"r")
			fout.write(fin.read())
			fin.close()
fout.close()
print num
