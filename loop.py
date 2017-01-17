import subprocess
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from pythonlib import sysf


inputform = "command,loops,output-floder"
if len(sys.argv) != 4:
    print "input:" + inputform
    sys.exit(1)

outf = sys.argv[3]+'/loop-'+'-'.join(map(lambda x:x.strip('/').split('/')[-1],sys.argv[1:-1]))
fout = sysf.logger(outf,inputform)

comm = sys.argv[1].split()
for i in range(len(comm)):
    if comm[i][0] == '~':
        comm[i] = path.expanduser(comm[i])
    elif comm[i][0] == '.':
        comm[i] = path.abspath(comm[i])
loops = int(sys.argv[2])

for i in range(loops):
    if subprocess.call(comm) != 0:
        sys.exit(1)
