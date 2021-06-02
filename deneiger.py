# -*- coding: utf-8 -*-
#!/usr/bin/env python

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

G = ox.graph_from_place('Ivry-sur-Seine, France', network_type='drive')
nodes = list(G.nodes)
edges = list(G.edges(data=True))

edges_list = []
for (x, y, info) in edges:
    edges_list.append((nodes.index(x), nodes.index(y), info["length"]))

def solvePractical(num_vertices, edge_list):
    G = nx.Graph()
    for u, v, w in edge_list:
        G.add_edge(u, v, weight=w)

    if G.is_directed() and not nx.is_weakly_connected(G):
        raise nx.NetworkXError("G is not connected")
        
    if not G.is_directed() and not nx.is_connected(G):
        raise nx.NetworkXError("G is not connected")

    circuit = []
    
    if nx.is_eulerian(G):
        circuit = [i for i in nx.eulerian_circuit(G)]
    else:
        G = nx.algorithms.euler.eulerize(G)
        circuit = [i for i in nx.eulerian_circuit(G)]
    
    print(G)
    nx.draw(G)
    plt.show()
    return num_vertices, circuit

print(solvePractical(len(edges), edges_list))