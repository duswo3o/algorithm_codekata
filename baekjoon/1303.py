# 전쟁 - 전투

import sys

# 깊이 우선 탐색
def dfs(stack, field, m):
    # 상하좌우 탐색
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    s = 0 # 이어진 길이
    while stack:
        # 현재 위치
        now_r, now_c = stack.pop()
        if field[now_r][now_c] == m: # 현재 위치가 같은 팀일 때
            s += 1 # 이어짐 추가
        field[now_r][now_c] = "V" # 방문 표시

        # 탐색할 곳
        for i in range(4):
            next_r, next_c = now_r +dr[i], now_c + dc[i]
            # 탐색할 위치가 범위 내에 존재하고 같은 편이라면
            if 0<=next_r<M and 0<=next_c<N and field[next_r][next_c] == m:
                stack.append((next_r, next_c)) # 스택에 추가
    return s # 이어진 길이 반환

# 전쟁터의 가로, 세로
N, M = map(int, sys.stdin.readline().split())
battle =[] # 전쟁터
for _ in range(M):
    b = sys.stdin.readline().strip()
    b = [i for i in b]
    battle.append(b)

white_score = 0 # 우리팀 점수
blue_score = 0 # 적국의 점수

# 전쟁터의 모든 곳 방문
for row in range(M):
    for col in range(N):
        st = battle[row][col]
        stack = [(row,col)]
        if st in ["B","W"]:
            score = dfs(stack, battle, st)
            # 점수 계산
            if st == "W": white_score += score**2
            else: blue_score += score**2

print(white_score, blue_score)
