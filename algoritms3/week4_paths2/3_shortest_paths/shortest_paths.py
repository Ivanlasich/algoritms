#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):

    h = queue.Queue()
    distance[s] = 0
    reachable[s] = 1
    for i in range(len(adj)):
        for j in range(len(adj)):
            for k in range(len(adj[j])):
                if (distance[adj[j][k]] > distance[j] + cost[j][k]):
                    distance[adj[j][k]] = distance[j] + cost[j][k]
                    reachable[adj[j][k]] = 1
                    if (i == len(adj)-1):
                        h.put(adj[j][k])
    visited = [0] * len(adj)
    while (not h.empty()):
        u = h.get()
        visited[u] = 1
        shortest[u] = 0
        for i in adj[u]:
            if visited[i] == 0:
                h.put(i)



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

    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*') #no path
        elif shortest[x] == 0:
            print('-') #cycle
        else:
            print(distance[x])

