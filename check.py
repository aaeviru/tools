# -*- coding: utf-8 -*-
import os
import os.path
import sys
import re
num = 0
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
               	filename = root + '/' + name
               	if filename[len(filename)-3] == 't':
			num += 1
			if os.path.isfile(filename+".chasen"):
				print "chasen:"+filename
			elif  os.path.isfile(filename+".fq")==False:
				print "fq:"+filename
		#	fin.close()
		#	os.system("rm %s" % (filename+".chasen") )
print num
