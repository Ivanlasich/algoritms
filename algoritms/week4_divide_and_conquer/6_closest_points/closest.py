#Uses python3
import sys
import math

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def filtration(arr, point, d):
    ans=[]
    for i in range(0, len(arr)):
        dist = math.fabs(point-arr[i][0])
        if dist < d:
            ans.append(arr[i])
    return ans

def mid_distance(arr):
    d = distance(arr[0],arr[-1])
    l = len(arr)
    for i in range(l):
        j=1
        while(j< min(7, l - i)):
            d = min(d, distance(arr[i], arr[i+j]))
            j+=1

    return d



def minimum_distance(arr):
    l = len(arr)
    d = distance(arr[0],arr[-1])
    if (l <= 3):
        for i in range(l):
            for j in range(i+1, l):
                d = min(d, distance(arr[i], arr[j]))
        return d
    arr_1 = arr[:l//2]
    arr_2 = arr[l//2:]
    d = min(minimum_distance(arr_1),minimum_distance(arr_2))
    point = (arr_1[-1][0]+arr_2[0][0])/2
    arr_0=filtration(arr_1, point, d)
    arr_22 = filtration(arr_2, point, d)
    arr_0.extend(arr_2)
    arr_0.sort(key=lambda x:x[1])
    d = min(d, mid_distance(arr_0))

    return d

if __name__ == '__main__':
    n = int(input())
    points=[]
    for i in range(n):
        data = list(map(int, input().split()))
        points.append((data[0],data[1]))
    points.sort()


    print(round(minimum_distance(points), 4))
