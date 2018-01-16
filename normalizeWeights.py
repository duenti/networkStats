import sys
import itertools

if len(sys.argv) != 3:
	print("Usage: python normalizeWeights.py inputnetwork outputnetwork\n");
	sys.exit()

networkfile = sys.argv[1]
outputfile = sys.argv[2]

G = []
minw = 999999999
maxw = 0

fr = open(networkfile,'r')

for line in fr:
	line = line.strip()
	temp = line.split()
	u = temp[0]
	v = temp[1]
	w = int(temp[2])
	if w > maxw:
		maxw = w
	if w < minw:
		minw = w
	G.append((u,v,w))

fr.close()

fw = open(outputfile,'w')

for u,v,w in G:
	wN = float(w-minw)/float(maxw-minw)
	fw.write(u + " " + v + " " + str(wN) + "\n")

fw.close()