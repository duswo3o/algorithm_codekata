# 롤케이크 자르기

from collections import Counter

def solution(topping):
    answer = 0
    front = set()
    rear = Counter(topping)

    for i in topping:
        front.add(i)
        rear[i] -= 1
        if rear[i] == 0:
            del rear[i]
        if len(front) == len(rear.keys()):
            answer += 1
    return answer




print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0
print(solution([1,1,4,7,7,5])) # 1
print(solution([4,1,1,1,5,2,2,2,5])) # 1
print(solution([1,1,1,1,1])) # 4