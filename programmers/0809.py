# 멀리 뛰기

def factorial(n):
    fac = [1,1]
    for i in range(2,n+1):
        fac.append(fac[i-1]*i)
    return fac[-1]

# print(factorial(3))

def solution(n):
    result = 0
    one, two = n, 0
    while two <= n//2:
        result += (factorial(one+two)//(factorial(one)*factorial(two)))
        one -= 2
        two += 1
    return result%1234567

print(solution(4))
print(solution(3))
print(solution(1))
print(solution(2))
print(solution(2000))