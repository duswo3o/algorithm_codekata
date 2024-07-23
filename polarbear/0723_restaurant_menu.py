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




####################################################################
####################################################################
####################################################################

# # 큐 구현해서 풀기 -> 42% 시간초과
#
# # 노드생성
# class Node:
#     def __init__(self, item, next):
#         self.item = item
#         self.next = next
#
#
# # 큐 구형
# class Queue:
#     def __init__(self):
#         self.front = None # 가장 앞에 있는 값 = 가장 먼저 들어온 값
#         self.size = 0
#
#
#     # 삽입
#     def push(self, value):
#         self.size += 1
#
#         if self.front is None: # 이전에 들어온 값이 없는 경우
#             self.front = Node(value, None) # 첫 번째 값 업데이트
#
#         else: # 이전에 값이 있는 경우
#             node = self.front # 가장 먼저 들어온 값부터 시작
#             while node.next is not None: # 가장 마지막 값까지 이동
#                 node = node.next
#
#             node.next = Node(value, None) # 가잘 마지막 노드의 다음 노드에 추가
#
#     # 삭제
#     def pop(self):
#         node = self.front # 가장 먼저 들어온 값 먼저 삭제
#
#         if node is None: # 노드가 비어있는 경우
#             return None
#
#         self.front = self.front.next # 가장 먼저 들어온 값을 다음 값으로 업데이트
#         self.size -= 1
#
#         return node.item
#
#
# import sys
#
# A = [] # 본인이 좋아하는 메뉴를 먹은 학생
# B = [] # 본인이 좋아하지 않은 메뉴를 먹은 학생
# C = [] # 식당에 도착했으나 식사를 하지 못한 학생
#
# N = int(input()) # 정보의 수
# waiting = Queue()
# # print(waiting)
#
# for _ in range(N):
#     info = sys.stdin.readline().strip().split()
#
#     if len(info) == 3: # 유형 1의 정보 : 대기 줄에 학생이 추가되는 경우
#         waiting.push((info[1], info[2])) # 대기줄에 (학생번호, 좋아하는 메뉴 번호) 저장
#     else: # 유형 2의 정보 : 대기 줄의 학생이 식사를 시작하는 경우
#         meal_number, meal_type = waiting.pop() # 대기 줄의 가장 앞에 있는 학생의 정보
#         if meal_type == info[1]: # 좋아하는 메뉴 번호와 준비된 메뉴가 같다면
#             A.append(int(meal_number)) # 좋아하는 메뉴를 먹은 리스트에 추가
#         else: # 좋아하는 메뉴 번호와 다르다면
#             B.append(int(meal_number)) # 좋아하지 않은 메뉴를 먹은 리스트에 추가
#
#
# while waiting.front:
#     C.append(int(waiting.pop()[0]))
#
# # 오름차순이 될 수 있도록 정렬 -> sort를 따로 빼주면 시간초과가 발생하지 않음
# A.sort()
# B.sort()
# C.sort()
#
# # 빈 칸을 사이에 두고 출력
# print(" ".join(list(map(str, A))) if len(A)!=0 else None)
# print(" ".join(list(map(str, B))) if len(B)!=0 else None)
# print(" ".join(list(map(str, C))) if len(C)!=0 else None)

