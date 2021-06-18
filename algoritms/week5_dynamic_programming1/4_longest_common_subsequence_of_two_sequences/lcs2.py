#Uses python3
import numpy as np
import sys

def lcs2(x, y):

    m = len(x)
    n = len(y)
    lcs = np.zeros((m, n))

    d = 0
    for i in range(1, m):
        for j in range(1, n):
            if (x[i]==y[j]):
                lcs[i ,j] = lcs[i-1, j-1]+1
            else:
                lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1])



    return lcs[m-1,n-1]


n = int(input())
a = [0]
b = [0]
data = list(map(int, input().split()))
a.extend(data)
m = int(input())
data = list(map(int, input().split()))
b.extend(data)
print(int(lcs2(a,b)))