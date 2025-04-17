class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        if self.empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        if self.empty():
            return -1

        first = self.head.value
        self.head = self.head.next
        self.size -= 1
        return first

    def empty(self):
        if self.head is None:
            return 1
        return 0

    def front(self):
        if self.empty():
            return -1
        return self.head.value

    def back(self):
        if self.empty():
            return -1
        return self.tail.value


import sys

N = int(sys.stdin.readline())

queue = Queue()
for _ in range(N):
    _input = sys.stdin.readline().strip().split()
    order = _input[0]
    if order == "push":
        queue.push(_input.pop())

    elif order == "pop":
        sys.stdout.write(str(queue.pop())+"\n")

    elif order == "empty":
        sys.stdout.write(str(queue.empty())+"\n")

    elif order == "size":
        sys.stdout.write(str(queue.size)+"\n")

    elif order == "front":
        sys.stdout.write(str(queue.front())+"\n")

    elif order == "back":
        sys.stdout.write(str(queue.back())+"\n")