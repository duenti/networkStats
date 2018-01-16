# networkStats

Set of python scripts used to model and analysis residue co-affiliation networks.

**adjustBipartiteInput**

  Usage: python adjustBipartiteInput.py input_network output_network output_mapfile
  
  Some external tools requires a format for bipartite networks with numeric nodes, which the counting for U set nodes range from 0 to size of U set, and the V set starts from size of U set to total number of nodes in the network. This program takes a bipartite network file in a edge list format and convert it for this specific numeric bipartite network format.
  
**applyThreshold**

  Usage: python applyThreshold.py input_network threshold_value output_network 0|1(0 for lower cut and 1 for upper cut)

  Applies a given threshold on a network

**avgNResidues_scale**

  Usage: python avgNResidues_scale.py sequences_list_directory community_file input_alignment

  Get an average number of residues for given subsets of sequences. The first parameter consists of a path to a directory containing text files with list of sequences that are going to be averaged. The second parameter consists in a community file containing the nodes from each community in each line separated by space (example below). The last parameter is an alignment file in a selex format.

  L2779 N517 W2850 V425 N3087 G421 <br>
  F930 S1125 <br>
  C1515 C3076 L646<br> 
  W729 G747 <br>
  T883 E2724 D827 V640 W3030<br> 
  N865 G1445 <br>
  T657 H3028 <br>
  G3055 F2869 <br>
  Y1454 W792 <br>

**backboneHairball**

  Usage: python backboneHairball.py input_projection input_weighted_degrees_file alpha output_network

  Statistically validation of edges through the Hairball approach. More information about the method in the paper. The method takes as parameter the projected network in a edge list format, a file containing the list of weighted degree for each node, an alpha cutoff parameter and the output network path.

**backbonePearson**

  Usage: python backbonePearson.py input_projection input_biadjacency_matrix cutoff output_network

  Statistically validation of edges through the Pearson approach. More information about the method in the paper. The method takes as parameter the projected network in a edge list format, the biadjacency matrix file, an alpha cutoff parameter and the output network path.

**backboneSerrano**

  Usage: python backboneSerrano.py input_projection input_degrees input_weighted_degrees alpha output_network

  Statistically validation of edges through the Serrano approach. More information about the method in the paper. The method takes as parameter the projected network in a edge list format, a file containing the list of degree for each node, a file containing the list of weighted degree for each node, an alpha cutoff parameter and the output network path.

**borgattiBackbone**

  Usage: python borgattiBackbone.py input_projection input_biadjacency_matrix output_network1 output_network2 output_network3

  This program calculates the statistically validation of edges through the following three approaches: Borgatti normalization, Jaccard coefficient and Bonacich equation. More information about the method in the paper. The method takes as parameter the projected network in a edge list format, a file containing the biadjacency matrix, and the three output files, one for each approach.

**calculateBipDegrees**

  Usage: python calculateBipDegrees.py inpute_network_file outputfile_file

  Calculates the degree distribution for every node on a given bipartite network.

**calculateDegrees_scale**

  Usage: python calculateDegrees.py input_network_path output_path

  Calculates the degree distribution for each node of every network on a given directory.

**calculateWeightedDegrees_scale**

  Usage: python calculateWeightedDegrees.py input_network_path output_path

  Calculates the weighted degree distribution for each node of every network on a given directory. 

**createBiadjancecyMatrix**

  Usage: python createAdjacencyMatrix.py input_bipartite_file output_matrix

  Generate the biadjacency matrix from a given bipartite network file.

**createBiadjancecyMatrix2**

  Usage: python createAdjacencyMatrix.py input_map_file output_matrix

  Generate the biadjacency matrix from a given bipartite map file.

**direct2undirectEdges**

  Usage: python direct2undirectEdges.py input_network output_network

  Remove the directedness characteristic of a network.

**filterRedundancy**

  Usage: python filterRedundancy.py input_network input_biadjacency_matrix min_distance output_network_gml output_communities

  Remove redundancy from networks including marginally conservation patterns and detect the communities (Check the article for futher informations).

**genBipartite**

  Usage: python genBipartite.py input_msa output_network output_mapX output_mapY

  Generate the bipartite network and an auxilar map file for each projected set from a multiple sequence alignment file.

**genMarginallyBipartite_scale**

  Usage: python genMarginallyBipartite_scale.py input_msa_path output_network_dir output_mapX_dir

  Generate the bipartite networks including marginally conservation patterns from a given directory containing multiple sequence alignment files.

**genProjectionX**

  Usage: python genProjectionX.py input_map_file output_network

  Generate the projected network from a map file (The map files are created together with the bipartite network).

**logw**

  Usage: python logw.py input_network output_network

  Converts the edge weights to a logarithmic scale.

**nodeInt2NodeStr**

  Usage: python nodeInt2NodeStr.py input_int_network node_map_file output_network w? (1-yes, 2-no)

  Converts the nodes nomenclature from numeric to string (The last pattern is related to include or not the edge weights).

**nodeStr2nodeInt**

  Usage: python nodeStr2nodeInt.py input_network output_network output_node_map

  Converts the nodes nomenclature from string to numeric (The last pattern is related to include or not the edge weights).

**normalizeWeights**

  Usage: python normalizeWeights.py input_network output_network

  Normalizes the edges weights to a 0-1 scale.

**removeSamePosEdges**

  Usage: python removeSamePosEdges.py input_network_directory output_directory

  Remove edges linking nodes with the same position on all networks in a folder.

**removeWeights**

  Usage: python removeWeights.py input_network_directory output_directory

  Remove the weights from a edge list file.

**thresholdingCommunity**

  Usage: python thresholdingCommunity.py input_network input_biadjacency_matrix min_distance output_network_gml output_communities

  Find the cutoff with maximizes the number of clusters in a network.

**topEdges**

  Usage: python topEdges.py input_network_directory number_of_elements output_directory

  Retain the top N edges on the network.

**trimmGroups_scale**

  Usage: python trimGroups_scale.py input_map_directory maxFrequency minFrequency output_map_directory

  Remove nodes based on their frequency.

**w_matrix**

  Usage: python w_matrix.py input_network output_matrix

  Generates a weighted biadjacency matrix.
