# 수 정렬하기

import sys

N = int(sys.stdin.readline())

num =[0]*100001
for _ in range(N):
    n = int(sys.stdin.readline())
    num[n] += 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)


########################################################################################
########################################################################################

