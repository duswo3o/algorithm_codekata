
from collections import deque, defaultdict
import sys

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack += sorted(graph[now], reverse = True)
    return visited


def bfs(graph, start):
    visited = []
    que = deque([start])

    while que:
        now = que.popleft()
        if now not in visited:
            visited.append(now)
            que += sorted(graph[now])
    return visited


N,M,V = map(int, sys.stdin.readline().split())
g = defaultdict(list)
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())

    g[node1].append(node2)
    g[node2].append(node1)


dfs = map(str, dfs(g, V))
bfs = map(str, bfs(g, V))

print(" ".join(dfs))
print(" ".join(bfs))