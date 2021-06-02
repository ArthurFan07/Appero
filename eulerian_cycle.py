import itertools
from eulerian import make_eulerian

def find_eulerian_cycle(n, edges):
    if n == 0 or edges == []:
        return []

    adj = [[] for x in range(n)]

    for (x, y, w) in edges:
        adj[x].append(y)
        adj[y].append(x)

    edges_count = dict()
    for i in range(n):
        edges_count[i] = len(adj[i])

    curr = [0]
    res = []
    tmp_curr = 0

    while len(curr):
        if edges_count[tmp_curr]:
            curr.append(tmp_curr)
            next = adj[tmp_curr].pop()
            adj[next].remove(tmp_curr)

            edges_count[tmp_curr] -= 1
            edges_count[next] -= 1
            tmp_curr = next
        else:
            res.append(tmp_curr)
            tmp_curr = curr.pop()

    return res[::-1]


def find_path(u, v, next):
    if next[u][v] == -1:
        return []

    res = [u]
    while u != v:
        u = next[u][v]
        res.append(u)

    return res

def odd_vertices(n, edges):
    res = []

    for i in range(n):
        L = [(x, y) for x, y, z in edges if (i == x or i == y) and x != y]
        if len(L) % 2 == 1:
            res.append(i)

    return res

def solve(num_vertices, edge_list):
    odd_vert_list = odd_vertices(num_vertices, edge_list)
    
    if len(odd_vert_list) == 0:
        return find_eulerian_cycle(num_vertices, edge_list)

    new_edge_list = make_eulerian(num_vertices, edge_list, odd_vert_list)

    return find_eulerian_cycle(num_vertices, new_edge_list)