import sys

fen = open("/home/ec2-user/data/en_words.txt","r")
fout = open("/home/ec2-user/data/gen.txt","w")

for line in fen:
    check = 0;
    for ch in line:
        if ch not in "ATUGCatugc\n":
            check = 1
            break
    if check == 0:
        fout.write(line)
fen.close()
fout.close()
