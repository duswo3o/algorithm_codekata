# 섬의 개수

import sys

def dfs(row, col):
    stack = [(row, col)]
    dr = [1,0,-1,0,1,-1, 1, -1]
    dc = [0,1,0,-1,1,-1, -1, 1]
    while stack:
        now_row, now_col = stack.pop()
        island[now_row][now_col] = 0

        for i in range(8):
            next_row, next_col = now_row+dr[i], now_col+dc[i]

            if (0<=next_row<M) and (0<=next_col<N) and (island[next_row][next_col] == 1):
                stack.append((next_row, next_col))
                island[next_row][next_col] = 0


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    island = []
    for _ in range(M):
        island.append(list(map(int, sys.stdin.readline().split())))

    cnt_island = 0
    for r in range(M):
        for c in range(N):
            if island[r][c] == 1:
                cnt_island += 1
                dfs(r,c)

    print(cnt_island)