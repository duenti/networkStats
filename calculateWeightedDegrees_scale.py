import sys
import networkx as nx
import glob

if len(sys.argv) != 3:
	print("Calculate Weighted Degrees for each node\nUsage: python calculateWeightedDegrees.py networkdir outputdir\n");
	sys.exit()

inputdir = sys.argv[1]
outputdir = sys.argv[2]

for i,file in enumerate(glob.glob(inputdir + "*.txt")):
	print("Calculating network " + str(i))
	G = nx.Graph()
	f1 = open(file,'r')

	for line in f1:
		temp = line.split()
		n1 = temp[0]
		n2 = temp[1]
		w = int(temp[2])
		G.add_edge(n1, n2, weight=w)
	f1.close()

	temp = file.split('/')
	output = temp[len(temp)-1]
	outputfile = outputdir + output
	fw = open(outputfile,'w')
	#Calculate Degrees
	d= G.degree(weight='weight')
	for node, degree in d.items():
		#print node + " " + str(degree)
		fw.write(node + " " + str(degree) + "\n")

	fw.close()