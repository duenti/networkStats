import sys
import pandas as pd

if len(sys.argv) != 3:
	print("Usage: python w_matrix.py network outputmatrix\n");
	sys.exit()

networkfile = sys.argv[1]
outputfile = sys.argv[2]

rf = open(networkfile,'r')
residues = set()
dic = {}

for line in rf:
	temp = line.split()
	n1 = temp[0]
	n2 = temp[1]
	w = temp[2]
	residues.add(n1)
	residues.add(n2)
	if n1 <= n2:
		dic[(n1,n2)] = w
	else:
		dic[(n2,n1)] = w
rf.close()

residues = list(residues)

wf = open(outputfile,'w')
wf.write("residues")
for r in residues:
	wf.write(" " + r)

for r1 in residues:
	wf.write("\n" + r1)
	for r2 in residues:
		if r1 <= r2:
			if (r1,r2) in dic:
				wf.write(" " + dic[(r1,r2)])
			else:
				wf.write(" 0")
		else:
			if (r2,r1) in dic:
				wf.write(" " + dic[(r2,r1)])
			else:
				wf.write(" 0")

wf.close()