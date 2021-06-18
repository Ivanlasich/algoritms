#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(node, min, msx):
  if not node in tree: return True
  else:
    if tree[node][0] < min or tree[node][0] > msx: return False
    return IsBinarySearchTree(tree[node][1], min, tree[node][0] - 1) and IsBinarySearchTree(tree[node][2], tree[node][0], msx)
  # Implement correct algorithm here


def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree = {}
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, -2147483648, 2147483647):
    print("CORRECT")
  else:
    print("INCORRECT")


threading.Thread(target=main).start()
