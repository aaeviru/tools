# -*- coding: utf-8 -*-

import os
import os.path
import re
import sys

if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print '''2017/02/20
	python chasen-topic.py [特許文章(topic,utf8)フォルダ]
	*.txtの特許文章を形態素解析の結果を*.chasenに保存する
    '''
    sys.exit(1)

if len(sys.argv) != 2:
    print "input:topic-folder"
    sys.exit(1)

root = sys.argv[1]
for name in os.listdir(root):
    filename = root + '/' + name
    if (filename[len(filename)-3] == 't'):
	os.system("chasen -iw -o %s %s" % (filename+".chasen",filename) )
