# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
a =[0,1]

for i in range(2,n+1):
    a.append(a[i-2]+a[i-1])

print(a[n])