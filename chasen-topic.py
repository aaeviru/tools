import os
import os.path
import re
root = "/home/meip-users/Downloads/ntc6pat/jp/topics/"
for name in os.listdir(root):
	filename = root + '/' + name
	if (filename[len(filename)-3] == 't'):
		os.system("chasen -o %s %s" % (filename+".chasen",filename) )
