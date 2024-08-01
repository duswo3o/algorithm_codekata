# 모음 사전

def solution(word):
    aeiou = {"A":1, "E":2, "I":3, "O":4, "U":5}
    digit = [780, 155, 30, 5, 0] # 각 자리 수의 경우의 수
    answer = 0

    for idx, w in enumerate(word):
        answer += digit[idx]*(aeiou[w]-1) + aeiou[w]

    return answer

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))