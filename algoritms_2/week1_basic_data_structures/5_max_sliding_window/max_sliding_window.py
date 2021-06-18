# python3

class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def push(self, elem):
        if self.stack:
            self.stack.append((elem, max(elem, self.stack[-1][1])))
        else:
            self.stack.append((elem, elem))

    def pop(self):
        return self.stack.pop()[0]

    def get_max(self):
        if not self.stack:
            return -1
        return self.stack[-1][1]

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, elem):
        self.s1.push(elem)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def get_max(self):
        return max(self.s1.get_max(), self.s2.get_max())

def max_sliding_window_naive(sequence, m):
    maximums = []
    queue = Queue()
    for i in range(m):
        queue.push(sequence[i])
    maximums.append(queue.get_max())
    for i in range(m, len(sequence)):
        queue.pop()
        queue.push(sequence[i])
        maximums.append(queue.get_max())

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

