import sys

name = sys.argv[1]
l = int(sys.argv[2])

r = [0 for i in range(l)]
n = []

for i in range(10):
    if i == 0:
        f = name+".log"
    else:
        f = name+'-v'+str(i)+'.log'
    fin = open(f,'r')
    tmp = fin.readlines()
    fin.close()
    if tmp == None:
        continue
    if len(tmp[-2]) < 2:
        lines = tmp[-2+(l*-1):-2]
    else:   
        lines = tmp[(l*-1):]
    for j in range(l):
        if i == 9:
            n.append(lines[j].split(':')[0])    
        r[j] = r[j] + float(lines[j].split(':')[1])
for i in range(l):
    s = r[i] / 10
    print n[i],s
