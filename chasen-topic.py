import os
import os.path
import re
root = "/home/ec2-user/data/topics"
for name in os.listdir(root):
	filename = root + '/' + name
	if (filename[len(filename)-3] == 't'):
		os.system("chasen -iw -o %s %s" % (filename+".chasen",filename) )
