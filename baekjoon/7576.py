# 토마토

import sys
from collections import deque
import copy

def bfs(x, y, cnt):
    maxi = -5
    visited = copy.deepcopy(tomato)
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    que = deque([(x,y)])

    while que:
        now_x, now_y = que.popleft()
        visited[now_x][now_y] = 1
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]

            if (0<=next_x<N) and (0<=next_y<M) and (visited[next_x][next_y] == 0):
                visited[next_x][next_y] = 1
                if day[next_x][next_y] == -5: day[next_x][next_y] = day[now_x][now_y]+1
                else: day[next_x][next_y] = min(day[next_x][next_y], day[now_x][now_y]+1)
                cnt -= 1
                maxi = max(maxi, day[next_x][next_y])
                que.append((next_x, next_y))
    return cnt, maxi


M,N = map(int, sys.stdin.readline().split())
tomato = []
for _ in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    tomato.append(t)

ripe = [] # 익은 토마토의 위치
day = [[-5]*M for _ in range(N)] # 익는데 걸리는 날짜
no_ripe = N*M

for row in range(N):
    for col in range(M):
        if tomato[row][col] == 1:
            ripe.append((row,col))
            day[row][col] = 0
            no_ripe -=1
        elif tomato[row][col] == -1:
            day[row][col] = 0
            no_ripe -= 1

for r,c in ripe:
    no_ripe, top = bfs(r,c, no_ripe-1)

if no_ripe > 0: print(-1)
else: print(top)