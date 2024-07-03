# 시저 암호

s = "AB"
n = 1

answer = []
for i in s:
    if i == " ":
        answer.append(" ")
    else:
        answer.append(chr(ord(i)+n))

print(''.join(answer))
    