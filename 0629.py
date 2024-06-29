# 이상한 문자 만들기
# 1차 제출 실패 = 공백을 기준의로 단어의 짝수와 홀수를 바꿔줘야 함

text = 'try hello python'

n = 0
answer = ''
for i in text:
    if i == ' ':
        answer+=i
        n = 0
    else:
        if n % 2 == 0:
            answer += i.upper()
            n+=1
        else:
            answer += i.lower()
            n+=1

print(answer)