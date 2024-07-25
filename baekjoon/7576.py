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

def bfs(queue):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while ripe:
        now_x, now_y = queue.popleft()
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]

            if (0<=next_x<N) and (0<=next_y<M) and (tomato[next_x][next_y] == 0):
                tomato[next_x][next_y] = tomato[now_x][now_y] + 1
                queue.append((next_x, next_y))
    return tomato


M,N = map(int, sys.stdin.readline().split())
tomato = []
for _ in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    tomato.append(t)

ripe = deque()

for row in range(N):
    for col in range(M):
        if tomato[row][col] == 1:
            ripe.append((row,col))

bfs(ripe)
day = 0
for r in tomato:
    for c in range(M):
        if r[c] == 0:
            print(-1)
            exit()
    day = max(day, max(r))

print(day -1)