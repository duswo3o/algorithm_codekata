# 성격 유형 검사하기

def solution(survey, choices):
    # 성격유형
    personality = {"R":0,"T":0,
                   "C":0, "F":0,
                   "J":0, "M":0,
                   "A":0, "N":0,}

    for i, s in enumerate(survey):
        if choices[i] < 4: # 선택 번호가 4미만인 경우
            personality[s[0]] += abs(choices[i] - 4) # 질문의 앞 성격에 가운데서 떨어진 정도(절대값) 점수 부여
        else:
            personality[s[1]] += abs(choices[i] - 4) # 질문의 뒤 성격에 점수 부여

    answer = ''
    # 각 유형별로 높은 점수를 가진 성격을 결과로 추가
    answer += "R" if personality["R"] >= personality["T"] else "T"
    answer += "C" if personality["C"] >= personality["F"] else "F"
    answer += "J" if personality["J"] >= personality["M"] else "M"
    answer += "A" if personality["A"] >= personality["N"] else "N"

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"],[7, 1, 3]))