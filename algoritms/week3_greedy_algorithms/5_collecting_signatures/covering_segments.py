# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    n = len(dots)
    points = []
    i = 0
    while segments[i][1]<=segments[i+1][0]:
        i=i+1;

    return points

if __name__ == '__main__':
    n = int(input())
    dots=[]
    ans=[]
    for i in range(n):
        data = list(map(int, input().split()))
        dots.append((data[0],data[1]))
    dots.sort(key=lambda x: x[1])
    point = dots[0][1]
    for i in range(1,n):
        if(point < dots[i][0]):
          ans.append(point)
          point=dots[i][1]
    ans.append(point)

    print(len(ans))
    for i in (ans):
        print(i,end=" ")
#1 4 5 8 9 10 14 15 18 23 26 28 29 30 32 34 35 36 40 41 44 46 49 52 54 56 58 61 62 63 65 67 70 74 77 78 79 81 84 87 91 93 95
#1 4 5 8 9 10 14 15 18 23 26 28 29 30 32 34 35 36 40 41 44 46 49 52 54 56 58 61 62 63 65 67 70 74 77 78 79 81 84 87 91 93 95