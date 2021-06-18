import numpy as np

def hash_func(x):
    return ((a*x + b) % p) % m

def add(number, name):
    index = hash_func(number)
    for i in phone_book[index]:
        if (i[0] == number):
            i[1] = name
            return
    phone_book[index].append([number, name])

def find(number):
    index = hash_func(number)

    for i in phone_book[index]:
        if (i[0] == number):
            print(i[1])
            return
    print('not found')

def delete(number):
    index = hash_func(number)

    for i in range(len(phone_book[index])):
        if (phone_book[index][i][0] == number):
            phone_book[index].pop(i)
            return


phone_book = np.arange(1) ** 3

p = 10000019
m = int(input())
a = np.random.randint(1, p - 1)
b = np.random.randint(0, p - 1)
phone_book = x = [[] for i in range(m)]


for i in range(m):
    s = input().split()
    if(s[0] == 'add'):
        add(int(s[1]), s[2])
    elif (s[0] == 'find'):
        find(int(s[1]))
    else:
        delete(int(s[1]))

