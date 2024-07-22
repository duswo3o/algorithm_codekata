# DFS와 BFS

import sys
from collections import deque

def dfs(tree, stack, visited):
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(sorted(tree[now], reverse=True))
    return visited

def bfs(tree, queue, visited):
    while queue:
        now = queue.popleft()
        if now not in visited:
            visited.append(now)
            queue.extend(sorted(tree[now]))
    return visited

N, M ,V = map(int, input().split()) # 정점, 간선, 시작할 정점
graph = {i+1:[] for i in range(N)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

stack = [V]
que = deque([V])
visited_dfs = []
visited_bfs = []

print(" ".join(list(map(str, dfs(graph, stack, visited_dfs)))))
print(" ".join(list(map(str, bfs(graph, que, visited_bfs)))))