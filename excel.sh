#!/bin/sh
for d in a b c d e f g h; do
	qrsh -N ex$d -nostdin python excel.py /home/ko/Download/ipc_ver2016_${d}_section_excel.xls  
done

