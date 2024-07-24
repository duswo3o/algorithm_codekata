# 멀리 뛰기

# 팩토리얼 구하기
def factorial(n):
    fac = [1,1]
    for i in range(2,n+1):
        fac.append(fac[i-1]*i)
    return fac[-1]

# print(factorial(3))

def solution(n):
    result = 0 # 멀리뛰기의 경우의 수
    one, two = n, 0 # 1칸과 2칸의 수
    while two <= n//2: # 2칸의 수가 n//2보다 커지면 종료
        # 동일한 값이 있는 순열 계산하기
        result += (factorial(one+two)//(factorial(one)*factorial(two)))
        # 한 칸과 두 칸의 수 업데이트
        one -= 2
        two += 1
    return result%1234567

print(solution(4))
print(solution(3))
print(solution(1))
print(solution(2))
print(solution(2000))