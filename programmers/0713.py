# 키드뭉치

from collections import deque
def solution(cards1, cards2, goal):
    # 리스트를 큐로 변경
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    # 각각의 첫 번째 요소 pop
    c1, c2= cards1.popleft(), cards2.popleft()

    # goal에 요소가 남아 있을 때까지
    while goal:
        g = goal.popleft() # goal의 첫 번째 요소 pop
        if g not in [c1,c2]: # 일치하는 문자가 없다면 no 리턴
            return "No"

        # 요소가 일치하고 카드의 개수가 1개 이상이면 다음 카드 다용
        if c1 == g and len(cards1) > 0:
            c1 = cards1.popleft()
        if c2 == g and len(cards2) > 0:
            c2 = cards2.popleft()

    return "Yes" # goal의 순서로 만들어진다면 yes 리턴

# print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
# print(solution(["show", "lot", "please", "the", "me"], ["money"], ["show", "me", "the", "money"]))
print(solution(["a","b","c"],["d","e","f"],["a","d","f"])) # No