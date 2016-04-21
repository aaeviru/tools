import re
import os
root = "/home/meip-users/Downloads/ntc6pat/jp/topics/"
for name in os.listdir(root):
	filename = root + '/' + name
	print name
	if (filename[len(filename)-3] == 's'):
		ww = ""
		fin = open(filename,"r")
		for line in fin:
			if len(line)>1:
				ww += line
		fin.close()
		fout = open(filename,"w")
		fout.write(ww)
		fout.close()
