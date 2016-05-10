import sys

fen = open("/home/ec2-user/data/gen.txt","r")
fdf = open("/home/ec2-user/data/totaldf.txt","r")

gen = []
for line in fen:
    gen.append(line.strip('\n'))
fen.close()

for line in fdf:
    term = line.split()[0]
    num = int(line.split()[1])
    if term in gen and num > 10:
        print term,num
fdf.close() 
