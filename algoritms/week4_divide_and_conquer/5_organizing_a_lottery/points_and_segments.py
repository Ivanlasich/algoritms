# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    data = list(map(int, input().split()))
    points=[]
    n = data[0]
    k = data[1]
    j=0
    for i in range(n):
        data = list(map(int, input().split()))
        points.append((data[0],'l'))
        points.append((data[1],'r'))

    data = list(map(int, input().split()))
    for i in data:
        points.append((i, 'p'))
    points.sort()
    ans=0
    answer=dict()
    for i in points:
        if (i[1]=='l'):
            ans+=1
        if(i[1]=='r'):

            ans-=1
        if(i[1]=='p'):
            answer[i[0]]=ans

    for i in data:
        print(answer[i], end=' ')

