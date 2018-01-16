#Filter nodes in order to run Tuminello backbone extractor
import sys
import requests
import glob
import os
from joblib import Parallel, delayed
import multiprocessing
import numpy as np

if len(sys.argv) != 3:
	print("Usage: python removeSamePosEdges.py networkdir outputdir\n");
	sys.exit()

inputdir = sys.argv[1]
outputdir = sys.argv[2]

def execute(file):
	print(file)
	temp = file.split('/')
	outfile = outputdir + temp[len(temp)-1]

	fw = open(outfile,'w')
	fr = open(file,'r')

	for line in fr:
		line = line.strip()
		temp = line.split()
		ni = temp[0]
		nj = temp[1]

		if ni[1:] != nj[1:]:
			fw.write(line + "\n")

	fr.close()
	fw.close()
	
num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(execute)(file) for file in glob.glob(inputdir + "*.txt"))