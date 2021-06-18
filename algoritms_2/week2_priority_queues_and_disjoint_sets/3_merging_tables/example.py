import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def Union(i, j):
    i_id = Find(i)
    j_id = Find(j)
    if i_id == j_id:
        return parent[i_id][1]
    parent[j_id][0] = i_id
    parent[i_id][1] = parent[i_id][1]+parent[j_id][1]
    parent[j_id][1] = 0
    return parent[i_id][1]

def MakeSet(i):
    parent.append([i, counts[i]])

def Find(i):
    if i != parent[i][0]:
        parent[i][0] = Find(parent[i][0])
    return parent[i][0]

def main():
    n_tables, n_queries = map(int, input().split())
    global parent, counts
    parent =[]
    counts = list(map(int, input().split()))
    Maxi = max(counts)
    for i in range(n_tables):
        MakeSet(i)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        Maxi = max(Maxi, Union(dst-1,src-1))
        print(Maxi)
threading.Thread(target=main).start()
