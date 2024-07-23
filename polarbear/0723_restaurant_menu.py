# 식당 메뉴

import sys
from collections import deque

A = [] # 본인이 좋아하는 메뉴를 먹은 학생
B = [] # 본인이 좋아하지 않은 메뉴를 먹은 학생
C = [] # 식당에 도착했으나 식사를 하지 못한 학생

N = int(input()) # 정보의 수
waiting = deque([]) # 대기 줄

for _ in range(N):
    info = sys.stdin.readline().strip().split()

    if len(info) == 3: # 유형 1의 정보 : 대기 줄에 학생이 추가되는 경우
        waiting.append((info[1], info[2])) # 대기줄에 (학생번호, 좋아하는 메뉴 번호) 저장
    else: # 유형 2의 정보 : 대기 줄의 학생이 식사를 시작하는 경우
        meal_number, meal_type = waiting.popleft() # 대기 줄의 가장 앞에 있는 학생의 정보
        if meal_type == info[1]: # 좋아하는 메뉴 번호와 준비된 메뉴가 같다면
            A.append(int(meal_number)) # 좋아하는 메뉴를 먹은 리스트에 추가
        else: # 좋아하는 메뉴 번호와 다르다면
            B.append(int(meal_number)) # 좋아하지 않은 메뉴를 먹은 리스트에 추가

if len(waiting) != 0:
    C = [int(waiting[w][0]) for w in range(len(waiting))]

# 오름차순이 될 수 있도록 정렬 -> sort를 따로 빼주면 시간초과가 발생하지 않음
A.sort()
B.sort()
C.sort()

# 빈 칸을 사이에 두고 출력
print(" ".join(list(map(str, A))) if len(A)!=0 else None)
print(" ".join(list(map(str, B))) if len(B)!=0 else None)
print(" ".join(list(map(str, C))) if len(C)!=0 else None)