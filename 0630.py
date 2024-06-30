from itertools import combinations

def solution(numbers):
    triple = list(combinations(numbers, 3))
    answer = 0
    for i in triple:
        if sum(i) == 0:
            answer += 1
    return answer


print(solution([-2, 3, 0, 2, -5]))