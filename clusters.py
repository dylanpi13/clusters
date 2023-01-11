import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

from string import ascii_lowercase

#generate data but with specified centres
centres = [(-0.8, 0.8), (-0.8, 0), (-0.8, -0.8), (0, 0.8), (0, 0), (0, -0.8), (0.8, 0.8), (0.8, 0), (0.8, -0.8)]
theory, labels_true = make_blobs(
    n_samples=900, centers=centres, cluster_std=0.05, random_state=0
)

#kmeans just for colouring!
kmeans = KMeans(n_clusters = 9).fit(theory)
centers = pd.DataFrame(kmeans.cluster_centers_, columns =["noneq_apo", "noneq_eq"])
label = kmeans.labels_

plt.close("all")
plt.figure(1)
plt.clf()

#setting axes, plotting origin
ax = plt.gca()
plt.axhline(0, color='lightgrey', zorder=0)
plt.axvline(0, color='lightgrey', zorder=0)
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_xticks([-1, 0, 1])
ax.set_yticks([-1, 0, 1])

colors = plt.cycler("color", sns.color_palette("cool", 9)) #allows matplotlib to cycle through plot colours

for k, col in zip(range(0,9), colors):
    class_members = label == k
    centroids=centres[k]
    plt.scatter(
        theory[class_members, 0], theory[class_members, 1], color=col["color"], marker="o", s=20,
    ) #plot individual data points
    plt.scatter(
    centroids[0], centroids[1], s=150, color="black", marker=r"$ {} $".format(k+1), zorder=10
    ) #plot centroid as letter

plt.xlabel("Difference from Apo")
plt.ylabel("Difference from Eq")
plt.title("Theoretical behaviour")
plt.show()
