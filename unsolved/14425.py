# 문자열 집합

import sys

# 문자열의 개수
N, M = map(int, sys.stdin.readline().split())

# 집합 S에 포함된 문자열
S = set()
for _ in range(N):
    s = sys.stdin.readline().strip()
    S.add(s)

cnt = 0 # 집한에 포함된 문자열의 개수
# 검사해야하는 문자열
for _ in range(M):
    e = sys.stdin.readline().strip()
    # 검사해야하는 문자열에는 중복이 있을 수 있어서 하나씩 값을 비교해주어야함
    if e in S:
        cnt += 1

print(cnt)