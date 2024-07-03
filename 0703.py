# 시저 암호

s = "yY"
n = 2

def solution(s, n):
    answer = []
    for i in s:
        if i == " ":
            answer.append(" ")
        elif (ord(i)+n > ord('z')) or (ord(i)+n >= ord('Z')):
            answer.append(chr(ord(i)-26+n))
        else:
            answer.append(chr(ord(i)+n))
    return ''.join(answer)

print(solution(s,n))
    