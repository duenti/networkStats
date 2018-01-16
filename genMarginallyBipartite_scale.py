import glob
import sys
import requests

if len(sys.argv) != 4:
	print("Generate bipartite network and mapProjections\nUsage: python genMarginallyBipartite_scale.py msadir outnetworkdir outputmapXdir\n");
	sys.exit()

inputdir = sys.argv[1]
outputnetdir = sys.argv[2]
outputmapXdir = sys.argv[3]

aa_properties = {}
aa_properties['A'] = "ÂÑŨ"
aa_properties['C'] = "ŜṔÕ"
aa_properties['D'] = "#_Õ$"
aa_properties['E'] = "_Ĩ%"
aa_properties['F'] = "Ñ!Ã"
aa_properties['G'] = "ÂÑŨ"
aa_properties['H'] = "&Ĩ"
aa_properties['I'] = "ÂÑ!Ẽ"
aa_properties['K'] = "&#+Ẽ"
aa_properties['L'] = "ÂÑ!Ẽ"
aa_properties['M'] = "ŜÑ!Ẽ"
aa_properties['N'] = "ÁṔ#Õ$"
aa_properties['P'] = "Ñ#Õ"
aa_properties['Q'] = "ÁṔ#Ĩ%"
aa_properties['R'] = "&#+Ẽ"
aa_properties['S'] = "ĤṔŨ"
aa_properties['T'] = "ĤṔÕ"
aa_properties['V'] = "ÂÑ!Ĩ"
aa_properties['W'] = "Ñ!Ã"
aa_properties['Y'] = "ĤṔÃ"



for i,file in enumerate(glob.glob(inputdir + "*.txt")):
	print("Creating Bipartide Network - " + str(i))
	f1 = open(file,'r')

	temp = file.split('/')
	output = temp[len(temp)-1]

	fwbn = open(outputnetdir + output,'w')
	fwbmX = open(outputmapXdir + output,'w')
	sequences = []
	#Making Bipartide Network
	for line in f1:
		temp = line.split()
		seqname = temp[0]
		#w = temp[1]
		seq = temp[1].strip()
		fwbmX.write(seqname)
		sequences.append((seqname,seq))
		#print "Creating Bipartite Network... " + seqname
		for i, aa in enumerate(seq):
			if aa != '-' and aa != '.':
				residue = aa + str(i+1)
				fwbn.write(seqname + " " + residue + "\n")
				fwbmX.write(" " + residue)
				for c in aa_properties[aa]:
					subres = c + str(i+1)
					fwbn.write(seqname + " " + subres + "\n")
					fwbmX.write(" " + subres)

		fwbmX.write("\n")

	f1.close()