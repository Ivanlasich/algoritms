#Uses python3

import sys
import numpy as np

def reach(adj, x, y):
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            reach(adj, adj[x][i], y)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    data = []
    data.append(n)
    data.append(m)
    for i in range(m+1):
        data1 = list(map(int, input().split()))
        data.extend(data1)
    #print(data)
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = np.zeros(n)
    reach(adj, x, y)
    print(int(visited[y]))

'''
4 4 1 2 3 2 4 3 1 4 1 4
'''