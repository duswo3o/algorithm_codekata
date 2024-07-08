# 가장 가까운 같은 글자

s = 'banana'
pre_position = {}
answer = []

for i in range(len(s)):

    if s[i] in pre_position.keys():
        answer.append(i-pre_position[s[i]])
        pre_position[s[i]] = i
    else:
        answer.append(-1)
        pre_position[s[i]] = i

print(answer)