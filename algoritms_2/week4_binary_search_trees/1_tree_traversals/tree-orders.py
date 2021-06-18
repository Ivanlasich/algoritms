# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
    return self.result

  def inOrder_rec(self, x):
      if (self.left[x] == -1):
        print(self.key[x], end=' ')
        if (self.right[x] != -1):
            self.inOrder_rec(self.right[x])
      else:
        self.inOrder_rec(self.left[x])
        print(self.key[x], end=' ')
        if (self.right[x] != -1):
            self.inOrder_rec(self.right[x])

      return 0


  def preOrder(self, x):
    print(self.key[x], end=' ')
    if(self.left[x]!= -1):
        self.preOrder(self.left[x])
    if (self.right[x] != -1):
        self.preOrder(self.right[x])
      # Finish the implementation
    # You may need to add a new recursive method to do that
                


  def postOrder(self, x):
    if(x!=-1):
        self.postOrder(self.left[x])
        self.postOrder(self.right[x])
        print(self.key[x], end=' ')


def main():

    tree = TreeOrders()

    tree.read()
    tree.inOrder_rec(0)
    print()
    tree.preOrder(0)
    print()
    tree.postOrder(0)



threading.Thread(target=main).start()
