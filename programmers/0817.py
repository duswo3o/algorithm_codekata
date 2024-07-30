# 의상

from collections import defaultdict
def solution(clothes):
    my_closet = defaultdict(int)
    for c in clothes:
        my_closet[c[1]] += 1

    answer = 1
    for i in my_closet.values():
        answer *= i+1

    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))