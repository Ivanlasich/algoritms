#Uses python3

import sys
import numpy as np



def search(adj, x):
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            search(adj, adj[x][i])


def number_of_components(adj):
    result = 0
    for i in range(len(adj)):
        if not visited[i]:
            search(adj, i)
            result+=1
    return result

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
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = np.zeros(n)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
