import matplotlib.pyplot as plt
import networkx as nx

def print_graph(G):
    options = {
      'node_color' : 'red',
      'node_size'  : 100,
      'edge_color' : 'tab:grey',
      'with_labels': True
    }
    plt.figure()
    nx.draw(G, **options)
    plt.show()