# 문자열 다루기 기본

def solution(s):
    return True if (s.isdigit()==True and len(s) in [4,6] )else False

print(solution("a234"))
print(solution("1234"))