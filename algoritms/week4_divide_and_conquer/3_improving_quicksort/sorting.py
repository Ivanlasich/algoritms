# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    m1 = l
    for i in range(l + 1, r ):
        if a[i] < x:
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
    a[l], a[m1] = a[m1], a[l]
    m2 = m1
    for i in range(m2 + 1, r ):
        if a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]

    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
def create_array(size):
    return [random.choice(list(range(10))) for _ in range(size)]

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

def quicksort3(arr, l, r):

    if l + 1 >= r:
        return

    m = random.randint(l, r-1)

    arr[l], arr[m] = arr[m], arr[l]

    m1, m2 = partition3(arr, l, r)

    quicksort3(arr, l, m1)
    quicksort3(arr, m2+1, r)




if __name__ == '__main__':

    n = int(input())
    a = list(map(int, input().split()))
    quicksort3(a, 0, n )
    for i in range(n):
        print(a[i], end=' ')
