import urllib2
import sys
import requests

if len(sys.argv) != 5:
	print("Generate bipartite network and mapProjections\nUsage: python genBipartite.py msa outnetwork outputmapX outputmapY\n");
	sys.exit()

inputfile = sys.argv[1]
outputnet = sys.argv[2]
outputmapX = sys.argv[3]
outputmapY = sys.argv[4]

f1 = open(inputfile,'r')

fwbn = open(outputnet,'w')
fwbmX = open(outputmapX,'w')
fwbmY = open(outputmapY,'w')
sequences = []
#Making Bipartide Network
for line in f1:
	temp = line.split()
	seqname = temp[0]
	#w = temp[2]
	seq = temp[1].strip()
	#fwbmX.write(seqname + " " + str(w))
	fwbmX.write(seqname)
	sequences.append((seqname,seq))
	print "Creating Bipartite Network... " + seqname
	for i, aa in enumerate(seq):
		if aa != '-' and aa != '.':
			residue = aa + str(i+1)
			fwbn.write(seqname + " " + residue + "\n")
			fwbmX.write(" " + residue)
	fwbmX.write("\n")

nCols = len(sequences[0][1])
nLines = len(sequences)
colsVec = []
for i in xrange(nCols):
	pos = i + 1
	aas = set()
	for j in xrange(nLines):
		if sequences[j][1][i] != '-' and sequences[j][1][i] != '.':
			aas.add(sequences[j][1][i])

	for aa in aas:
		residue = aa + str(i+1)
		fwbmY.write(residue)
		for j in xrange(nLines):
			if sequences[j][1][i] == aa:
				fwbmY.write(" " + sequences[j][0])
		fwbmY.write("\n")
	colsVec.append(len(aas))

#Count no gaps
count = 0
for v in colsVec:
	if v > 0:
		count +=1

fwbmY.write(str(count))

f1.close()