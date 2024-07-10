# 콜라 문제

def solution(a, b, n):
    get_bottle = 0 # 받은 병의 개수

    while n//a > 0: # 더 이상 받을 수 있는 병이 없을 때까지
        get_bottle += (n//a)*b # 받은 병의 수 계산
        n = (n//a)*b + (n%a) # 가지고 있는 빈 병의 수 업데이트

    return get_bottle

print(solution(2,1,20))
print(solution(3,1,20))
print(solution(8,1,20))