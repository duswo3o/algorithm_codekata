# 의상

from collections import defaultdict
def solution(clothes):
    my_closet = defaultdict(int)
    # 옷의 종류 : 개수
    for c in clothes:
        my_closet[c[1]] += 1

    answer = 1
    # 경우의 수 계산
    for i in my_closet.values():
        answer *= i+1
    # 어떤 종류도 선택 하지 않는 경우를 빼줌
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))