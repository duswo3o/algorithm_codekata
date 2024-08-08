# 소수 찾기

from itertools import permutations


# 소수인지 판별
def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, int(num**0.5)+1):
        if num%n == 0:
            return False
    return True


def solution(numbers):
    answer = 0 # 소수의 개수
    numbers = [number for number in numbers] # 문자열의 숫자를 하나씩 리스트에 넣기

    concat_number = set() # 합쳐진 문자열(숫자)의 집합 -> 중복제거
    # 흩어진 조각들 붙이기(1개부터 n개 만큼)
    for i in range(1, len(numbers)+1):
        temp = list(permutations(numbers, i))
        # 순열로 만들어진 것을 합쳐서 정수로 변환한 후에 집합에 추가
        for t in temp:
            concat_number.add(int("".join(t)))

    # 집합 안에 있는 수가 소수인지 확인
    for c in concat_number:
        if is_prime(c):
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))