# 트리의 부모 찾기


import sys
from collections import deque

T = int(input())

my_tree = {}
for i in range(T):
    my_tree[i+1] = []
my_tree[1].append(None)
waiting = deque([])

for _ in range(T-1):
    a, b = map(int, sys.stdin.readline().strip().split())

    if my_tree[a]:
        my_tree[b].append(a)
    elif my_tree[b]:
        my_tree[a].append(b)
    else:
        waiting.append((a,b))

while waiting:
    a, b = waiting.popleft()

    if my_tree[a]:
        my_tree[b].append(a)
    elif my_tree[b]:
        my_tree[a].append(b)
    else:
        waiting.append((a,b))

for i in range(2,T+1):
    print(my_tree[i][0])

