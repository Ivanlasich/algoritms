#Uses python3

import sys
import queue
import numpy as np


def distance(adj, s, t):
    dist = np.zeros(len(adj))
    a = queue.Queue()
    for i in range(len(adj)):
        dist[i] = -1
    dist[s] = 0
    a.put(s)
    while (not a.empty()):
        u = a.get()
        for i in adj[u]:
            if dist[i] == -1:
                a.put(i)
                dist[i] = dist[u] + 1
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
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1


    print(int(distance(adj, s, t)))
