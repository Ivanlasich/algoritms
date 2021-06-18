# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i=1
    while n != 0:
       n = n - i
       if  n/2 < i:
           summands.append(n)
           n=0
       else:
           summands.append(i)
       i=i+1
    return summands

if __name__ == '__main__':
    n = int(input())
    m = n
    summands = []
    i = 1
    while n != 0:
        if n - i < i+1:
            summands.append(n)
            n = 0
        else:
            summands.append(i)
            n = n - i
            i = i + 1
    print(len(summands))
    for i in summands:
        print(i, end=" ")
