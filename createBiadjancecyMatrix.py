import sys
import pandas as pd

if len(sys.argv) != 3:
	print("Usage: python createAdjacencyMatrix.py bipartide outputmatrix\n");
	sys.exit()

bipartidefile = sys.argv[1]
outputfile = sys.argv[2]

rf = open(bipartidefile,'r')
proteins = set()
residues = set()
dic = {}

for line in rf:
	temp = line.split()
	n1 = temp[0]
	n2 = temp[1]
	proteins.add(n1)
	residues.add(n2)
	if n2 in dic:
		dic[n2].append(n1)
	else:
		dic[n2] = [n1]

rf.close()

proteins = list(proteins)
residues = list(residues)

wf = open(outputfile,'w')
wf.write("proteins")
for r in residues:
	wf.write(" " + r)

for p in proteins:
	wf.write("\n" + p)
	for r in residues:
		if p in dic[r]:
			wf.write(" 1")
		else:
			wf.write(" 0")

wf.close()

# rf = open(projectionfile,'r')
# wf = open(outputfile,'w')

# for line in rf:
# 	temp = line.split()
# 	ni = temp[0]
# 	nj = temp[1]
# 	df = pd.DataFrame(
# 		{'ANi' : mapY[ni],
# 		'ANj' : mapY[nj]})
# 	pd.crosstab(df.ANi,df.ANj)

# rf.close()
# wf.close()