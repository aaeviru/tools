#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sw = set() 
felse = open("/home/ec2-user/git/statresult/else_words.txt","r")
f1 = open("/home/ec2-user/git/statresult/1.txt","r")
fol = open("/home/ec2-user/git/statresult/onlyonce.txt","r")
fsw = open("/home/ec2-user/git/statresult/stopword2.txt","r")
fen = open("/home/ec2-user/git/statresult/gen2.txt","r")
fu = open("/home/ec2-user/git/statresult/usersw.txt","r")
fout = open("/home/ec2-user/git/statresult/stopword5.txt","w")

for line in felse:
    term = line.strip('\n')
    if term not in sw:
        sw.add(term)
felse.close()
for line in f1:
    term = line.strip('\n')
    if term not in sw:
        sw.add(term)
f1.close()
for line in fol:
    term = line.strip('\n')
    if term not in sw:
        sw.add(term)
fol.close()

for line in fsw:
    term = line.split()[0]
    if term not in sw:
        sw.add(term)
fsw.close()
for line in fen:
    term = line.strip('\n')
    if term not in sw:
        sw.add(term)
fen.close()
for line in fu:
    term = line.strip('\n')
    if term not in sw:
        sw.add(term)
fu.close()

for term in sw:
    fout.write(term + "\n")
fout.close()
