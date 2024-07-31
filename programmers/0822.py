# k 진수에서 소수 개수 구하기

from collections import deque

# k진수로 변환하는 함수
def k_transfer(number,k_div):
    t = deque()
    while number//k_div > 0:
        t.appendleft(str(number%k_div))
        number //= k_div
    t.appendleft(str(number))
    return t

# 소수인지 판별하는 함수
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1


def solution(n,k):
    k_trans = k_transfer(n,k) # 입력받은 수를 k진수로 변환하기

    # 변환된 수에 있는 1을 제외한 10진수 (0을 기준으로 나눈)
    num_list = []
    temp = ""
    for i in k_trans:
        if i == "0" and temp == "1":
            temp = ""
        if i == "0" and len(temp)>0:
            num_list.append(int(temp))
            temp = ""
        elif i != "0":
            temp += i
    # 마지막 수가 0이 아닌 경우는 추가가 안될 수 있음
    # 마지막에 있는 10진수가 1이 아닌 경우 리스트에 추가
    if len(temp) > 0 and temp!="1":
        num_list.append(int(temp))

    # k진수로 변환된 수에서 0을 기준으로 분리된 10진수 중 소수의 개수
    answer = 0
    for num in num_list:
        answer += is_prime(num)
    return answer

print(solution(437674, 3))
print(solution(110011, 10))
print(solution(101,10)) # tc 3번