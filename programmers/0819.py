# 프로세스

from collections import deque

# def solution(priorities, location):
#     answer = 0
#
#     # 실행대기 큐 (인덱스, 우선순위)
#     que = deque()
#     for idx, priority in enumerate(priorities):
#         que.append((idx, priority))
#
#     priorities.sort() # 우선순위 정렬
#     now_p = priorities.pop() # 현재 가장 높은 우선순위
#
#     while que:
#         task = que.popleft() # 현재 프로세스
#         # 프로세스의 우선순위가 최우선 순위이고 찾는 위치의 프로세스라면
#         if task[1] == now_p and task[0] == location:
#             answer += 1 # 몇 번째 작업인지 업데이트
#             return answer # 정답 리턴
#
#         # 우선순위가 최우선 순위이지만 찾는 작업이 아니라면
#         if task[1] >= now_p and task[0] != location:
#             answer += 1 # 몇 번째 작업인지 업데이트
#             now_p = priorities.pop() # 우선순위 업데이트
#
#         # 우선 순위보다 낮은 작업이라면
#         if task[1] < now_p:
#             que.append(task) # 작업 큐의 맨 뒤로 보내기



##################################################################
##################################################################
##################################################################



# 큐 구현해서 풀기

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.end = None

    def push(self, value):
        if self.front is None:
            node = Node(value, None)
            self.front = node
            self.end = node

        else:
            node = Node(value,None)
            self.end.next = node
            self.end = node

    def pop(self):
        if self.front is None:
            return None

        else:
            node = self.front
            self.front = self.front.next

        return node.item


def solution(priorities, location):
    answer = 0
    que = Queue()

    for idx, priority in enumerate(priorities):
        que.push((idx, priority))

    priorities.sort()
    now_p = priorities.pop()

    while priorities:
        task = que.pop()

        if task[0] == location and task[1] == now_p:
            answer += 1
            return answer
        if task[0] != location and task[1] >= now_p:
            answer += 1
            now_p = priorities.pop()
        if task[1] < now_p:
            que.push(task)
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))