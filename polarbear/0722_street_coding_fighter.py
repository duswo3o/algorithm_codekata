# 백준 23348 스트릿 코딩 파이터

import sys

one_hand, no_look, phone = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
top_score = 0
for _ in range(N):
    team_score = 0
    for i in range(3):
        a, b, c = map(int, sys.stdin.readline().split())
        team_score += a*one_hand + b*no_look + c*phone
    top_score = team_score if team_score > top_score else top_score

print(top_score)