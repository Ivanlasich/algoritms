# python3
import sys


def compute_min_refills(n, tank, stops):
    numRefills=0
    currentRefill=0
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n) and (stops[currentRefill+1]-stops[lastRefill]<=tank):
            currentRefill=currentRefill+1
        if(currentRefill==lastRefill):
            return -1
        if(currentRefill<=n):
            numRefills=numRefills+1
    return numRefills

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stop=[]
    stop.append(0)
    data = list(map(int, input().split()))
    stop.extend(data)
    stop.append(d)
    print(compute_min_refills(len(stop)-2, m, stop))
