##Testar o Pearson nas matriz da projeção
import sys
import pandas as pd
import itertools
import scipy.stats

if len(sys.argv) != 5:
	print("Usage: python backbonePearson.py projectionfile adjacency_matrix cutoff outputnetwork1\n");
	sys.exit()

projectionfile = sys.argv[1]
adjacencyfile = sys.argv[2]
cutoff = float(sys.argv[3])
outputfile1 = sys.argv[4]

df = pd.read_csv(adjacencyfile,0,' ')
headers = list(df.columns.values)[1:]
#N = str(len(list(itertools.permutations(headers, 2))))

fw = open(outputfile1,'w')

i = 0
for Ni,Nj in itertools.combinations(headers, 2):
	i += 1
	#print(str(Ni) + "/" + str(Nj))
	PosI = Ni[1:]
	PosJ = Nj[1:]
	if PosI != PosJ:
		Ni_list = df[Ni]
		Nj_list = df[Nj]
		cc,pvalue = scipy.stats.pearsonr(Ni_list,Nj_list)
		if abs(cc) >= cutoff:
			fw.write(Ni + " " + Nj + " " + str(cc) + " " + str(pvalue) + "\n")
			#print(Ni + " " + Nj + " " + str(cc) + " " + str(pvalue))
		#elif cc <= (cutoff*-1):###############Utilizar em casos reais
			#fw.write(Ni + " " + Nj + " " + str(cc) + " " + str(pvalue) + "\n")
			#print(Ni + " " + Nj + " " + str(cc) + " " + str(pvalue))

fw.close()