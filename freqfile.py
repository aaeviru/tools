import os
import sys
import os.path
fout = open("/mnt/nas2a/ko/NTCIR.txt","w")
stopword = open(sys.argv[1]+"stopword2.txt")
sp = []
for line in stopword.readlines():
        sp.append(line.split()[0])
stopword.close()
num = 0
for name in os.listdir(sys.argv[1]):
	filename = sys.argv[1] + name
	if (filename[len(filename)-1] == 'e'):
		print filename
		fin = open(filename,"r")
		for line in fin.readlines():
			if line[0] == '@':
				num = num + 1
                		fout.write(line)
	        	elif line.split()[1] not in sp:
		                fout.write(line)
		fin.close()
fout.close()
print num
