# 부족한 금액 계산하기

def solution(price, money, count):
    for i in range(count):
        money -= price*(i+1)
    return abs(money)




print(solution(3,20,4)) # 10