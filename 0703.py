# 시저 암호

s = "aY"
n = 2

def solution(s, n):
    answer = []
    for i in s:
        if i == " ":
            answer.append(" ")
        elif (ord(i) <= ord('Z') and ord(i)+n >= ord('Z')) or (ord(i)+n >= ord('z')):
            answer.append(chr(ord(i)-26+n))
        else:
            answer.append(chr(ord(i)+n))
    return ''.join(answer)

print(solution(s,n)) 