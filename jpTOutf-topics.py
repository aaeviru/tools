# -*- coding: utf-8 -*-

import os
import os.path
import sys

if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print '''
	2017/02/16
	python jpTOutf.py [質問フォルダ]
	*特許文章をutfに変換し*に保存する
    '''
    sys.exit(1)

for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
		filename = root + '/' + name
		print filename
		os.system("nkf -w --overwrite %s" % filename)
