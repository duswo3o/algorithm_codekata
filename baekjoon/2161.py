# 카드1

from collections import deque

def card(n):
    c = deque([i+1 for i in range(n)])
    while len(c)!=1:
        print(c.popleft(), end = " ")
        c.append(c.popleft())

    return print(c.pop())

# card(int(input()))

############################################################

# 큐 구현해서 플어보기

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def push(self, val):
        if self.front is None:
            self.front = Node(val, None)

        else:
            q = self.front
            while q.next:
                q = q.next
            q.next = Node(val, None)

    def pop(self):
        if self.front:
            q = self.front
            self.front = self.front.next

            return q.value


c = int(input())
que = Queue()
for i in range(c):
    que.push(i+1)

while que.front.value != None:
    print(que.pop())
    que.push(que.pop())
