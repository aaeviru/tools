# -*- coding: utf-8 -*-

import os
import os.path
import sys

if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print '''
	2017/02/16
	python jpTOutf.py [特許文章総フォルダ]
	*.TXTの特許文章をutfに変換し*.txtに保存する
	総文書数を出力する
    '''
    sys.exit(1)

num = 0
for i in range(1993,2003):
	tmp = str(i)+'A'
	print tmp	
	print num
	for root, dirs, files in os.walk(sys.argv[1]+tmp):
		for name in files:
			filename = root + '/' + name
			if filename[len(filename)-3] == 'T':
				num += 1
				filename = filename[0:len(filename)-3]
				os.system("nkf -w -O %s %s" % (filename+"TXT", filename+"txt") )	

for i in range(1993,2003):
	tmp = str(i)+'B'
	print tmp
	print num
	for root, dirs, files in os.walk(sys.argv[1]+tmp):
		for name in files:
			filename = root + '/' + name
			if filename[len(filename)-3] == 'T':
				num +=1
				filename = filename[0:len(filename)-3]
				os.system("nkf -w -O %s %s" % (filename+"TXT", filename+"txt") )  
print num
