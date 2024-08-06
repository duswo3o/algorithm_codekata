# 최단경로

import sys


# 방문하지 않은 노드 중에 최단 거리가 가장 짧은 노드를 찾기
def get_smallest_node():
    smallest = 1e9
    idx = K

    for i in range(1,V+1):
        if visited[i] == False and dist[i] < smallest:
            smallest = visited[i]
            idx = i

    return idx


def dijkstra(start):
    visited[start] = True # 시작 노드 방문 처리
    dist[start] = 0 # 시작 노드의 최단거리

    # 인접 노드 거리 구하기
    for arrive, weight in graph[start]:
        dist[arrive] = weight # 시작 노드와 이어진 노드의 거리

    for i in range(1,V+1):
        now = get_smallest_node()
        visited[now] = True
        for arrive, weight in graph[now]:
            dist[arrive] = min(dist[now]+weight, dist[arrive])


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = {i+1: [] for i in range(V)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

visited = [False] * (V+1)
dist = [1e9] * (V+1)

dijkstra(K)

for i in range(1, V+1):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])

