# n^2 배열 자르기

from itertools import chain

def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        i = idx // n # 행 번호
        j = idx % n # 열 번호

        value = max(i+1, j+1) # 행과 열 중에서 큰 값음 값으로 함
        answer.append(value) # 리스트에 숫자 추가

    return answer

print(solution(3,2,5))
print(solution(4,7,14))