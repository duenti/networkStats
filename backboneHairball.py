import sys
import itertools
#from statsmodels.stats.proportion import binom_test
from scipy import stats, optimize
import math

if len(sys.argv) != 5:
	print("Usage: python backboneHairball.py projectedNet w_degreefile alpha outputnetwork\n");
	sys.exit()

projectionfile = sys.argv[1]
w_degreefile = sys.argv[2]
alpha = float(sys.argv[3])
outputfile = sys.argv[4]

w_degrees = {}
T = 0

rf = open(w_degreefile,'r')

def binom_test(count, nobs, prop=0.5):
	pval = stats.binom.sf(count-1, nobs, prop)
	

for line in rf:
	temp = line.split()
	node = temp[0]
	degree = int(temp[1])
	w_degrees[node] = degree
	T += degree
	#print("Reading Weighted Degree " + node)

rf.close()

T = T/2

rf = open(projectionfile,'r')
wf = open(outputfile,'w')

for line in rf:
	temp = line.split()
	ni = temp[0]
	nj = temp[1]
	w = int(temp[2])
	ki = w_degrees[ni]
	kj = w_degrees[nj]
	p = ki * kj * 1.0 / T / T / 2.0
	Pr = stats.binom.sf(w-1, T, p)
	strPr = -1*math.log10(Pr)
	#print(strPr)
	if strPr > alpha:
		print(nj + " " + ni + " " + str(strPr))
		wf.write(nj + " " + ni + " " + str(strPr) + "\n")

rf.close()
wf.close()