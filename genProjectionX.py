import sys
import itertools
import glob

#Versao com consumo de memoria maior

if len(sys.argv) != 3:
	print("Generate network projection X from the projection map\nUsage: python genProjectionX.py mapX outputnetwork\n");
	sys.exit()

mapXdir = sys.argv[1]
outputdir = sys.argv[2]

mapx = open(mapXdir,'r')
edges = {}

for line in mapx:
	line = line.strip()
	tempvec = line.split(" ")
	if len(tempvec) > 3:
		seq = tempvec[0]
		#w = float(tempvec[1])
		resList = tempvec[2:]
		#print seq
		for a,b in itertools.combinations(resList,2):
			if (a,b) in edges: 
				edges[(a,b)] += 1
			else:
				edges[(a,b)] = 1
mapx.close()

fw = open(outputdir,'w')

for key, value in edges.items():
	#print key[0] + " " + key[1] + " " + str(value)
	fw.write(key[0] + " " + key[1] + " " + str(value) + "\n")