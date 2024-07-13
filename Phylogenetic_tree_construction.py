from Bio import Phylo
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage

# Example Newick format tree
newick_tree = "((A:0.1,B:0.2),(C:0.3,D:0.4));"
tree = Phylo.read(StringIO(newick_tree), "newick")

# Visualize the tree
fig, axs = plt.subplots(1, 3, figsize=(15, 6))

Phylo.draw(tree, do_show=False, axes=axs[0])
axs[0].set_title('Phylogenetic Tree')

# Simulate and visualize genetic distance matrix
distance_matrix = np.array([[0, 0.1, 0.2, 0.3],
                            [0.1, 0, 0.15, 0.25],
                            [0.2, 0.15, 0, 0.1],
                            [0.3, 0.25, 0.1, 0]])

sns.heatmap(distance_matrix, annot=True, cmap='coolwarm', ax=axs[1])
axs[1].set_title('Genetic Distance Matrix')
axs[1].set_xlabel('Samples')
axs[1].set_ylabel('Samples')

# Convert distance matrix to condensed form
condensed_distance_matrix = squareform(distance_matrix)

# Cluster analysis and dendrogram
linked = linkage(condensed_distance_matrix, 'single')
dendrogram(linked, labels=['A', 'B', 'C', 'D'], ax=axs[2])
axs[2].set_title('Dendrogram')

plt.tight_layout()
plt.show()
