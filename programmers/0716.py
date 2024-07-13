# 소수만들기

from itertools import combinations

# 소수인지 아닌지 확인하는 함수
def is_prime(n):
    for i in range(2, int(n**0.5)+1): # 2부터 root(n)까지 반복
        if n % i == 0: # 나누어떨어지는 수가 있다면 소수가 아님 -> 0 리턴
            return 0
    return 1 # 나누어떨어지는 수가 없다면 소수임 -> 1 리턴

def solution(nums):
    combi = list(combinations(nums, 3)) # 조합 생성
    cnt = 0 # 소수의 개수
    for c in combi: # 조합에서
        cnt += is_prime(sum(c)) # 합이 소수면 +1 아니면 +0
    return cnt

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))