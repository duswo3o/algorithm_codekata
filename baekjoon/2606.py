# 바이러스

import sys
from collections import deque

def dfs(tree, visited, stack):
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(tree[now])
    return visited


def bfs(tree, visited, que):
    while que:
        now = que.popleft()
        if now not in visited:
            visited.append(now)
            que.extend(tree[now])
    return visited

com = int(input())

network = {i+1:set() for i in range(com)}

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())

    network[a].add(b)
    network[b].add(a)

virus = []
will_visit = [1]

print(dfs(network, virus, will_visit))
print(len(dfs(network, virus, will_visit))-1)
print(bfs(network, virus, deque(will_visit)))
print(len(bfs(network, virus, deque(will_visit)))-1)