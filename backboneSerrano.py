import sys
import itertools
from scipy.integrate import quad

def integrand(x, Di):
     return (1-x)**(Di-2)

if len(sys.argv) != 6:
	print("Usage: python backboneSerrano.py projectedNet degreefile w_degreefile alpha outputnetwork\n");
	sys.exit()

projectionfile = sys.argv[1]
degreefile = sys.argv[2]
w_degreefile = sys.argv[3]
alpha = float(sys.argv[4])
outputfile = sys.argv[5]

degrees = {}
w_degrees = {}

rf = open(degreefile,'r')

for line in rf:
	temp = line.split()
	node = temp[0]
	degree = int(temp[1])
	degrees[node] = degree
	#print("Reading Degree " + node)
	
rf.close()

rf = open(w_degreefile,'r')

for line in rf:
	temp = line.split()
	node = temp[0]
	degree = int(temp[1])
	w_degrees[node] = degree
	#print("Reading Weighted Degree " + node)

rf.close()

rf = open(projectionfile,'r')
wf = open(outputfile,'w')

for line in rf:
	temp = line.split()
	ni = temp[0]
	nj = temp[1]
	w = int(temp[2])
	##Node i -> Node j
	wd = w_degrees[ni]
	pij = float(w)/float(wd)
	Di = degrees[ni]
	intrg = quad(integrand,0,pij,args=(Di))
	Pr = 1 - (Di-1) * intrg[0]
	#print(ni + " " + nj + " " + str(Pr))
	if Pr <= alpha:
		wf.write(ni + " " + nj + " " + str(Pr) + "\n")
	##Node j -> Node i
	wd = w_degrees[nj]
	pji = float(w)/float(wd)
	Dj = degrees[nj]
	intrg = quad(integrand,0,pji,args=(Dj))
	Pr = 1 - (Dj-1) * intrg[0]
	#print(nj + " " + ni + " " + str(Pr))
	if Pr <= alpha:
		wf.write(nj + " " + ni + " " + str(Pr) + "\n")

rf.close()
wf.close()