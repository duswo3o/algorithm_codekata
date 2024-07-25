# # 토마토
#
# import sys
# from collections import deque
# import copy
#
# def bfs(queue):
#     # maxi = -5
#     # visited = copy.deepcopy(tomato)
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     # que = deque([(x,y)])
#
#     while ripe:
#         now_x, now_y = queue.popleft()
#         # visited[now_x][now_y] = 1
#         for i in range(4):
#             next_x, next_y = now_x + dx[i], now_y + dy[i]
#
#             if (0<=next_x<N) and (0<=next_y<M) and (day[next_x][next_y] == -5):
#                 # visited[next_x][next_y] = 1
#                 # if day[next_x][next_y] == -5: day[next_x][next_y] = day[now_x][now_y]+1
#                 # else: day[next_x][next_y] = min(day[next_x][next_y], day[now_x][now_y]+1)
#                 # cnt -= 1
#                 # maxi = max(maxi, day[next_x][next_y])
#                 day[next_x][next_y] = day[now_x][now_y] + 1
#                 queue.append((next_x, next_y))
#     return day
#
#
# M,N = map(int, sys.stdin.readline().split())
# tomato = []
# for _ in range(N):
#     t = list(map(int, sys.stdin.readline().split()))
#     tomato.append(t)
#
# ripe = deque([]) # 익은 토마토의 위치
# day = [[-5]*M for _ in range(N)] # 익는데 걸리는 날짜
# # no_ripe = N*M
#
# for row in range(N):
#     for col in range(M):
#         if tomato[row][col] == 1:
#             ripe.append((row,col))
#             day[row][col] = 1
#             # no_ripe -=1
#         elif tomato[row][col] == -1:
#             day[row][col] = -1
#         #     no_ripe -= 1
#
# # print("안 익은 토마토",no_ripe)
# # no_ripes = []
#     # temp = copy.deepcopy(no_ripe)
#     # temp, top = bfs(r,c, temp)
#     # no_ripes.append(temp)
#
# # print("안 익은 토마토",no_ripes)
#
# bfs(ripe)
# # print(day)
#
# if min(min(day)) == -5: print(-1)
# else: print(max(max(day))-1) # max(max(day))


import sys
from collections import deque


# 넓이 우선 탐색 : 주변의 모든 토마토를 익게 만들어서 넓이 우선 탐색 이용!
def bfs(queue):
    # 상하좌우 이동
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while ripe:
        now_x, now_y = queue.popleft() # 현재 좌표
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i] # 다음 방문할 좌표
            # 좌표가 범위 내에 존재하고 다음 갈 좌표가 안익은 토마토라면
            if (0<=next_x<N) and (0<=next_y<M) and (tomato[next_x][next_y] == 0):
                tomato[next_x][next_y] = tomato[now_x][now_y] + 1 # 익는데 걸리는 날짜 값으로 업데이트
                queue.append((next_x, next_y)) # 방문할 좌표에 추가
    return tomato


M,N = map(int, sys.stdin.readline().split())
tomato = [] # 토마토 밭
for _ in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    tomato.append(t)

ripe = deque() # 익은 토마토의 위치
# 익은 토마토 찾기
for row in range(N):
    for col in range(M):
        if tomato[row][col] == 1:
            ripe.append((row,col))

bfs(ripe) # 토마토 익는중
day = 0 # 토마토가 익는데 걸리는 날
for r in tomato:
    for c in range(M):
        if r[c] == 0: # 안익은 토마토가 있으면
            print(-1) # -1 출력하고
            exit() # 종료 -> 이후 코드는 무시
    day = max(day, max(r)) # 익는데 가장 오래 걸리는 날짜

print(day -1) # 익어있는 토마토부터 시작했으므로 -1을 해줌