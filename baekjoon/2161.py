# 카드1

from collections import deque

def card(n):
    c = deque([i+1 for i in range(n)])
    while len(c)!=1:
        print(c.popleft(), end = " ")
        c.append(c.popleft())

    return print(c.pop())

card(int(input()))