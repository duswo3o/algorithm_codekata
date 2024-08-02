# 뒤에 있는 큰 수 찾기

from collections import deque

def solution(numbers):
    answer = []
    numbers = deque(numbers)

    while numbers:
        num = numbers.popleft()
        rear = -1
        for i in numbers:
            if i>num:
                rear = i
                break
        answer.append(rear)
    return answer


print(solution([2,3,3,5]))
print(solution([9,1,5,3,6,2]))