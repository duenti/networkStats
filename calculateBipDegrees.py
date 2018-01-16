import sys
import networkx as nx
import glob

if len(sys.argv) != 3:
	print("Calculate Degrees for each node\nUsage: python calculateDegrees.py bipartitefile outputfile\n");
	sys.exit()

inputfile = sys.argv[1]
outputfile = sys.argv[2]

G = nx.Graph()
nodes = set()
f1 = open(inputfile,'r')

for line in f1:
	line = line.strip()
	temp = line.split()
	n1 = temp[0]
	n2 = temp[1]
	nodes.add(n2)
	G.add_edge(n1, n2)
f1.close()

fw = open(outputfile,'w')
#Calculate Degrees
d= G.degree(nodes)
for node, degree in d.items():
	#print node + " " + str(degree)
	fw.write(node + " " + str(degree) + "\n")
fw.close()