from collections import deque
import sys

queue = deque()

N = int(sys.stdin.readline())
for _ in range(N):
    _input = sys.stdin.readline().strip().split()
    order = _input[0]
    length = len(queue)

    if order == "push":
        queue.append(_input.pop())
    elif order == "pop":
        if length:
            print(queue.popleft())
        else:
            print(-1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if length:
            print(queue[0])
        else:
            print(-1)
    elif order == "back":
        if length:
            print(queue[-1])
        else:
            print(-1)