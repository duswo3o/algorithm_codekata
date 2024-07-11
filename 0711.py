# 명예의 전당

def solution(k, score):
    hof = [score[0]]
    result = [hof[-1]]

    for i in range(1, len(score)):
        hof.append(score[i])
        hof.sort(reverse=True)

        if len(hof) > k:
            hof.pop()
            
        result.append(hof[-1])

    return result


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))