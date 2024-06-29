# 이상한 문자 만들기

text = 'try hello python'
# answer = ''

# for i, t in enumerate(text): # 입력 받은 문자를 순서대로 반복
#     if i%2 == 0: # 인덱스가 짝수일 경우 대문자
#         answer += t.upper()
#     else: # 아니면 소문자
#         answer += t.lower()

# answer = [t.upper() if i%2 == 0 else t.lower() for i, t in enumerate(text)]

# print(''.join(answer))


def solution(text):
    answer = [t.upper() if i%2 == 0 else t.lower() for i, t in enumerate(text)]
    return ''.join(answer)

print(solution(text))