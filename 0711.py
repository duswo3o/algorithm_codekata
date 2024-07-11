# 명예의 전당

def solution(k, score):
    hof = sorted(score[:k], reverse=True)
    result = [hof[-1]]*k

    for i in range(k, len(score)):
        hof.append(score[i])
        hof.sort(reverse=True)
        hof.pop()
        result.append(hof[-1])

    return result


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))