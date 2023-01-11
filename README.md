
# Clusters.ipynb 
This project is for clustering peptides based on changes in HDX (hydrogen-deuterium exchange) to identify regions of a protein that are associated with conformational transitions. This has been tested on actual experimental data, but that cannot be shared here,

The workbook will walk through generating an artificial dataset with three features, calculating the difference between those features, scaling the differences to be between -1 and 1, then running k means analysis. The k means analysis also includes assessing the optimum k (number of clusters) based on elbow and silhouette plots. More detail on the latter is given in the workbook. 

All of the packages used come installed with Anaconda. The elbow plot for kmeans may give a warning about a known issue with memory leaks on windows and gives instructions on how to fix it! 

# Some background on HDX
HDX uses deuterium (an isotope of hydrogen) as a label. When a protein is in a deuterated buffer, the free hydrogens on the protein will exchange with deuterium in the buffer. The degree of deuterium uptake is affected by the 3D structure of the protein, and therefore measuring the level of exchange in different conditions (in our case using mass spectrometry) gives us information on that structure. 

Each row in a real dataset would correspond to a peptide generated during digest for MS. It's worth noting that the enzyme used does not digest predictably and many overlapping peptides will be generated. The data has three features: two baselines (apo & eq) and a non-equilibrium dataset. We compare the difference of non-eq to apo and eq to get two axis, with nine theoretical clusters:

![The 9 clusters: one in each corner, one on each axis, and one in at the origin](https://github.com/dylanpi13/clusters/blob/main/Figure_1.png?raw=true)

At each corner (1, 3, 7, 9) is a difference from both apo and eq, with the sign indicating a positive or negative difference (ie an increase or decrease in uptake). At the origin (5) is no difference from either apo or eq. Difference from only apo (2, 8) or eq (4, 6) is also possible. This is represents the extremes, and real data may cluster in between these regions. 

This figure was generated using clusters.py.

# Future directions
The overall aim of this analysis is to produce clusters of peptides to then map onto a 3D structure of the protein and interpret from there. As HDX is influenced by global and local structural dynamics, a predictive model would have to be much more complex than kmeans alone and more importantly needs scientific justification!  Predicting the conformational dynamics of proteins based on sequence is an entire field of computational chemistry :P 

In future I would like to make this more modular and customisable (such as making each section of the workbook into a script that can take local .csv files as input). I would also like to learn to add in functionality from PyMOL for creating 3D models of the clusters on a protein, and calculating hydrogen bonds (an important factor in HDX).
