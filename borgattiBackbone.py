import sys
import pandas as pd
import math

if len(sys.argv) != 6:
	print("Usage: python borgattiBackbone.py projectionfile adjacency_matrix outputnetwork1 outputnetwork2 outputnetwork5\n");
	sys.exit()

projectionfile = sys.argv[1]
adjacencyfile = sys.argv[2]
outputfile1 = sys.argv[3]
outputfile2 = sys.argv[4]
outputfile5 = sys.argv[5]

df = pd.read_csv(adjacencyfile,0,' ')

rf = open(projectionfile,'r')
wf1 = open(outputfile1,'w')
wf2 = open(outputfile2,'w')
wf5 = open(outputfile5,'w')

count = 0
for line in rf:
	#count += 1
	#print(count)
	temp = line.split()
	ni = temp[0]
	nj = temp[1]
	ct = pd.crosstab(df[ni] > 0, df[nj] > 0)
	a = float(ct[1][1])
	b = float(ct[1][0])
	c = float(ct[0][1])
	d = float(ct[0][0])
	Pij5 = 0.0
	
	Pij1 = a/min(a+b,a+c)
	Pij2 = a/(a+b+c)
	if a*d == b*c:
		Pij5 = 0.5
	else:
		Pij5 = ((a*d)-math.sqrt(a*b*c*d))/(a*d - b*c)

	wf1.write(ni + " " + nj + " " + str(Pij1) + "\n")
	wf2.write(ni + " " + nj + " " + str(Pij2) + "\n")
	wf5.write(ni + " " + nj + " " + str(Pij5) + "\n")

rf.close()
wf1.close()
wf2.close()