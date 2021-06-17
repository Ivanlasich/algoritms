#Uses python3

import sys
import queue
import numpy as np
global answ

def bipartite(adj):
    #write your code here
    return -1

def bipartite(adj):
    colour = np.zeros(len(adj))
    a = queue.Queue()
    for i in range(len(adj)):
        if (colour[i] == 0):
            colour[i] = 1
            a.put(i)
            while (not a.empty()):
                u = a.get()
                for i in adj[u]:
                    if colour[i] == 0:
                        a.put(i)
                        colour[i] = -colour[u]
                    elif (colour[i] == colour[u]):
                        return 0
    return 1
'''
def dfs(adj, x, c):
    colour[x] = c
    for i in adj[x]:
        if (not colour[i]):
            return dfs(adj, i, -c)
        elif (colour[i] == c):
            return 0
        else:
            return 1
'''


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    data = []
    data.append(n)
    data.append(m)
    for i in range(m):
        data1 = list(map(int, input().split()))
        data.extend(data1)

    answ = 1
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    '''    
    colour = np.zeros(n)
    for i in range(n):
        if (not colour[i]):
            answ = dfs(adj, i, 1)

        if answ == 0:
            break
    print(int(answ))
    '''
    print(int(bipartite(adj)))