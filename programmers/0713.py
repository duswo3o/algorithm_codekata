# 키드뭉치

from collections import deque
def solution(cards1, cards2, goal):
    l = len(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    c1, c2= cards1.popleft(), cards2.popleft()

    for i in range(l):
        g = goal.popleft()
        if g not in [c1,c2]:
            return "No"

        if c1 == g and len(cards1) > 0:
            c1 = cards1.popleft()
        if c2 == g and len(cards2) > 0:
            c2 = cards2.popleft()

    return "Yes"

# print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
# print(solution(["show", "lot", "please", "the", "me"], ["money"], ["show", "me", "the", "money"]))
print(solution(["a","b","c"],["d","e","f"],["a","d","f"])) # No