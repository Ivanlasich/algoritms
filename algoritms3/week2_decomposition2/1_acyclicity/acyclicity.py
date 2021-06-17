#Uses python3
import numpy as np
import sys

def acyclic(adj, v):
    color[v] = 1
    for i in (adj[v]):
        if (color[i] == 0):
            acyclic(adj, i)
        if (color[i] == 1):
            answ[0] = 1

    color[v] = 2
    return 0

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
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    color = np.zeros(n)
    answ = np.zeros(1)

    for i in range(n):
        acyclic(adj, i)

    print(int(answ[0]))
