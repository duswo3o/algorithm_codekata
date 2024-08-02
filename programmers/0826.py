# 롤케이크 자르기

from collections import deque

def solution(topping):
    answer = 0
    mid = len(topping)//2

    front, rear = topping[:mid], deque(topping[mid:])
    if len(set(front)) == len(set(rear)):
        answer+=1

    while front:
        rear.appendleft(front.pop())
        f,r = len(set(front)), len(set(rear))
        if  f==r:
            answer +=1
            # continue
        else:
            break

    front, rear = topping[:mid], deque(topping[mid:])
    while rear:
        front.append(rear.popleft())
        f, r = len(set(front)), len(set(rear))
        if f == r:
            answer += 1
            # continue
        else:
            break

    return answer




print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0
print(solution([1,1,4,7,7,5])) # 1
print(solution([4,1,1,1,5,2,2,2,5])) # 1
print(solution([1,1,1,1,1])) # 4