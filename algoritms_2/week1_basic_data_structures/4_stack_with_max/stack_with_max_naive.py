#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        return self.__stack.pop()

    def Get(self):
        if (self.isEmpty()):
            return -1
        return self.__stack[-1]

    def isEmpty(self):
        if (len(self.__stack)==0):
            return True
        else:
            return False

if __name__ == '__main__':
    ans=[]
    stack = StackWithMax()
    stack_max = StackWithMax()
    num_queries = int(input())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
            if (int(query[1]) >= stack_max.Get()):
                stack_max.Push(int(query[1]))

        if query[0] == "pop":
            if (stack_max.Get() == stack.Pop()):
                stack_max.Pop()

        if query[0] == "max":
           ans.append(stack_max.Get())

for i in ans:
    print(i)
