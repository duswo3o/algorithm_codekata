# 기사단원의 무기

# 약수의 개수 구하는 함수
def count_divisor(n):
    cnt = 1
    if n == 1:
        return 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            cnt += 1
    return cnt*2 if int(n**0.5) != n**0.5 else (cnt-1)*2+1



def solution(number, limit, power):
    knight = [i+1 for i in range(number)] # 이거 굳이 안 만들었어도 됐을 듯
    needed_iron = 0 # 필요한 철의 무게

    for k in knight:
        k_attack = count_divisor(k) # 기사단원 무기의 공격력 (번호의 약수의 개수)
        if k_attack > limit: # 제한값을 초과하면
            needed_iron += power # 정해진 공격력 무기 사용
        else: # 제한값 초과 안하면 자신의 공격력 무기 사용
            needed_iron += k_attack

    return needed_iron



# # 한 줄 코딩
# def solution2(number, limit, power):
#     return sum([count_divisor(i+1) if count_divisor(i+1)<=limit else power for i in range(number)])


print(solution(5,3,2))
print(solution(10,3,2))

