import math

def adjacent(n, edges):
    res = [[] for i in range(n)]
    for (x, y, w) in edges:
        res[x].append((y, w))
        res[y].append((x, w))
    return res


def dijkstra(n, edges, src, dst):
    if n == 0 or edges == []:
        return math.inf

    if src == dst:
        return 0

    adj = adjacent(n, edges)

    parents = [-1] * n
    dist = [math.inf] * n
    visit = [False] * n

    dist[src] = 0
    q = [src]

    while q:
        x = q.pop(0)
        for y, w in adj[x]:
            if dist[y] > dist[x] + w:
                dist[y] = dist[x] + w
                parents[y] = x

            if not visit[y]:
                visit[y] = True
                q.append(y)

    i = dst
    res = []

    while parents[i] != -1:
        res.insert(0, i)
        i = parents[i]

    res.insert(0, i)

    return (dist[dst], res)