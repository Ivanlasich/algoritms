# Uses python3
import sys
import random
def majority_element(a, n):
    for i in range(n):
        currentElement=a[i]
        count=0
        for j in range(n):
            if a[j]==currentElement:
                count=count+1
        if count>n/2:
            return 1
    return -1;


def get_majority_element(a, n):

    a.sort()
    ans = 1
    maxi = 1
    for i in range(0, n - 1):
        if (a[i] == a[i + 1]):
            ans = ans + 1
            maxi = max(ans, maxi)

        else:
            maxi = max(ans, maxi)

            ans = 1

    if maxi>n/2:
        return 1

    return 0

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    print(get_majority_element(data, n))

'''   
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
'''
