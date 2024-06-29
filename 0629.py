# 이상한 문자 만들기
# 1차 제출 실패 = 공백을 기준의로 단어의 짝수와 홀수를 바꿔줘야 함

text = 'try hello python'

# n = 0
# answer = ''
# for i in text:
#     if i == ' ':
#         answer+=i
#         n = 0
#     else:
#         if n % 2 == 0:
#             answer += i.upper()
#             n+=1
#         else:
#             answer += i.lower()
#             n+=1

def solution(text):
    n = 0 # 공백을 기준으로 각 단어의 인덱스
    answer = '' 
    for i in text: # 문자열에서
        # 공벡이면 인덱스는 초기화하고 그대로 문자열에 추가
        if i == ' ': 
            answer+=i
            n = 0 
        # 문자를 만났을 때
        else:
            # 짝수번째 인덱스이면 대문자로 추가
            if n % 2 == 0:
                answer += i.upper()
                n+=1
            # 짝수번째가 아니면 소문자로 추가
            else:
                answer += i.lower()
                n+=1
    return answer

print(solution(text))