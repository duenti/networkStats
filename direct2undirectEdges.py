import sys

if len(sys.argv) != 3:
	print("Usage: python direct2undirectEdges.py network outputnetwork\n");
	sys.exit()

networkfile = sys.argv[1]
outputfile = sys.argv[2]

G = {}

fr = open(networkfile,'r')

for line in fr:
	line = line.strip()
	temp = line.split()
	u = temp[0]
	v = temp[1]
	w = float(temp[2])
	if u < v:
		if (u,v) in G:
			if w < G[(u,v)]:
				G[(u,v)] = w
		else:
			G[(u,v)] = w
	else:
		if (v,u) in G:
			if w < G[(v,u)]:
				G[(v,u)] = w
		else:
			G[(v,u)] = w

fr.close()

fw = open(outputfile,'w')

for (u,v),w in G.items():
	fw.write(u + " " + v + " " + str(w) + "\n")

fw.close()