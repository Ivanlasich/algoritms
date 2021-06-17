#Uses python3

import sys
import queue
import numpy as np

def Relax(u, v, dist):
    if ( dist[v] > dist[u] + cost[u][v]):
        dist[v] = dist[u] + cost[u][v]


def distance(adj, cost, s, t):
    dist = np.zeros(len(adj))
    for i in range(len(adj)):
        dist[i] = float('inf')
    dist[s] = 0
    h = queue.PriorityQueue()
    h.put((dist[s],s))
    while(not h.empty()):
        u = h.get()
        for i in range(len(adj[u[1]])):
            if (dist[adj[u[1]][i]] > dist[u[1]] + cost[u[1]][i]):
                dist[adj[u[1]][i]] = dist[u[1]] + cost[u[1]][i]
                h.put((dist[adj[u[1]][i]], adj[u[1]][i]))
    if(dist[t]==float('inf')):
        return -1
    #write your code here
    return dist[t]


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    data = []
    data.append(n)
    data.append(m)
    for i in range(m+1):
        data1 = list(map(int, input().split()))
        data.extend(data1)

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1


    print(int(distance(adj, cost, s, t)))
