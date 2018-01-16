import sys

if len(sys.argv) != 5:
	print("Usage: python nodeInt2NodeStr.py intnetwork map outputnetwork w? (1-yes, 2-no)\n");
	sys.exit()

networkfile = sys.argv[1]
mapfile = sys.argv[2]
outputfile = sys.argv[3]
hasw = int(sys.argv[4])

dic = {}

fr = open(mapfile,'r')

for line in fr:
	line = line.strip()
	temp = line.split()
	Nstr = temp[0]
	Nint = temp[1]
	dic[Nint] = Nstr

fr.close()

fr = open(networkfile,'r')
fw = open(outputfile,'w')

for line in fr:
	line = line.strip()
	temp = line.split()
	Ii = temp[0]
	Ij = temp[1]
	if hasw == 1:
		w = temp[2]
		fw.write(dic[Ii] + " " + dic[Ij] + " " + w + "\n")
	else:
		fw.write(dic[Ii] + " " + dic[Ij] + "\n")

fw.close()
fr.close()