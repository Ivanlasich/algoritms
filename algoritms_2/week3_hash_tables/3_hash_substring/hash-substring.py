import numpy as np



def PolyHash(S, p, x):
    hash = 0
    for c in reversed(S):
        hash = (hash * x + ord(c)) % p
    return hash

def PrecomputeHashes(T, P, p, x):
    H =  [0]*(len(T) - P + 1)
    S = T[-P:]
    H[len(T)-P] = PolyHash(S, p, x)
    y = 1
    for i in range(1, P+1):
        y = (y * x) % p
    for i in reversed(range(len(T) - P)):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + P]))% p
    return H

def RabinKarp(T, P):
    p = 1000000007
    x = np.random.randint(1, p)
    result = []
    pHash = PolyHash(P, p, x)
    H = PrecomputeHashes(T, len(P), p, x)
    for i in range(0, len(T) - len(P)+1):
        if pHash==H[i] and T[i:i + len(P)] == P:
            print(i, end=' ')


s1 = input()
s2 = input()
RabinKarp(s2, s1)
