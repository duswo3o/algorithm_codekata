## 우유 축제
# 딸기(0) -> 초코(1) -> 바나나(2)

import sys

N = int(sys.stdin.readline()) # 우유 가게의 수
milks = list(map(int, sys.stdin.readline().split())) # 가게 정보

total = 0 # 마실 수 있는 우유의 수
drink_type = 0 # 현재 마실 우유의 종류
for milk in milks:
    if drink_type == milk: # 가게에서 파는 우유와 마실수 있는 우유가 같은 경우
        total += 1 # 마실 수 있는 우유의 수 증가
        drink_type = (drink_type + 1) % 3 # 마실 우유 정보 업데이트

print(total)