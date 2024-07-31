# 프로세스

from collections import deque

def solution(priorities, location):
    answer = 0

    # 실행대기 큐 (인덱스, 우선순위)
    que = deque()
    for idx, priority in enumerate(priorities):
        que.append((idx, priority))

    priorities.sort() # 우선순위 정렬
    now_p = priorities.pop() # 현재 가장 높은 우선순위

    while que:
        task = que.popleft() # 현재 프로세스
        # 프로세스의 우선순위가 최우선 순위이고 찾는 위치의 프로세스라면
        if task[1] == now_p and task[0] == location:
            answer += 1 # 몇 번째 작업인지 업데이트
            return answer # 정답 리턴
        # 우선순위가 최우선 순위이지만 찾는 작업이 아니라면
        if task[1] >= now_p and task[0] != location:
            answer += 1 # 몇 번째 작업인지 업데이트
            now_p = priorities.pop() # 우선순위 업데이트
        # 우선 순위보다 낮은 작업이라면
        if task[1] < now_p:
            que.append(task) # 작업 큐의 맨 뒤로 보내기

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))