# 삼총사


# 파이썬 라이브러리를 사용한 풀이
from itertools import combinations

def solution(numbers):
    triple = list(combinations(numbers, 3)) # 조합 리스트
    answer = 0
    for i in triple:
        if sum(i) == 0: # 세 원소의 합이 0이면 삼총사 +1
            answer += 1
    return answer


# print(solution([-2, 3, 0, 2, -5]))

# q = [-2, 3, 0, 2, -5]


# 3중 반복문을 통한 풀이
def solution2(numbers):
    answer = 0
    n = len(numbers)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    answer +=1
    return answer

# print(solution2(q))