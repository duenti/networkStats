import sys
import glob
from joblib import Parallel, delayed
import multiprocessing

if len(sys.argv) != 4:
	print("Usage: python topEdges.py networkdir N_elements outputdir\n");
	sys.exit()

projdir = sys.argv[1]
N = int(sys.argv[2])
outputdir = sys.argv[3]

def execute(file):
	print(file)
	G = []

	fr = open(file,'r')

	for line in fr:
		line = line.strip()
		temp = line.split()
		Ni = temp[0]
		Nj = temp[1]
		w = float(temp[2])
		G.append((Ni,Nj,w))

	fr.close()

	G.sort(key=lambda tup: tup[2], reverse=True)

	temp = file.split('/')
	output = temp[len(temp)-1]
	writefile = outputdir + output

	fw = open(writefile,'w')

	for Ni,Nj,w in G[:N]:
		fw.write(Ni + " " + Nj + " " + str(w) + "\n")

	fw.close()

#num_cores = multiprocessing.cpu_count()
num_cores = 1
results = Parallel(n_jobs=num_cores)(delayed(execute)(file) for file in glob.glob(projdir + "*.txt"))