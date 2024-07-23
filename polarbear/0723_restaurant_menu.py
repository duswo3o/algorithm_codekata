# 식당 메뉴

import sys
from collections import deque

A = [] # 본인이 좋아하는 메뉴를 먹은 학생
B = [] # 본인이 좋아하지 않은 메뉴를 먹은 학생
C = [] # 식당에 도착했으나 식사를 하지 못한 학생

N = int(input())
waiting = deque([])

for _ in range(N):
    info = sys.stdin.readline().strip().split()

    if len(info) == 3:
        waiting.append((info[1], info[2]))
    else:
        meal_number, meal_type = waiting.popleft()
        if meal_type == info[1]:
            A.append(int(meal_number))
        else:
            B.append(int(meal_number))

if len(waiting) != 0:
    C = [int(waiting[w][0]) for w in range(len(waiting))]

print(" ".join(list(map(str, sorted(A)))) if len(A)!=0 else None)
print(" ".join(list(map(str, sorted(B)))) if len(B)!=0 else None)
print(" ".join(list(map(str, sorted(C)))) if len(C)!=0 else None)