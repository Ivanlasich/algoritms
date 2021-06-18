# Uses python3
import numpy as np
import math
def evalt(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def get_maximum_value():
    for s in range (1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j)

def MinAndMax(i, j):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

s = input()
d=[]
op=[]
for i in s:
    if i.isdigit():
        d.append(i)
    else:
        op.append(i)
n = len(d)

m=np.zeros((n,n))
M=np.zeros((n,n))
for i in range(n):
    m[i][i] = d[i]
    M[i][i] = d[i]

for i in range(n):
    m[i][i] = int(d[i])
    M[i][i] = int(d[i])

get_maximum_value()
print( int(M[0][n-1]))