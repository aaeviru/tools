import os
import sys

fin = open(sys.argv[1]+"NTCIR.txt","r")
for line in fin:
	if line[0] == '@':
		if not line[1].isdigit():
			print line
fin.close()
