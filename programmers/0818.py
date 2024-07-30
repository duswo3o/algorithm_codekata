# 기능 개발

from collections import deque
import math

def solution(progresses, speeds):
    answer = []

    # 완료까지 걸리는 작업일수
    take_times = deque()
    for i in range(len(speeds)):
        take_times.append(math.ceil((100-progresses[i])/speeds[i]))

    # 함께 배포 할 수 있는 작업의 수 계산하기
    std = take_times.popleft() # 기준 배포 작업일수
    cnt = 1 # 함께 배포할 작업의 수
    while take_times:
        now = take_times.popleft() # 배포하는데까지 걸리는 작업일수
        if now > std: # 만약 기준일보다 오래 걸린다면 : 함께 배포 불가
            answer.append(cnt) # 함께 배포할 수 있는 작업의 수를 리스트에 추가
            std = now # 새로운 기준일 업데이트
            cnt = 1 # 함께 배포할 작업의 수 업데이트
        else: # 기준일보다 적거나 같게 걸린다면 : 함께 배포 가능
            cnt += 1 # 함께 배포 가능한 작업의 수에 추가
    answer.append(cnt) # 마지막 배포 작업의 수
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))