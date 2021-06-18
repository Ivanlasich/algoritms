# Uses python3
import sys
import itertools
import numpy as np

def optimal_weight(W, weight, n):
    ans=0
    value = np.zeros((W+1,n+1))
    for i in range(1,n+1):
        for w in range(1,W+1):
            value[w, i]=value[w, i-1]
            if (weight[i]<=w):
                val = value[w - weight[i], i-1] + weight[i]
                if value[w, i] < val:
                    value[w, i] = val
        if(value[w, i]==W):
            ans=ans+1
    return ans


def optimal_values(A, w, W):
    i = len(w)-1
    ans = np.zeros(i + 1)
    while i != 0:
        if A[W, i] == A[W - w[i], i - 1] + w[i]:
            ans[i] = 1
            W = W - w[i]
            i = i - 1
        elif A[W, i] == A[W, i - 1]:
            ans[i] = 0
            i = i - 1
    return ans




n = int(input())
w=[0]
data =  list(map(int, input().split()))
w.extend(data)
if(sum(data)%3!=0):
    print(0)
else:
    W = (sum(data)//3)
    ans = optimal_weight(W, w, len(w) - 1)
    if(ans>=3):
        print(1)
    else:
        print(0)
