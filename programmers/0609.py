# 하샤드 수

def solution(x):
    harshad = x//1000 + (x%1000)//100 + (x%100)//10 + x%10
    return True if x%harshad == 0 else False

print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))