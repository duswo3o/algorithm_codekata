# 이상한 문자 만들기

text = 'try hello python'
answer = ''

for i, t in enumerate(text):
    if i%2 == 0:
        answer += t.upper()
    else:
        answer += t.lower()

print(answer)