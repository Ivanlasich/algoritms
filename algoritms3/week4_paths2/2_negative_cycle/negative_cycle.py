#Uses python3
import sys
import math
import numpy as np

def Relax(u, v, dist, cost):
    if ( dist[v] > dist[u] + cost[u][v]):
        dist[v] = dist[u] + cost[u][v]



def negative_cycle(adj, cost):
    dist = np.zeros(len(adj))
    for i in range(len(adj)):
        dist[i] = 100009


    for i in range(len(adj)):
        ind = 0
        for j in range(len(adj)):
            for k in range(len(adj[j])):
                if (dist[adj[j][k]] > dist[j] + cost[j][k]):
                    dist[adj[j][k]] = dist[j] + cost[j][k]
                    ind = 1

    #write your code here
    return ind


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    data = []
    data.append(n)
    data.append(m)

    for i in range(m):
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

    print(negative_cycle(adj, cost))
