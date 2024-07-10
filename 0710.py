# 콜라 문제

def solution(a, b, n):
    get_bottle = 0

    while n//a > 0:
        get_bottle += n//a
        n = (n//a)*b + (n%a)

    return get_bottle

print(solution(2,1,20))
print(solution(3,1,20))