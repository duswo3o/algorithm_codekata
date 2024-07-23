# 피보나치 수

def solution(n):
    fibo = [0,1,1] # 피보나치 수 배열
    for i in range(2, n): # 피보나치 수 추가하기
        fibo.append(fibo[i-1]+fibo[i])
    return fibo[n]%1234567 # 피보나치 수 출력

print(solution(3))
print(solution(5))