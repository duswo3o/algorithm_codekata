# 육각타일미로 탈출기

import sys
from collections import deque
# import pprint

def bfs(r,c):
    que = deque([(r,c)])

    dr = [-1, -1, 0, 0, 1, 1]
    # 열 번호가 홀수일 때 이동할 수 있는 방향
    odd_dc = [0, 1, -1, 1, 0, 1]
    # 열 번호가 짝수일 때 이동할 수 있는 방향
    even_dc = [-1, 0, -1, 1, -1, 0]

    while que:
        now_r, now_c = que.popleft()
        # maze[now_r][now_c] = 0
        for i in range(6):
            if now_r%2 == 0:
                next_c, next_r = now_c + even_dc[i], now_r + dr[i]
            else:
                next_c, next_r = now_c + odd_dc[i], now_r + dr[i]

            if (0<=next_r<N) and (0<=next_c<M) and (maze[next_r][next_c] == 0):
                maze[next_r][next_c] += maze[now_r][now_c]+1
                que.append((next_r, next_c))
        # pprint.pprint(maze)
    return


N,M,K = map(int, sys.stdin.readline().split())
maze = [[0]*M for i in range(N)]

for _ in range(K):
    row, col = map(int, sys.stdin.readline().split())
    maze[row][col] = -1

bfs(0,0)
if maze[N-1][M-1] > 1:
    print(maze[N-1][M-1])
else:
    print(-1)