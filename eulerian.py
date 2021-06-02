import itertools
from dijkstra import dijkstra


def find_combination_odd_nodes(nodes):
    res = []
    for x in nodes:
        for y in nodes:
            if x != y and (x, y) not in res and (y, x) not in res:
                res.append((x, y))
    return res


def find_edge(edge_list, x, y):
    res = None
    for (a, b, w) in edge_list:
        if (a == x and b == y) or (a == y and b == x):
            res = (a, b, w)
    return res


def make_eulerian(num_vertices, edge_list, odd_vert_list):
    list_comb = find_combination_odd_nodes(odd_vert_list)
    reslist = []
    for (a, b) in list_comb:
        d = [a, b]
        d.extend(dijkstra(num_vertices, edge_list, a, b))
        reslist.append(tuple(d))

    new_edge_list = edge_list.copy()

    # sort by the cost
    reslist.sort(key=lambda tup: tup[2])

    while reslist:
        i = 0
        len_reslist = len(reslist[0][3]) - 1

        # append new edges (duplicating edge)
        while i < len_reslist:
            (a, b) = (reslist[0][3][i], reslist[0][3][i + 1])
            new_edge_list.append(find_edge(edge_list, a, b))
            i += 1

        # remove all tuple with x and y from reslist[0]
        reslist = [ elm for elm in reslist 
                   if reslist[0][0] not in elm[0:2] and reslist[0][1] not in elm[0:2]]
    return new_edge_list