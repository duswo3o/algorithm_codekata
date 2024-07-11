# 문자열 내림차순으로 배치하기

def solution(s):
    return "".join(sorted([i for i in s], reverse=True))

print(solution("Zbcdefg"))