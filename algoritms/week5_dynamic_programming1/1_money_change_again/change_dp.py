# Uses python3
import sys
import numpy as np

def get_change(money, coins):
    MinNumCoins = np.zeros(money+1)
    MinNumCoins[0]=0
    for m in range(1, money+1):
        MinNumCoins[m] = 1e4
        for i in coins:
            if ( m >= i):
                NumCoins=MinNumCoins[m-i]+1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m]=NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    coins=[1,3,4]
    n = int(input())
    print(int(get_change(n, coins)))
