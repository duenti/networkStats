import sys
import itertools

if len(sys.argv) != 4:
	print("Usage: python adjustBipartiteInput.py inputnetwork outputnetwork mapfile\n");
	sys.exit()

networkfile = sys.argv[1]
outputfile = sys.argv[2]
mapfile = sys.argv[3]

uset = {}
vset = {}
i = 0

fr = open(networkfile,'r')

for line in fr:
	line = line.strip()
	temp = line.split()
	n1 = temp[0]
	n2 = temp[1]
	if n1 not in uset:
		uset[n1] = -1
	if n2 not in vset:
		vset[n2] = -1

fr.close()

fr = open(networkfile,'r')
fw1 = open(outputfile,'w')

iU = 0
iV = len(uset)

for line in fr:
	line = line.strip()
	temp = line.split()
	n1 = temp[0]
	n2 = temp[1]
	intU = -1
	intV = -1
	if uset[n1] == -1:
		uset[n1] = iU
		iU += 1
	if vset[n2] == -1:
		vset[n2] = iV
		iV += 1
	intU = uset[n1]
	intV = vset[n2]
	fw1.write(str(intU) + " " + str(intV) + "\n")


fr.close()
fw1.close()

fw2 = open(mapfile,'w')

#fw2.write("#\n")
for k,v in vset.items():
	fw2.write(k + " " + str(v) + "\n")

fw2.close()