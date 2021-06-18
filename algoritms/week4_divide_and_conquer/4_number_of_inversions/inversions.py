# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

def Merge(B, C):
    D = []
    q = 0
    p = 0
    ans=0
    while B!=[] and C!=[]:
        b = B[0]
        c = C[0]
        if (b<=c):
            B.remove(b)
            D.append(b)
            q = q + 1
        else:
            ans=ans+len(B)
            C.remove(c)
            D.append(c)
            p = p + 1

    if(B==[]):
        D[p + q:] = C
    else:
        D[p + q:] = B
    return D, ans
def ex(a,b):
    return a,b


def MergeSort(A, n):

    if n == 1:
        return  A, 0
    m = int(n/2)
    B, ans1 = MergeSort(A[:m], m)
    C, ans2 = MergeSort(A[m:], n-m)
    a, ans = Merge(B, C)
    ans = ans1+ ans2 +ans
    return a, ans
if __name__ == '__main__':
    n = int(input())
    data = list(map(int,input().split()))
    a, ans = MergeSort(data, n)
    print(ans)

