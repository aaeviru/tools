import sys
import os
N = 1000
K = 61
num = 0
average = {}
for K in range(101,1101,10):
	average[K] = 0
#print average
for root, dirs, files in os.walk(sys.argv[1]):
                for name in files:
			num = num + 1
                        filename = root + '/' + name
			fin = open(filename,"r")
			list = []
			listall = []
			check = 1
			listtmp = []
			for line in fin:
				if line[4] != ':':
					if check == 0:
						list.append(listtmp)
						listtmp = []
					check = 1
					continue
				check = 0
				doc = line[5:13]
				listtmp.append(doc)
				if doc not in listall:
					listall.append(doc)
			list.append(listtmp)
			for K in range(101,1101,10):
				dict = {}
				for doc in listall:
					for keyword in list:
						if doc in keyword:
							score = 1.0 / (K + keyword.index(doc) )
						else:
							score = 1.0 / (K + N*2)
						if doc in dict:
							dict[doc] = dict[doc]+score
						else:
							dict[doc] = score
				dict = sorted(dict.items(), key=lambda d: d[1], reverse = True)
				lenth = len(dict)
				if lenth > 1000:
					lenth = 1000
				dict = dict[0:lenth]
				#for i in dict:
				#	print i[0],i[1]
				total = hit = 0
				fin = open(sys.argv[2]+name,"r")
				for line in fin:
					if line[4] != ':':
						continue
					doc = line[5:13]
					total = total + 1
					for item in dict:
						if doc in item:
							hit = hit + 1
							break
			#print hit*1.0/total
			#print num
				average[K] = average[K] + hit*1.0/total
#				print K,average[K]
			#fout.close()

#				raw_input("next")
for K in range(101,1101,10):
	average[K] = average / num
	print K,average[K]		
print num
