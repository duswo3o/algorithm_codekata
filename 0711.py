# 명예의 전당

def solution(k, score):
    hof = [score[0]] # 명예의 전단
    result = [hof[-1]] # 명예의 전당에서 가장 낮은 점수들을 기록

    for i in range(1, len(score)): 
        hof.append(score[i]) # 명예의 전당에 점수 추가
        hof.sort(reverse=True) # 내림차순 정렬

        if len(hof) > k: # 만약 명예의 전당 길이가 k이상이 되면
            hof.pop() # 가장 낮은 점수를 뺌

        result.append(hof[-1]) # 명예의 전당에서 가잔 낮은 점수를 result에 추가

    return result


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))