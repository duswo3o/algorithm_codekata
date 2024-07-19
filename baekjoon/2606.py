# 바이러스

import sys
from collections import deque

# 깊이 우선 탐색
def dfs(tree, visited, stack):
    while stack: # 더 이상 방문할 곳이 없을 때까지
        now = stack.pop() # 스택의 가장 마지막 요소를 꺼내서
        if now not in visited: # 꺼낸 곳이 방문하지 않은 곳이라면
            visited.append(now) # 방문한 곳에 추가
            stack.extend(tree[now]) # 연결된 노드들을 방문할 곳에 추가
    return visited

# 넓이 우선 탐색
def bfs(tree, visited, que):
    while que: # 더 이상 방문할 곳이 없을 때까지
        now = que.popleft() # 큐의 가장 첫 번째 요소를 꺼내서
        if now not in visited: # 꺼넨 곳이 방문하지 않은 곳이라면
            visited.append(now) # 방문한 곳에 추가
            que.extend(tree[now]) # 연결된 노드들을 방문할 곳에 추가
    return visited

com = int(input()) # 컴퓨터의 수
network = {i+1:set() for i in range(com)} # 네트워크 (트리)

for _ in range(int(input())): # 네트워크 상에 연결되어 있는 컴퓨터 쌍의 수
    a, b = map(int, sys.stdin.readline().split()) # 연결된 네트워크
    # 네트워크 딕셔너리에 추가
    network[a].add(b)
    network[b].add(a)

virus = [] # 바이러스가 퍼진 곳
will_visit = [1] # 1번에서 바이러스 감염 시작

print(dfs(network, virus, will_visit))
print(len(dfs(network, virus, will_visit))-1)
print(bfs(network, virus, deque(will_visit)))
print(len(bfs(network, virus, deque(will_visit)))-1)