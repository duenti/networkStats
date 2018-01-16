import sys
import requests
import glob
import os
from joblib import Parallel, delayed
import multiprocessing
import numpy as np

if len(sys.argv) != 5:
	print("Usage: python trimGroups_scale.py mapXdir maxFreq minFreq outputMapXdir\n");
	sys.exit()

def aa2num(aa):
	if aa == "A":
		return 0
	elif aa == "R":
		return 1
	elif aa == "N":
		return 2
	elif aa == "D":
		return 3
	elif aa == "C":
		return 4
	elif aa == "Q":
		return 5
	elif aa == "E":
		return 6
	elif aa == "G":
		return 7
	elif aa == "H":
		return 8
	elif aa == "I":
		return 9
	elif aa == "L":
		return 10
	elif aa == "K":
		return 11
	elif aa == "M":
		return 12
	elif aa == "F":
		return 13
	elif aa == "P":
		return 14
	elif aa == "S":
		return 15
	elif aa == "T":
		return 16
	elif aa == "W":
		return 17
	elif aa == "Y":
		return 18
	elif aa == "V":
		return 19
	elif aa == 'Á':
		return 20
	elif aa == 'Â':
		return 21
	elif aa == '&':
		return 22
	elif aa == 'Ĥ':
		return 23
	elif aa == 'Ŝ':
		return 24
	elif aa == 'Ñ':
		return 25
	elif aa == 'Ṕ':
		return 26
	elif aa == '!':
		return 27
	elif aa == '@':
		return 28
	elif aa == '#':
		return 29
	elif aa == '+':
		return 30
	elif aa == '_':
		return 31
	elif aa == 'Ũ':
		return 32
	elif aa == 'Õ':
		return 33
	elif aa == 'Ĩ':
		return 34
	elif aa == 'Ẽ':
		return 35
	elif aa == '$':
		return 36
	elif aa == '%':
		return 37
	elif aa == 'Ã':
		return 38
	else:
		return 39#put gap

inputdir = sys.argv[1]
maxFreq = float(sys.argv[2])
minFreq = float(sys.argv[3])
outputdir = sys.argv[4]

def filter(file):
	print(file)
	f1 = open(file,'r')

	sequences = []
	frequencies = []
	Ncols = 0

	for line in f1:
		line = line.strip()
		temp = line.split()
		seqname = temp[0]
		reslist = temp[1:]
		lastpos = int(reslist[len(reslist)-1][1:])
		if lastpos > Ncols:
			Ncols = lastpos
		sequences.append((seqname,reslist))

	N = len(sequences)

	for currentPos in range(1,Ncols+1):
		freqTuple = list(np.zeros(39))
		for seqname,reslist in sequences:
			for residue in reslist:
				aa = residue[0]
				pos = int(residue[1:])
				if pos == currentPos:
					aaid = aa2num(aa)
					freqTuple[aaid] += 1.0
				elif pos > currentPos:
					break
		freqTuple[:] = [x / N for x in freqTuple]
		#print("Col " + str(currentPos) + "\t" + str(freqTuple))
		frequencies.append(freqTuple)

	temp = file.split('/')
	output = outputdir + temp[len(temp)-1]
	#print(output)
	fw = open(output,'w')

	for i in range(0,N):
		name = sequences[i][0]
		reslist = sequences[i][1]
		fw.write(name)
		for res in reslist:
			aa = res[0]
			j = int(res[1:])-1
			num = aa2num(aa)
			if frequencies[j][num] < maxFreq and frequencies[j][num] > minFreq:
				fw.write(" " + res)
		fw.write("\n")
	fw.close()

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(filter)(file) for file in glob.glob(inputdir + "*.txt"))