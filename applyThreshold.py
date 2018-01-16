import sys
import os

if len(sys.argv) != 5:
	print("Usage: python applyThreshold.py network threshold outputfile 0|1 (0 for lower cut and 1 for upper cut)\n");
	sys.exit()

inputfile = sys.argv[1]
threshold = float(sys.argv[2])
outputfile = sys.argv[3]
bincut = sys.argv[4]

fr = open(inputfile,'r')
fw = open(outputfile,'w')

if bincut == "0":
	for line in fr:
		line = line.strip()
		temp = line.split()
		v1 = temp[0]
		v2 = temp[1]
		w = float(temp[2])

		if w >= threshold:
			fw.write(v1 + " " + v2 + " " + str(w) + "\n")
else:
	for line in fr:
		line = line.strip()
		temp = line.split()
		v1 = temp[0]
		v2 = temp[1]
		w = float(temp[2])

		if w <= threshold:
			fw.write(v1 + " " + v2 + " " + str(w) + "\n")

fr.close()
fw.close()