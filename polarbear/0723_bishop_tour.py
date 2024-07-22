# 비숍 투어

# from collections import deque
#
N,M = map(int,input().split()) # 체스판의 크기
st_x, st_y = map(int,input().split()) # 출발 좌표
ed_x, ed_y = map(int,input().split()) # 도착 좌표
#
# chess = [[0]*M for _ in range(N)] # 체스판 생성
# chess[ed_x-1][ed_y-1] = 1 # 도착 위치
#
# # 대각선으로 이동
# dx = [1,1,-1,-1]
# dy = [1,-1,1,-1]
#
# stack = deque([(st_x-1, st_y-1)])
#
# possible = "NO"
# while stack:
#     x, y = stack.popleft()
#     if chess[x][y] == 1:
#         possible = "YES"
#         break
#     chess[x][y] = 2
#     for i in range(4):
#         next_x, next_y = x+dx[i], y+dy[i]
#         if 0<=next_x<N and 0<=next_y<M and chess[next_x][next_y]!=2:
#             stack.append((next_x, next_y))
# print(possible)


###########################################################################
###########################################################################
###########################################################################

# 두 좌표의 차이
dx, dy = abs(ed_x - st_x), abs(ed_y - st_y)

if N==1 or M==1: # 한 줄로 이루어진 체스판
    if dx == dy == 0: # 둘의 좌표가 같아야만 됨
        print("YES")
    else:
        print("NO")
else: # 2X2이상의 체스판
    if (dx%2 == 0 and dy%2 == 0): # 시작점과 끝점의 차가 모두 짝수인 경우
        print("YES")
    elif (dx%2 != 0 and dy%2 != 0): # 시작점과 끝점의 차가 모두 홀수인 경우
        print("YES")
    else:
        print("NO")