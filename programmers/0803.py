# JadenCase 문자열 만들기

def solution(s):
    s = s.split(" ") # 공백 문자가 연속으로 나올 수 있음
    for i in range(len(s)):
        s[i] = s[i].lower().capitalize() # 첫 글자는 대문자, 나머지는 소문자
    return " ".join(s)

print(solution("3people unFollowed me"))
print(solution("for the last week"))