"""
Dataset: 
“TUDataset,” TUDataset, 2020. https://chrsmrrs.github.io/datasets/
"""


import networkx as nx 
import matplotlib.pyplot as plt


G = nx.Graph()
with open("BZR_A.txt") as f:
    for line in f:
        row, col = line.strip().split(",")
        G.add_edge(int(row), int(col))


# degree distribution 
degree_dist = dict(G.degree())
print("Degree distribution:", degree_dist)

# betweenness centrality 
betweenness = nx.betweenness_centrality(G)
print("Betweenness centrality:", betweenness)

# clustering coefficient
clustering_coefficients = nx.clustering(G)
average_clustering_coefficient = sum(clustering_coefficients.values()) / len(clustering_coefficients)
print("Average Clustering Coefficient:", average_clustering_coefficient)

# boxicity 
boxicity = 1
for k in range(2, len(G.nodes()) + 1):
    cliques = nx.find_cliques(G.to_undirected())
    for C in cliques:
        if len(C) >= k and nx.is_chordal(nx.subgraph(G.to_undirected(), C)):
            boxicity = max(boxicity, k)
print("Boxicity:", boxicity)

# Strength
strength_dict = nx.algorithms.link_analysis.pagerank_alg.pagerank(G, alpha=0.85, max_iter=100, tol=1e-06)
node_strengths = [strength_dict[node] for node in G.nodes]
graph_strength = sum(node_strengths)
print("Graph Strength:", graph_strength)

# Edge Connectivity
edge_connectivity = nx.edge_connectivity(G)
print("Edge Connectivity:", edge_connectivity)

# Chromatic Number
chromatic_number = nx.algorithms.coloring.greedy_color(G, strategy="largest_first")
print("Chromatic Number:", len(set(chromatic_number.values())))

# Characteristic Polynomial
characteristic_polynomial = nx.adjacency_spectrum(G).tolist()
print("Characteristic Polynomial:", characteristic_polynomial)


nx.draw(G)
plt.show()