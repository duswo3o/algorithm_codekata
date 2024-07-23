# 미로 탐색

import sys
from collections import deque

# 넓이 우선 탐색
def bfs(maze, que, ed):
    # 상하좌우 이동
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while que:
        now = que.popleft()
        now_x, now_y = now[0], now[1] # 현재좌표

        if now == ed: # 현재 좌표가 마지막 좌표면
            break # 반복문 탈출

        # 현재 좌표에서 상하좌우로 이동하면서 갈 수 있는 좌표를 방문할 좌표 큐에 넣기
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y+dy[i]
            if 0<=next_x<=ed[0] and 0<=next_y<=ed[1] and maze[next_x][next_y] == 1:
                maze[next_x][next_y] = maze[now_x][now_y] + 1 # 좌표값 업데이트
                que.append((next_x, next_y)) # 다음에 갈 좌표에 추가

    return maze[ed[0]][ed[1]] # 마지막 좌표값 반환

N, M = map(int, input().split())

maze = []
for _ in range(N):
    l = sys.stdin.readline().strip()
    maze.append([int(i) for i in l])

que = deque([(0,0)]) # 방문할 좌표
print(bfs(maze, que, (N-1, M-1)))