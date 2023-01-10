# Clusters

This code will generate a dataset to demonstrate k means clustering. This is part of the data analysis of HDX (hydrogen-deuterium exchange) to identify regions of a protein that undergo conformational changes under experimental conditions. 

# Some background on HDX
HDX uses deuterium (an isotope of hydrogen) as a label. When a protein is in a deuterated buffer, the free hydrogens on the protein will exchange with deuterium in the buffer. The degree of deuterium uptake is affected by the 3D structure of the protein, and therefore measuring the level of exchange (in our case with mass spectrometry) gives us information on that structure. 

For example, when an inhibitor is added that changes the conformation of the protein, the residues associated with that conformational change will show a change in deuterium uptake; such as an increase as they become more exposed through unfolding. This way we can begin to understand the specific regions of a protein that are involved in conformational changes

#  Clustering
A real dataset would have three sets of deuterium uptake data: one for the protein on its own (apo), one for the protein fully saturated with ligand (eq - equilibirum), and a the protein with the ligand in non-equilibrium (non-eq). We compare the difference of non-eq to apo and eq to get two axis, with nine theoretical clusters:

