import sys
fs = open(sys.argv[1],'r')
fc = open(sys.argv[2],'r')

s = set()
for line in fs:
    line = line.strip('\n')
    s.add(line)
for line in fc:
    line = line.split()[0]
    if line not in s:
        print line
