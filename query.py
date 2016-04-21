#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import re
import gssxml
stoplist = ["請求","こと","項"]

rel = []
def printls(ls):
	for i in ls:
		print i

for i in [4,5,6]:
	fin = open("/home/meip-users/Downloads/ntc6pat/jp/rels/def1/rel.ntc"+str(i)+".a","r")
	rel.append(fin.read())
	fin.close()

for root, dirs, files in os.walk("/home/meip-users/Downloads/ntc6pat/jp/topics/"):
	for name in files:
		filename = root + '/' + name
		if (filename[len(filename)-3] == 's'):

			topic = int(name[0:4])

			raw_input("topic:"+name[0:4]+ open(filename[0:len(filename)-7]).read())

			if topic < 1045:
				ref = rel[0]
			elif topic < 3350:
				ref = rel[1]
			else:
				ref = rel[2]
			relr = re.findall(r"(?<=" + name[0:4] +"\s\w\s.{16})\d{2}-\d{6}" ,ref)
			fin = open(filename,"r")
			#fout = open(filename+".txt","w")
			query = ""
			for line in fin:
				if len(line.split()) < 3 or re.match(r'名詞',line.split()[3]):
					keyword = line.split()[0]
					if (keyword in stoplist) or (keyword in query):
						continue
					query += keyword + " "
			#fout.write(temp)
			fin.close()

			raw_input(query)
			raw_input("search result:")
			sr = gssxml.search(query,20)
			printls(sr[1])
			hit = 0
			raw_input("relevant document:")
			for doc in relr:
				doc = re.sub(r'-','',doc)
				if doc in sr[0]:
					hit+=1
				print doc

			raw_input("hit:"+str(hit))
			#fout.close()
			#raw_input("Press Enter to continue...")
