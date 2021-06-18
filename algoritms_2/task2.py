import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            if(a[i] != x):
                d[a[i]]+=1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

def create_array(size):
    return [random.choice(list(range(10))) for _ in range(size)]


def sotrik(a, l, r):
    if (l >= l):
        return
    i = l
    j = r
    m = (l+r)//2
    while True:
        while(a[i]<a[m]):
            i+=1
        while (a[j] > a[m]):
            j -= 1

        if(i<=j):
            a[i], a[j] = a[j], a[i]
            i+=1
            j-=1
        if ( i>j ):
            break
    sotrik(a,l,m)
    sotrik(a,m+1,r)

indexes={}
n = int(input())
d = {}
a = create_array(n)
for i in a:
    d[i] = 0
print(a)
randomized_quick_sort(a, 0, n - 1)
print(a)
print(d)