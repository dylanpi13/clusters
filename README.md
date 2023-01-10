# Clusters

This code will generate a dataset to demonstrate k means clustering. This is part of the data analysis of HDX (hydrogen-deuterium exchange) to identify regions of a protein that undergo conformational changes under experimental conditions. 

# Some background on HDX
HDX uses deuterium (an isotope of hydrogen) as a label. When a protein is in a deuterated buffer, the free hydrogens on the protein will exchange with deuterium in the buffer. The degree of deuterium uptake is affected by the 3D structure of the protein, and therefore measuring the level of exchange (in our case with mass spectrometry) gives us information on that structure. 

For example, when an inhibitor is added that changes the conformation of the protein, the residues associated with that conformational change will show a change in deuterium uptake; such as an increase as they become more exposed through unfolding. This way we can begin to understand the specific regions of a protein that are involved in conformational changes

#  Data
A real dataset would have three sets of deuterium uptake data: one for the protein on its own (apo), one for the protein fully saturated with ligand (eq - equilibirum), and a the protein with the ligand in non-equilibrium (non-eq). Each row would correspond to a peptide generated during digest for MS - the enzyme used does not digest predictably, and many overlapping peptides will be generated. 

We compare the difference of non-eq to apo and eq to get two axis, with nine theoretical clusters:

![The 9 clusters: one in each corner, one on each axis, and one in at the origin](https://github.com/dylanpi13/clusters/blob/main/Figure_1.png?raw=true)

At each corner (1, 3, 7, 9) is a difference from both apo and eq, with the sign indicating a positive or negative difference (ie an increase or decrease in uptake). At the origin (5) is no difference from either apo or eq. Difference from only apo (2, 8) or eq (4, 6) is also possible. This is only an example of the extremes, and real data may cluster in between these regions. 

This figure was generated using clusters_1.py.

## Clusters.ipynb 
This workbook will walk through generating an artificial dataset with three features, calculating the difference between "noneq" and "apo" or "eq", scaling the differences to be between -1 and 1, then running k means analysis. The k means analysis also includes assessing the optimum k (number of clusters) based on elbow and silhouette plots. More detail on the latter is given in the workbook. 

# Future directions
I did consider creating a model to predict clusters based on the theoretical categories, or splitting my generated dataset into test and train. The aim of this analysis is to map clusters of HDX behaviour onto 3D structure, and interpret from there; a predictive model would have to be much more complex than a kmeans analysis on a very specific dataset for one protein. Additionally, whether or not you can predict the conformational dynamics of protein based on sequence alone is already an entire field! 

In future I would like to make this more modular and customisable (such as making each section of the workbook into a script that can take local .csvs as input). I would also like to learn to add in functionality from PyMOL for creating 3D models of the clusters on a protein, and calculating hydrogen bonds (an important factor in HDX)
