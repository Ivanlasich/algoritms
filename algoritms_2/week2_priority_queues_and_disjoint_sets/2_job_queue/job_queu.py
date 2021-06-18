global size

def Insert(p):

    H[size] = p
    SiftUp(size)

def ExtcactMin():
    result = H[0]
    H[0] = H[size]
    SiftDown(0)
    return result



def Parent(i):
    return (i-1)//2

def LeftChild(i):
    return 2*i+1

def RightChild(i):
    return 2*i+2

def SiftUp(i):
    while i > 0 and H[Parent(i)][0] > H[i][0]:
        H[Parent(i)], H[i] = H[i], H[Parent(i)]
        i = Parent(i)
    while i > 0 and H[Parent(i)][0] == H[i][0] and H[Parent(i)][1] > H[i][1]:
        H[Parent(i)], H[i] = H[i], H[Parent(i)]
        i = Parent(i)


def SiftDown(i):
    maxindex = i
    l = LeftChild(i)

    if (l <= (size) and H[l][0] < H[maxindex][0]):
        maxindex = l

    if (l <= (size) and H[l][0] == H[maxindex][0] and H[l][1] < H[maxindex][1]) :
        maxindex = l



    r = RightChild(i)

    if (r <= (size) and H[r][0] < H[maxindex][0]):
        maxindex = r
    if (r <= (size) and H[r][0] == H[maxindex][0] and H[r][1] < H[maxindex][1]) :
        maxindex = r


    if (i != maxindex):
        H[i], H[maxindex] = H[maxindex], H[i]
        SiftDown(maxindex)



def build_heap():
    for i in range(size//2, -1, -1):
        SiftDown(i)


n, m = map(int, input().split())
global size
size = n
size = size - 1
jobs = list(map(int, input().split()))
H = []

for i in range(size+1):
    H.append((jobs[i], i, jobs[i]))
    print(i, end=" ")
    print(0)
build_heap()

if(n < m):
    for i in range(n, m):
        result = ExtcactMin()
        print(result[1], end=" ")
        print(result[0])
        Insert((jobs[i] + result[0], result[1], result[0]))





