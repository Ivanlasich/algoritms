# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

n = int(input())
a =[0,1]

for i in range(2,n+1):
    a.append((a[i-2]+a[i-1])% 10)

print(a[n])
