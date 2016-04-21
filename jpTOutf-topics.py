import os
import os.path
for root, dirs, files in os.walk("/home/meip-users/Downloads/ntc6pat/jp/topics/"):
	for name in files:
		filename = root + '/' + name
		print filename
		os.system("nkf -w --overwrite %s" % filename)
