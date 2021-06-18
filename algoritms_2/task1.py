n = int(input())
a = list(map(int,input().split()))
print(a)
mini = a[0]
sum = 0
for i in range(n):
    mini = min(mini, a[i])
    sum = max(a[i]-mini, sum)
print(sum)