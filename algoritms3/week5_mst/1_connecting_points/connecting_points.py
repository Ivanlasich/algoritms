#Uses python3
import sys
import math
import numpy as np

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def union(i, j, vertexs, rank):
    i_id = Find(i, vertexs)
    j_id = Find(j, vertexs)
    if (i_id != j_id):
        if (rank[i_id]> rank[j_id]):
            vertexs[j_id] = i_id
        else:
            vertexs[i_id] = j_id
            if (rank[i_id] == rank[j_id]):
                rank[j_id] += 1


def Find(i, vertexs):
    i = int(i)
    if (i != int(vertexs[i])):
        vertexs[i] = Find(vertexs[i], vertexs)
    return vertexs[int(i)]

def minimum_distance(x, y):
    result = 0.
    vertexs = [0]*n
    edges = []
    rank = np.zeros(n)
    for i in range(n):
        vertexs[i] = int(i)

    for i in range(n):
        for j in range(i+1, n):
            edges.append((distance(x[i], y[i], x[j], y[j]), int(i), int(j)))
    edges.sort()
    for edge in edges:
        if (Find(int(vertexs[edge[1]]), vertexs) != Find(int(vertexs[edge[2]]), vertexs)):
            result += edge[0]
            union(int(vertexs[edge[1]]), int(vertexs[edge[2]]), vertexs, rank)


    #write your code here
    return result


if __name__ == '__main__':
    n = int(input())
    data = []
    data.append(n)


    for i in range(n):
        data1 = list(map(int, input().split()))
        data.extend(data1)

    n = data[0]
    x = data[1::2]
    y = data[2::2]

    print("{0:.9f}".format(minimum_distance(x, y)))
