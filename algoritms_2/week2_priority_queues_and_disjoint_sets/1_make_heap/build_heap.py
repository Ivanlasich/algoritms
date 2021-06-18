# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def LeftChild(i):
    return 2*i+1

def RightChild(i):
    return 2*i+2

def SiftDown(i):
    maxindex = i
    l = LeftChild(i)
    if (l <= (size-1) and H[l] < H[maxindex]):
        maxindex = l

    r = RightChild(i)

    if (r <= (size-1) and H[r] < H[maxindex]):
        maxindex = r

    if (i != maxindex):
        swap.append((i, maxindex))
        H[i], H[maxindex] = H[maxindex], H[i]
        SiftDown(maxindex)


def build_heap_(n):
    for i in range(n//2, -1, -1):
        SiftDown(i)


def main():
    global H
    global size
    global swap
    swap = []
    size = int(input())
    H = list(map(int, input().split()))
    build_heap_(size)

    print(len(swap))
    for i in swap:
        print(i[0], end=' ')
        print(i[1])
if __name__ == "__main__":
    main()
