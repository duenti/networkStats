import sys
import pandas as pd

if len(sys.argv) != 4:
	print("Usage: python nodeStr2nodeInt.py network outputmatrix outputmap\n");
	sys.exit()

networkfile = sys.argv[1]
outputfile = sys.argv[2]
mapfile = sys.argv[3]

rf = open(networkfile,'r')
wf1 = open(outputfile,'w')
wf2 = open(mapfile,'w')
residues = {}
index = 1

for line in rf:
	temp = line.split()
	n1 = temp[0]
	n2 = temp[1]
	i1 = 0
	i2 = 0
	w = temp[2]
	if n1 in residues:
		i1 = residues[n1]
	else:
		residues[n1] = index
		i1 = index
		wf2.write(n1 + " " + str(index) + "\n")
		index += 1
	if n2 in residues:
		i2 = residues[n2]
	else:
		residues[n2] = index
		i2 = index
		wf2.write(n2 + " " + str(index) + "\n")
		index += 1
	wf1.write(str(i1) + " " + str(i2) + " " + w + "\n")
	
rf.close()
wf1.close()
wf2.close()