import sys
import operator
import numpy as np
import glob

def getComposedAAList(idx):
	if idx == 'A':
		return ['A']
	elif idx == 'C':
		return ['C']
	elif idx == 'D':
		return ['D']
	elif idx == 'E':
		return ['E']
	elif idx == 'F':
		return ['F']
	elif idx == 'G':
		return ['G']
	elif idx == 'H':
		return ['H']
	elif idx == 'I':
		return ['I']
	elif idx == 'K':
		return ['K']
	elif idx == 'L':
		return ['L']
	elif idx == 'M':
		return ['M']
	elif idx == 'N':
		return ['N']
	elif idx == 'P':
		return ['P']
	elif idx == 'Q':
		return ['Q']
	elif idx == 'R':
		return ['R']
	elif idx == 'S':
		return ['S']
	elif idx == 'T':
		return ['T']
	elif idx == 'V':
		return ['V']
	elif idx == 'W':
		return ['W']
	elif idx == 'Y':
		return ['Y']
	elif idx == 'Á':
		return ["N","Q"]
	elif idx == 'Â':
		return ["G","A","V","L","I"]
	elif idx == '&':
		return ["H","K","R"]
	elif idx == 'Ĥ':
		return ["S","T","Y"]
	elif idx == 'Ŝ':
		return ["C","M"]
	elif idx == 'Ñ':
		return ["F","G","V","L","A","I","P","M","W"]
	elif idx == 'Ṕ':
		return ["Y","S","N","T","Q","C"]
	elif idx == '!':
		return ["L","I","F","W","V","M"]
	elif idx == '#':
		return ["R","K","N","Q","P","D"]
	elif idx == '+':
		return ["K","R"]
	elif idx == '_':
		return ["D","E"]
	elif idx == 'Ũ':
		return ["G","A","S"]
	elif idx == 'Õ':
		return ["C","D","P","N","T"]
	elif idx == 'Ĩ':
		return ["E","V","Q","H"]
	elif idx == 'Ẽ':
		return ["M","I","L","K","R"]
	elif idx == '$':
		return ["F","Y","W"]
	elif idx == '%':
		return ["N","D"]
	elif idx == 'Ã':
		return ["Q","E"]
	else:
		print("ERROR")
		return []

if len(sys.argv) != 4:
	print("Get average NResidues for group of sequences\nUsage: python avgNResidues_scale.py seqlistdir comms alignment\n");
	sys.exit()

seqdir = sys.argv[1]
commfile = sys.argv[2]
msa = sys.argv[3]

fr = open(commfile,'r')

communities = []
tempcomm = []
correctCount = 0
lencomm = 0
totalres = []

for line in fr:
	line = line.strip()
	temp = line.split()
	comm = []
	for node in temp:
		comm.append(node)

	if len(comm) > 1:
		communities.append(comm)
		totalres.append(len(comm))

fr.close()

fr = open(msa,'r')

sequences = {}

for line in fr:
	line = line.strip()
	temp = line.split()
	seqname = temp[0].split('/')[0]
	sequence = temp[1]
	sequences[seqname] = sequence

fr.close()

for seqfile in glob.glob(seqdir + "*.txt"):
	fr = open(seqfile,'r')

	sumRes = np.zeros(len(totalres))
	Nseqs = 0
	#print(totalres)
	for line in fr:
		Nseqs += 1
		rescount = np.zeros(len(totalres))
		refseq = line.strip()
		for i,comm in enumerate(communities):
			for res in comm:
				symbol = res[0]
				aalist = getComposedAAList(symbol)
				pos = int(res[1:])
				if(sequences[refseq][pos-1].upper() in aalist):
					rescount[i] += 1.0
		rescount /= totalres
		sumRes += rescount

	avgRes = sumRes/Nseqs

	print(seqfile.split('/')[1].split('.')[0] + " ",end='')
	for value in avgRes:
		print(str(value) + " ", end='')

	print("\n",end='')
	fr.close()

#Full conservation
sumRes = np.zeros(len(totalres))
Nseqs = 0
for name,seq in sequences.items():
	Nseqs += 1
	rescount = np.zeros(len(totalres))
	for i,comm in enumerate(communities):
		for res in comm:
			symbol = res[0]
			aalist = getComposedAAList(symbol)
			pos = int(res[1:])
			if(seq[pos-1].upper() in aalist):
				rescount[i] += 1.0
	rescount /= totalres
	sumRes += rescount

avgRes = sumRes/Nseqs
print("Full ",end='')
for value in avgRes:
	print(str(value) + " ", end='')