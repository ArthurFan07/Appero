# -*- coding: utf-8 -*-
#!/usr/bin/env python

import osmnx as ox
import sys
from eulerian_cycle import solve

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

print("\nVoici l'odre des sommets à parcourir : \n", solve(len(nodes), edges_list))



