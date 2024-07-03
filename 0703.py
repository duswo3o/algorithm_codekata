# 시저 암호

s = "aAzZ"
n = 25

def solution(s, n):
    answer = '' # 정답 문자열
    for i in s:
        # 공백은 밀어도 공백
        if i == " ":
            answer+=" "
        # 대문자 Z를 넘어가면 대문자 A로 소문자 z를 넘어가면 소문자 a로 시작하도록 설정
        elif (ord(i) <= ord('Z') and ord(i)+n > ord('Z')) or (ord(i)+n > ord('z')):
            answer += chr(ord(i)-26+n)
        else:
            answer += chr(ord(i)+n)
    return answer

print(solution(s,n)) 