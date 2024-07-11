# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if i**0.5 == int(i**0.5): # 제곱수이면 약수가 홀수개
            answer -= i
        else: # 제곱수가 아니면 약수가 짝수개
            answer += i
    return answer

print(solution(13,17))
print(solution(24,27))