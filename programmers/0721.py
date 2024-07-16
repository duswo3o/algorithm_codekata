# 숫자 짝꿍

from collections import deque
def solution(X,Y):
    X = [i for i in X]
    Y = deque([i for i in Y])
    common = []

    while X :
        x = X.pop()
        for _ in range(len(Y)):
            y = Y.popleft()
            if x == y:
                common.append(x)
                break
            else:
                Y.append(y)

    return f'{int("".join(sorted(common, reverse=True)))}' if len(common) != 0 else "-1"

print(type(solution("100", "2345")))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))