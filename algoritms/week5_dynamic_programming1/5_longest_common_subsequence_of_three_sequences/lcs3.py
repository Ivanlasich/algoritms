#Uses python3
import numpy as np
import sys

def lcs3(a, b, c):
    n = len(a)
    m = len(b)
    k = len(c)
    lcs = np.zeros((n, m, k))

    d = 0
    for i in range(1, n):
        for j in range(1, m):
            for l in range(1, k):

                if (a[i] == b[j]==c[l]):
                    lcs[i, j, l] = lcs[i - 1, j - 1, l - 1] + 1
                else:
                    lcs[i, j, l] = max(lcs[i - 1][j][l], lcs[i][j - 1][l], lcs[i][j][l-1])

    return lcs[n-1,m-1,k-1]

a = [0]
b = [0]
c = [0]

n = int(input())
data = list(map(int, input().split()))
a.extend(data)

m = int(input())
data = list(map(int, input().split()))
b.extend(data)

k = int(input())
data = list(map(int, input().split()))
c.extend(data)

print(int(lcs3(a, b, c)))

