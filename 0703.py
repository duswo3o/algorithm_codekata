# 시저 암호

s = "zZ"
n = 1

answer = []
for i in s:
    if i == " ":
        answer.append(" ")
    elif (i == 'z') or (i == 'Z'):
        answer.append(chr(ord(i)-26+n))
    else:
        answer.append(chr(ord(i)+n))


print(''.join(answer))
    