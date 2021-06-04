# -*- coding: utf-8 -*-
#!/usr/bin/env python

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import sys
from print_graph import print_graph



pays = input("Entrez un pays: ")
ville = input("Entrez une ville: ")
quartier = input("Entrez un quartier ou rien: ")

place = ville + ", " + pays
if (quartier != ""):
    place = quartier + ", " + place

print("Vous avez choisis : " + place )

try:
    G = ox.graph_from_place(place, network_type='drive')
except:
    print( "Ce lieu n'existe pas !")
    sys.exit(0)

nodes = list(G.nodes)
edges = list(G.edges(data=True))

edges_list = []
for (x, y, info) in edges:
    edges_list.append((nodes.index(x), nodes.index(y), info["length"]))

def solvePractical(num_vertices, edge_list):
    G = nx.Graph()
    for u, v, w in edge_list:
        G.add_edge(u, v, weight=w)
    
    print_graph(G)

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
    
    return num_vertices, circuit

print("\nVoici l'odre des sommets à parcourir : \n", solvePractical(len(edges), edges_list))