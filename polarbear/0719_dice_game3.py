# 주사위 게임 3

from collections import Counter

def solution(a, b, c, d):
    if a == b == c == d:
        return 1111*a

    dice = Counter([a,b,c,d])
    k = list(dice.keys())
    if len(dice) == 2:
        if dice[a] == 2:
            return (k[0]+k[1])*abs(k[0]-k[1])
        else:
            if dice[k[0]] == 3:
                return (10*k[0]+k[1])**2
            else:
                return (10*k[1]+k[0])**2
    elif len(dice) == 3:
        if dice[k[0]] == 2:
            return k[1]*k[2]
        elif dice[k[1]] == 2:
            return k[0]*k[2]
        else:
            return k[0]*k[1]

    else:
        return min(a, b, c, d)


print(solution(2,2,2,2))
print(solution(4,1,4,4))
print(solution(6,3,3,6))
print(solution(2,5,2,6))
print(solution(6,4,2,5))
