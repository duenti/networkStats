#Filter nodes in order to run Tuminello backbone extractor
import sys
import requests
import glob
import os
from joblib import Parallel, delayed
import multiprocessing
import numpy as np

if len(sys.argv) != 4:
	print("Usage: python trimBipartite.py bipartitedir filteredmapXdir outputBipartite\n");
	sys.exit()

inputdir = sys.argv[1]
mapdir = sys.argv[2]
outputdir = sys.argv[3]

def filter(file):
	print(file)
	temp = file.split('/')
	mapfile = mapdir + temp[len(temp)-1]

	nodeslist = set()
	f1 = open(mapfile,'r')

	for line in f1:
		line = line.strip()
		temp2 = line.split()
		seqname = temp2[0]
		reslist = temp2[1:]
		for res in reslist:
			nodeslist.add(res)

	f1.close()
	
	outfile = outputdir + temp[len(temp)-1]

	fw = open(outfile,'w')
	fr = open(file,'r')

	for line in fr:
		line = line.strip()
		temp = line.split()
		nj = temp[1]

		if nj in nodeslist:
			fw.write(line + "\n")

	fr.close()
	fw.close()
	
num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(filter)(file) for file in glob.glob(inputdir + "*.txt"))