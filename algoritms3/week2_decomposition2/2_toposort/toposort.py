#Uses python3
import numpy as np
import sys

def dfs(adj, used, order, x):
    used[x] = 1
    for i in adj[x]:
        if (not used[i]):
            dfs(adj, used, order, i);
    order.append(x)



def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if (not used[i]):
            dfs(adj, used, order, i)
    #write your code here
    return order

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


    order = toposort(adj)
    order = order[::-1]
    for x in order:
        print(x + 1, end=' ')

