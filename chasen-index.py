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
			dict = {}
			num += 1
			os.system("chasen -iw -o %s %s" % (filename+".chasen",filename) )
			fin = open(filename+".chasen","r")
			fout = open(filename+".fq","w")
			for line in fin:
				ssplit = line.split()
				t = len( ssplit )
				if t < 2 or (t == 4 and ( (re.match(r'記号',ssplit[3]) and  not re.search(r'アルファベット',ssplit[3])) or re.search(r'数',ssplit[3])  ) ):
					#raw_input()
					continue
				elif dict.has_key(ssplit[0]):
					#raw_input()
					dict[ssplit[0]]=dict[ssplit[0]]+1
				else:
					dict[ssplit[0]]=1
			fin.close()
			fin = open(filename,"r")
			lines = fin.readlines()
			fout.write("@"+filename[len(filename)-12:len(filename)-4]+" "+lines[4][25:len(lines[4])-2]+"\n")

			for i in dict:
				fout.write(str(dict[i])+" "+i+"\n")
			fout.close()
			os.system("rm %s" % (filename+".chasen") )
print num
