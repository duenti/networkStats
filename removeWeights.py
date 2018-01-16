import sys
import glob
import os

if len(sys.argv) != 3:
	print("Usage: python removeWeights.py networkdir outputdir\n");
	sys.exit()

networkdir = sys.argv[1]
outputdir = sys.argv[2]

for file in glob.glob(networkdir + "*.txt"):
	print(file)
	temp = file.split('/')
	output = temp[len(temp)-1]
	outputfile = outputdir + output

	fr = open(file,'r')
	fw = open(outputfile,'w')

	for line in fr:
		line = line.strip()
		temp = line.split()
		ni = temp[0]
		nj = temp[1]
		fw.write(ni + " " + nj + "\n")

	fw.close()
	fr.close()
	