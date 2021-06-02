# -*- coding: utf-8 -*-
#!/usr/bin/env python

import osmnx as ox
from eulerian_cycle import solve

G = ox.graph_from_place('Ivry-sur-Seine, France', network_type='drive')
nodes = list(G.nodes)
edges = list(G.edges(data=True))

edges_list = []
for (x, y, info) in edges:
    edges_list.append((nodes.index(x), nodes.index(y), info["length"]))

print(solve(len(nodes), edges_list))



