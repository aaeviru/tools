import os
import os.path
import sys
num = 0
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
        	filename = root + '/' + name
               	if filename[len(filename)-3] == 'T':
			num +=1
                        filename = filename[0:len(filename)-3]
                        os.system("nkf -w -O %s %s" % (filename+"TXT", filename+"txt") )  
print num
