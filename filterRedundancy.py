import sys
import itertools
import networkx as nx
import pandas as pd
import scipy.spatial.distance
import scipy.stats
from operator import itemgetter

if len(sys.argv) != 6:
	print("Usage: python filterRedundancy.py network biadjacency_matrix mindist outputnetwork_gml output_communities\n");
	sys.exit()

def consineSimilarity(Ni,Nj):
	comm1 = Ni.split(',')
	comm2 = Nj.split(',')
	col1 = df[comm1[0]]
	col2 = df[comm2[0]]
	for res in comm1[1:]:
		col1+=df[res]
	for res in comm2[1:]:
		col2+=df[res]
	col1 /= len(comm1)
	col2 /= len(comm2)

	return scipy.spatial.distance.cosine(col1,col2)

def merge_nodes(G,nodes, new_node, attr_dict=None, **attr):
	G.add_node(new_node, attr_dict, **attr) # Add the 'merged' node

	for n1,n2,data in G.edges(data=True):
		if n1 in nodes:
			G.add_edge(new_node,n2,data)
		elif n2 in nodes:
			G.add_edge(n1,new_node,data)

	for n in nodes: # remove the merged nodes
		G.remove_node(n)

def getAAScore(aa):
	if aa == "A":
		return 1
	elif aa == "R":
		return 1
	elif aa == "N":
		return 1
	elif aa == "D":
		return 1
	elif aa == "C":
		return 1
	elif aa == "Q":
		return 1
	elif aa == "E":
		return 1
	elif aa == "G":
		return 1
	elif aa == "H":
		return 1
	elif aa == "I":
		return 1
	elif aa == "L":
		return 1
	elif aa == "K":
		return 1
	elif aa == "M":
		return 1
	elif aa == "F":
		return 1
	elif aa == "P":
		return 1
	elif aa == "S":
		return 1
	elif aa == "T":
		return 1
	elif aa == "W":
		return 1
	elif aa == "Y":
		return 1
	elif aa == "V":
		return 1
	elif aa == 'Á':
		return 2
	elif aa == 'Â':
		return 5
	elif aa == '&':
		return 3
	elif aa == 'Ĥ':
		return 3
	elif aa == 'Ŝ':
		return 2
	elif aa == 'Ñ':
		return 9
	elif aa == 'Ṕ':
		return 6
	elif aa == '!':
		return 6
	elif aa == '@':
		return 9
	elif aa == '#':
		return 6
	elif aa == '+':
		return 2
	elif aa == '_':
		return 2
	elif aa == 'Ũ':
		return 3
	elif aa == 'Õ':
		return 5
	elif aa == 'Ĩ':
		return 4
	elif aa == 'Ẽ':
		return 5
	elif aa == '$':
		return 2
	elif aa == '%':
		return 2
	elif aa == 'Ã':
		return 3
	else:
		return 39#put gap

def filterGraph(Gnx):
	components = list(nx.connected_components(Gnx))

	for component in components:
		component = list(component)
		positions = {}
		for res in component:
			aa = res[0]
			pos = res[1:]
			if len(Gnx.neighbors(res)) == 0:
				Gnx.remove_node(res)
			elif pos in positions:
				positions[pos].append(aa)
			else:	
				positions[pos] = [aa]

		for pos,aalist in positions.items():
			listres = []
			if len(aalist) > 1:
				lowerScore = 9999
				bestScores = []
				for symbol in aalist:#Symbols in same pos
					currentRes = symbol + pos
					if getAAScore(symbol) < lowerScore:
						lowerScore = getAAScore(symbol)

						for symbol2 in bestScores:
							res2 = symbol2 + pos
							Gnx.remove_node(res2)

						bestScores = [symbol]
					else:
						Gnx.remove_node(currentRes)
	return Gnx

def filterGraphNeighboor(Gnx,components):
	# commresidues = []
	# for component in components:
	# 	commresidues += component

	# for node in Gnx.nodes():
	# 	if node not in commresidues:
	# 		Gnx.remove_node(node)

	for component in components:
		component = list(component)
		positions = {}
		for res in component:
			aa = res[0]
			pos = res[1:]
			if len(Gnx.neighbors(res)) == 0:
				Gnx.remove_node(res)
			elif pos in positions:
				positions[pos].append(aa)
			else:	
				positions[pos] = [aa]

		for pos,aalist in positions.items():
			listres = []
			if len(aalist) > 1:
				for symbol in aalist:#Symbols in same pos
					currentRes = symbol + pos
					avgPearson = 0.0
					N = 0
					for res in Gnx.neighbors(currentRes):
					#for res in component:
						aa = res[0]
						pos2 = res[1:]
						if pos != pos2: #Compare with residues of diferent positions
							cc,pvalue = scipy.stats.pearsonr(df[res],df[currentRes])
							avgPearson += cc
							N += 1
					if N > 0:
						avgPearson = avgPearson/float(N)
						listres.append((symbol,avgPearson))
				listres.sort(key=lambda tup: tup[1], reverse=True)
	
				if len(listres) > 0:
					maxPearson = max(listres,key=itemgetter(1))[1]

					listres2 = []
					for aa,cc in listres:
						res = aa + pos
						if cc < (maxPearson-0.05):
							if res in Gnx.nodes():
								Gnx.remove_node(res)
						elif cc == maxPearson:
							listres2.append((aa,getAAScore(aa)))

					if len(listres2) > 0:
						minAAscore = min(listres2,key=itemgetter(1))[1]

						for aa,score in listres2:
							res = aa + pos
							if score > minAAscore:
								if res in Gnx.nodes():
									Gnx.remove_node(res)

	return Gnx

def communityDetection(Gnx,cutoff):
	communities = []
	count = 0
	while True:
		count += 1
		mindist = 99999999
		#maxdist = 0
		mergecomm1 = ""
		mergecomm2 = ""
		for Ni in Gnx.nodes():
			for Nj in Gnx.neighbors(Ni):
				#dist = euclidianDistance(Ni,Nj)
				dist = consineSimilarity(Ni,Nj)
				if dist < mindist:
				#if dist > maxdist:
					mindist = dist
					#maxdist = dist
					mergecomm1 = Ni
					mergecomm2 = Nj
		if mergecomm1 == "" or mergecomm2 == "":
			break
		if mindist > cutoff:
			break
		new_node = mergecomm1 + "," + mergecomm2
		merge_nodes(Gnx,[mergecomm1,mergecomm2],new_node)

	fw = open(outputcomm,'w')
	for comms in Gnx.nodes():
		nodelist = comms.split(',')
		if len(nodelist) > 1:
			comm = []
			for node in nodelist:
				fw.write(node + " ")
				comm.append(node)
			communities.append(comm)
			fw.write("\n")
	fw.close()

	dicComm = {}

	for i,comm in enumerate(communities):
		for res in comm:
			dicComm[res] = i+1

	return dicComm


networkfile = sys.argv[1]
biadjacencyfile = sys.argv[2]
mindist = float(sys.argv[3])
outputfile = sys.argv[4]
outputcomm = sys.argv[5]
G = nx.Graph()

df = pd.read_csv(biadjacencyfile,0,' ')

fr = open(networkfile,'r')

for line in fr:
	line = line.strip()
	temp = line.split()
	Ni = temp[0]
	Nj = temp[1]
	w = float(temp[2])
	G.add_edge(Ni,Nj,weight=w)

fr.close()

components = list(nx.connected_components(G))
G = filterGraphNeighboor(G,components) #Testar filtrar por vizinhança
G = filterGraph(G)
detected_comms = communityDetection(G.copy(),mindist)

for node in G.nodes():
	if node not in detected_comms:
		detected_comms[node] = 0

nx.set_node_attributes(G, 'community', detected_comms)

nx.write_gml(G, outputfile)
