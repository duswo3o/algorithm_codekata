# 문자열 나누기

from collections import deque
def solution(s):
    s = deque([i for i in s]) # 문자역을 큐로 뱐환
    seperated_string = 1 # 분리된 문자역의 개수 :  만약 분리가 안 되면 하나의 문자열이르모 1로 시작
    while s: # s가 빈 리스트가 아니면
        x = s.popleft() # 첫 번째 요소를 x애 저장
        count_x = 1 # x의 개수
        count_y = 0 # x가 아닌 것의 개수

        while s: # 문자 리스트를 돌면서
            if count_x == count_y: # 두 개의 개수가 같아지는 지점에서
                seperated_string += 1 # 믄지 븐리
                break # 새로 시작

            next = s.popleft() # 다음 문자열 추출
            if next == x: # x와 같으면
                count_x += 1 # x의 개수에 추가
            else: # 다르면
                count_y += 1 # 다른 개수에 추가

    return seperated_string

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))