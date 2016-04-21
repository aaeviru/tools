import os
import os.path
import re
import sys
fout = open("/mnt/nas2a/ko/NTCIR.txt","w")
for name in os.listdir(sys.argv[1]):
	filename = sys.argv[1] + name
	if (filename[len(filename)-1] == 'e'):
		print filename
		fin = open(filename,"r")
		for line in fin.readlines():
			fout.write(line)
		fin.close()
fout.close()


