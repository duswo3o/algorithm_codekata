# 유기농 배추

import sys
from collections import deque

# 넓이 우선 탐색
def BFS(field, que):
    while que: # 큐에 남은 좌표가 없을 때까지
        now = que.popleft() # 먼저 들어온 것 부터
        now_y, now_x = now[0], now[1] # y좌표, x좌표
        field[now_y][now_x] = 0 # 현재 좌표를 0으로 바꾸기
        for d in range(4): # 상하좌우 이동
            next_y, next_x = now_y + dy[d], now_x + dx[d]
            # 좌표가 범위 내에 있고, 좌표의 값이 1인 경우
            if (0 <= next_y < len(field)) and (0 <= next_x < len(field[0])) and (field[next_y][next_x]==1):
                que.append((next_y, next_x)) # 큐에 추가
    return field

# 깊이 우선 탐색
def DFS(field, stack):
    while stack: # 스택에 좌표가 남아 있는 동안
        now = stack.pop() # 가장 마지막으로 추가된 것 부터
        now_y, now_x = now[0], now[1] # 좌표
        field[now_y][now_x] = 0 # 현재 위치를 0으로 교체
        for d in range(4): # 현재 위치에서 상하좌우로 이동
            next_y, next_x = now_y + dy[d], now_x + dx[d]
            # 좌표가 범위 내에 있고, 좌표의 값이 1일때
            if (0 <= next_y < len(field)) and (0 <= next_x < len(field[0])) and (field[next_y][next_x]==1):
                stack.append((next_y, next_x)) # 스택에 추가
    return field

T = int(sys.stdin.readline()) # 테스트케이스 수

# 이동할 좌표
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(T):
    # 배추밭의 가로 길이, 배추밭의 세로 길이, 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, sys.stdin.readline().split())
    # print("M :",M, "M :", N, "K :",K)

    cabbage_field = [[0] * M for n in range(N)] # 배추밭 생성

    # 배추밭에서 배추가 있는 위치 표시
    for i in range(K):
        y, x = map(int, sys.stdin.readline().split())
        cabbage_field[x][y] = 1

    worm = 0 # 배추흰지렁이 개수
    # 밭의 모든 좌표를 돌아다니면서
    for n in range(N):
        for m in range(M):
            # 좌표값이 0일 때
            if cabbage_field[n][m] == 0:
                continue
            # 좌표값이 0이 아닐 때 (1일 때)
            else:
                worm += 1 # 지렁이 추가

                # 넓이우선탐색 이용 : 제출시 시간초과
                que = deque() # 큐 생성
                que.append((n, m)) # 큐에 시작 좌표 추가
                BFS(cabbage_field, que) # 붙어있는 모든 배추를 방문

                # # 깊이우선탐색 이용
                # stack = [] # 스택 생성
                # stack.append((n,m)) # 스택에 시작 좌표 추가
                # DFS(cabbage_field, stack) # 붙어있는 모든 배추를 방문
    print(worm)