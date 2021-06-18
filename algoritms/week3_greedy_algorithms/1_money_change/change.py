# Uses python3
import sys

def get_change(m):
    ans = 0
    n = int(m /10);
    if(n != 0):
        ans=ans+n
    m = m - n*10

    n = int(m / 5);
    if (n != 0):
        ans = ans + n
    m = m - n * 5

    n = int(m);

    if (n != 0):
        ans = ans + n
    m = m - n * 1

    return ans

if __name__ == '__main__':
    m = int(input())

    print((get_change(m)))
