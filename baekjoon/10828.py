# 스택


def my_stack(command, s):
    if len(command) == 2:
        s.append(int(command.pop()))

    else:
        c = command.pop()
        if c == "pop":
            return print(s.pop() if len(s) != 0 else -1)

        elif c == "size":
            return print(len(s))

        elif c == "empty":
            return print(1 if len(s) == 0 else 0)

        elif c == "top":
            return print(s[-1] if len(s) != 0 else -1)

# python3로 제출하면 런타임 에러 pypy3로 제출하면 통과
s = []
# for i in range(int(input())):
#     my_stack(input().split(" "), s)


##########################################################################################


# 클래스로 스택 구현해서 풀어보기

import sys

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.t = None
        self.length = 0

    def empty(self):
        return 1 if self.t is None else 0

    def push(self, val):
        self.t = Node(val, self.t)
        self.length +=1

    def pop(self):
        if self.t is None:
            return -1

        node = self.t
        self.length -= 1
        self.t = self.t.next

        return node.value

    def size(self):
        return self.length

    def top(self):
        if self.t is None:
            return -1

        return self.t.value


s = Stack()
for i in range(int(input())):
    m = sys.stdin.readline().split() # 여기를 input으로 받아서 런타임 에러가 나는 것!

    if m[0] == "push":
        s.push(int(m[1]))
    elif m[0] == "pop":
        print(s.pop())
    elif m[0] == "size":
        print(s.size())
    elif m[0] == 'empty':
        print(s.empty())
    elif m[0] == 'top':
        print(s.top())

