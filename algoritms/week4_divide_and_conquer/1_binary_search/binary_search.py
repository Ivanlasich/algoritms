# Uses python3
import sys

def binary_search(A, low, high, key):
    if high < low:
        return -1
    mid = int(low + (high-low)/2)
    if key == A[mid]:
        return mid
    else:
        if key < A[mid]:
            return binary_search(A, low, mid-1, key)
        else:
            return binary_search(A, mid+1, high, key)
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,0 , n-1, x), end = ' ')