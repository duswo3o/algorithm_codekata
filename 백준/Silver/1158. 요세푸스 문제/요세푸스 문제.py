import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

josephus = deque(str(i+1) for i in range(N))
idx = 1
ans = []
while josephus:
    n = josephus.popleft()

    if idx<K:
        idx += 1
        josephus.append(n)

    elif idx == K:
        idx = 1
        ans.append(n)

print("<"+", ".join(ans)+">")