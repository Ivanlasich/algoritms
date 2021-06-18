# Uses python3
import sys
import numpy as np

n = int(input())
num = np.zeros(n+1)
sequence = np.zeros(n+2)
sequence[1] = 1

for i in range(2, n+1):
    if ( i% 3 == 0):
        if(i%2==0):
            num[i] = min(num[i//3], num[i//2], num[i-1]) + 1
            if(num[i] == num[i//3]+1):
                sequence[i]=(i//3)
            elif (num[i] == num[i//2]+1):
                sequence[i]=(i//2)
            else:
                sequence[i]=(i-1)
        else:
            num[i] = min(num[i//3], num[i-1])+1
            if (num[i] == num[i // 3] + 1):
                sequence[i] = (i // 3)
            else:
                sequence[i] = (i - 1)
    elif (i % 2 == 0):
            num[i] = min(num[i//2], num[i-1]) + 1
            if (num[i] == num[i // 2] + 1):
                sequence[i] = (i // 2)
            else:
                sequence[i] = (i - 1)
    else:
            num[i]= num[i-1]+1
            sequence[i] = int(i - 1)
print(int(num[n]))
sequence[n+1]=n
i=n+1
answer=[]
while i >=2:
    answer.append(int(sequence[i]))
    i = int(sequence[i])
for i in range(len(answer)-1,-1,-1):
    print(answer[i], end=' ')
