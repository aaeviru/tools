#!/usr/bin/python
# -*- coding: utf-8 -*-
from xlrd import open_workbook
import re
import sys
#创建一个用于读取sheet的生成器,依次生成每行数据,row_count 用于指定读取多少行, col_count 指定用于读取多少列
def readsheet(s, row_count=-1, col_count=-1):
    # Sheet 有多少行
	nrows = s.nrows
    # Sheet 有多少列
    	ncols = s.ncols
    	row_count = (row_count if row_count > 0 else nrows)
    	col_count = (col_count if col_count > 0 else ncols)
    	row_index = 0
    	while row_index < row_count:
        	yield [s.cell(row_index, col).value for col in xrange(col_count)]
        	row_index += 1

wb = open_workbook(sys.argv[1]) #打开Excel文件
fout = open("/mnt/nas2a/ko/classinfo/"+sys.argv[1][len(sys.argv[1])-19]+".txt","w")
# 读取Excel中所有的Sheet
for s in wb.sheets():
    	for row in readsheet(s, -1, 4):# 只读取每个Sheet的前10行，前10列(当然你要确保,你的数据多余10行，且多余10列)
		if len(row) > 2 and len(row[1]) == 4 and row[1][0:1].isalpha():
        		fout.write(row[1].encode('utf-8')+" "+row[3].encode('utf-8')+"\n")
fout.close()
