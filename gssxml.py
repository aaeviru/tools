#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import requests
import re
def search_name(keyword,narticles=10):
	xml_request = """<?xml version="1.0" encoding="UTF-8"?>
			<gss version="3.0">
			<assoc target="sample" niwords="70" cutoff-df="0" stage1-sim="WT_SMARTAW" narticles="10" nkeywords="10" yykn="10" nacls="1" nkcls="1" a-offset="0" a-props="title" cross-ref="aw" stage2-sim="WT_SMARTWA">
			<freetext cutoff-df="0" stemmer="auto">"""+keyword+"""</freetext>
			</assoc>
			</gss>"""  
	headers = {'Content-Type': 'application/xml'}
	url = 'http://localhost/getassoc/gss3'
	response = requests.post(url, data=xml_request, headers=headers).text
	namelist = []
	for name in re.findall(r"(?<=<article name=\")[0-9]*",response):
		namelist.append(name)
	return namelist

def search_title(keyword,narticles=10):
	xml_request = """<?xml version="1.0" encoding="UTF-8"?>
			<gss version="3.0">
			<assoc target="sample" niwords="70" cutoff-df="0" stage1-sim="WT_SMARTAW" narticles=\"""" + str(narticles) + """\" nkeywords="10" yykn="10" nacls="1" nkcls="1" a-offset="0" a-props="title" cross-ref="aw" stage2-sim="WT_SMARTWA">
			<freetext cutoff-df="0" stemmer="auto">"""+keyword+"""</freetext>
			</assoc>
			</gss>"""  
	headers = {'Content-Type': 'application/xml'}
	url = 'http://localhost/getassoc/gss3'
	response = requests.post(url, data=xml_request, headers=headers).text
	titlelist = []
	for title in re.findall(r"(?<=title=\").*?(?=\")",response):
		titlelist.append(title)
	return titlelist

def search(keyword,narticles=10):
	xml_request = """<?xml version="1.0" encoding="UTF-8"?>
			<gss version="3.0">
			<assoc target="sample" niwords="70" cutoff-df="0" stage1-sim="WT_SMARTAW" narticles="10" nkeywords="10" yykn="10" nacls="1" nkcls="1" a-offset="0" a-props="title" cross-ref="aw" stage2-sim="WT_SMARTWA">
			<freetext cutoff-df="0" stemmer="auto">"""+keyword+"""</freetext>
			</assoc>
			</gss>"""  
	headers = {'Content-Type': 'application/xml'}
	url = 'http://localhost/getassoc/gss3'
	response = requests.post(url, data=xml_request, headers=headers).text
	namelist = []
	for name in re.findall(r"(?<=<article name=\")[0-9]*",response):
		namelist.append(name)
	titlelist = []
	for title in re.findall(r"(?<=title=\").*?(?=\")",response):
		titlelist.append(title)
	return (namelist,titlelist)
