import sys
import itertools
#from statsmodels.stats.proportion import binom_test
from scipy import stats, optimize
import math

if len(sys.argv) != 3:
	print("Usage: python logw.py projectedNet outputnetwork\n");
	sys.exit()

projectionfile = sys.argv[1]
outputfile = sys.argv[2]

rf = open(projectionfile,'r')
wf = open(outputfile,'w')

for line in rf:
	temp = line.split()
	ni = temp[0]
	nj = temp[1]
	w = float(temp[2])
	wf.write(ni + " " + nj + " " + str(-math.log10(w)) + "\n")

rf.close()
wf.close()