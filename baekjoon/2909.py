import sys

C, K = map(int, sys.stdin.readline().split())
print(round(int(C+10**(K-1)), -K)) # 5는 내림으로 계산됨 따라서 추가적인 연산 필요