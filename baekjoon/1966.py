# 프린터 큐

from collections import deque
import sys

for _ in range(int(input())): # 테스트케이스의 수만큼 반복
    command = list(map(int, sys.stdin.readline().split())) # 문서의 개수와 몇 번쩨로 인쇄되었는지 궁금한 문서(인덱스)
    level = list(map(int, sys.stdin.readline().split())) # 문서의 중요도
    document = deque((i, l) for i,l in enumerate(level)) # 문서의 인덱스와 중요도를 가진 리스트
    level.sort() # 중요도를 오름차순 정렬

    now_level = level.pop() # 가장 높은 중요도
    cnt = 0 # 인쇄되는 순서
    while document:
        d = document.popleft() # 가장 앞에 있는 문서
        if now_level == d[1] and command[1] == d[0]: # 출력 가능한 중요도이고, 찾는 인덱스일 때
            print(cnt+1) # 출력
            break

        if d[1] == now_level: # 출력할 중요도와 같을 때
            cnt += 1 # 인쇄
            now_level = level.pop() # 중요도 업데이트
        else:
            document.append(d) # 출력할 문서가 아니면 다시 맨 뒤에 저장
