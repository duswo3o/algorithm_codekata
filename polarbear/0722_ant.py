# 백준 11880 개미

import sys
T = int(input())
for _ in range(T):
    line = list(map(int, sys.stdin.readline().split())) # 가로, 세로, 높이
    line.sort() # 오름차순 정렬
    c = line.pop() # 가장 긴 길이
    print(sum(line)**2 + c**2) # 짧은 길이 2개의 합 ** 2 + 긴 길이 하나의 제곱