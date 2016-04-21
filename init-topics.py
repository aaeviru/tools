import os
import os.path
import re
for root, dirs, files in os.walk("/home/meip-users/Downloads/ntc6pat/jp/topics/"):
	for name in files:
		filename = root + '/' + name
		if (filename[len(filename)-3] == 't'):
			continue
		fin = open(filename,"r")
		fout = open(filename+".txt","w")
		temp = re.findall(r"(?<=<CLAIM>).*(?=</CLAIM>)",fin.read(),re.DOTALL)[0]
		temp = re.sub(r'<.*?>','',temp)
		fout.write(temp)
		fin.close()
		fout.close()
