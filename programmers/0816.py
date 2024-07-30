# 할인 행사

from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        # 10일동안 할인하는 품목
        now_discount = discount[i:i+10]
        now_discount = Counter(now_discount)
        # 원하는 모든 제품을 살 수 있는지 확인
        possible = True
        for w in range(len(want)):
            # 원하는 모든 뭂품을 살 수 없는 경우
            if now_discount[want[w]] != number[w]:
                possible = False
                break
        if possible:
            answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))