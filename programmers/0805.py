# 피보나치 수

def solution(n):
    fibo = [0,1,1]
    for i in range(2, n):
        fibo.append(fibo[i-1]+fibo[i])
    return fibo[n]%1234567

print(solution(3))
print(solution(5))