import os
import os.path
import re
import sys
if len(sys.argv) != 2:
    print "input:topic-folder"
    sys.exit(1)

root = sys.argv[1]
for name in os.listdir(root):
    filename = root + '/' + name
    if (filename[len(filename)-3] == 't'):
	os.system("chasen -iw -o %s %s" % (filename+".chasen",filename) )
