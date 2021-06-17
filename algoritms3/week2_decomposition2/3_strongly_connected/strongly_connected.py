#Uses python3

import sys
import numpy as np
sys.setrecursionlimit(200000)

def dfs1(v):
    used[v] = 1
    for i in adj[v]:
        if(not used[i]):
            dfs1(i)
    order.append(v)

def reverse(adj):
    T_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            T_adj[adj[i][j]].append(i)
    return T_adj

def dfs2(v, T_adj):
    used[v] = 1
    for i in T_adj[v]:
        if(not used[i]):
            dfs2(i, T_adj)

def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
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
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    used = np.zeros(n)
    order = []
    answ = 0
    for i in range(len(adj)):
        if (not used[i]):
            dfs1(i)

    used = np.zeros(n)
    T_adj = reverse(adj)

    for i in range(len(T_adj)):
        x = order.pop()
        if (not used[x]):
            dfs2(x, T_adj)
            answ+=1

    print(int(answ))
