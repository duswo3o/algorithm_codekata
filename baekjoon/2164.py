# 키드2

from collections import deque

def last_card(s):
    card = deque([i+1 for i in range(s)]) # 카드 생성
    while len(card)>1: # 카드가 하나 남을 때까지
        card.popleft() # 가장 위의 카드를 버림
        card.append(card.popleft()) # 그 다음 제일 위에 있는 카드를 가아 아래로 내림
    return card.pop() # 마지막 카드

print(last_card(6))
