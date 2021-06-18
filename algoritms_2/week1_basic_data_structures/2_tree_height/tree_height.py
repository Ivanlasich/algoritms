# python3

import sys
import threading
import numpy as np
def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def get_height(n, parents, i):
    if (parents[i] < 0):
        heights[i] = 1
        return 1
    if( heights[i]>=0 ):
        return heights[i]

    heights[i] = get_height(n, parents, parents[i]) + 1

    return heights[i]




def main():
    n = int(input())
    parents = list(map(int, input().split()))
    global heights
    heights = -np.ones(n)

    for i in range(n):
        get_height(n, parents, i)

    print(int(max(heights)))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
