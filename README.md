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
**calculateDegrees_scale**
**calculateWeightedDegrees_scale**
**createBiadjancecyMatrix**
**createBiadjancecyMatrix2**
**direct2undirectEdges**
**filterRedundancy**
**genBipartite**
**genMarginallyBipartite_scale**
**genProjectionX**
**logw**
**nodeInt2NodeStr**
**nodeStr2nodeInt**
**normalizeWeights**
**removeSamePosEdges**
**removeWeights**
**thresholdingCommunity**
**topEdges**
**trimBipartite**
**trimmGroups_scale**
**w_matrix**
