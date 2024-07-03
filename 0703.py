# 시저 암호

s = "aAzZ"
n = 25

def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer+=" "
        elif (ord(i) <= ord('Z') and ord(i)+n > ord('Z')) or (ord(i)+n > ord('z')):
            answer += chr(ord(i)-26+n)
        else:
            answer += chr(ord(i)+n)
    return answer

print(solution(s,n)) 