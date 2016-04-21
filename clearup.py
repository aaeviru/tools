import os
import os.path
import sys
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
		filename = root + '/' + name
		if (filename[len(filename)-3] == 'T') or (filename[len(filename)-3] == 's'):
			os.system("rm -f %s" % filename )
