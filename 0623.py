# 부족한 금액 계산하기

def solution(price, money, count):
    for i in range(count): # count번 반복
        money -= price*(i+1) # 현재 가진 돈에서 사용힌 돈 빼기

    # 돈이 마이너스 인 경우(돈이 부족한 경우) 절댓값으로 부족한 돈 반환, 아닌경우 0반환
    return abs(money) if money < 0 else 0




print(solution(3,20,4)) # 10