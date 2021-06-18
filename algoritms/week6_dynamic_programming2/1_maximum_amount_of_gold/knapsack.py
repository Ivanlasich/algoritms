# Uses python3
import sys
import numpy as np

def optimal_weight(W, weight, n):
    value = np.zeros((W+1,n+1))
    for i in range(1,n+1):
        for w in range(1,W+1):
            value[w, i]=value[w, i-1]
            if (weight[i]<=w):
                val = value[w - weight[i], i-1] + weight[i]
                if value[w, i] < val:
                    value[w, i] = val
    return value[W,n]

data = list(map(int, input().split()))
W = data[0]
n = data[1]
w=[0]
data =  list(map(int, input().split()))
w.extend(data)
print(int(optimal_weight(W, w, n)))

