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


def solution(s):
    pre_position = {} # 문자의 가장 최신 위치
    answer = [] # 가장 가까운 같은 글자의 위치

    for i in range(len(s)):
        if s[i] in pre_position.keys(): # 만약에 이전에 같은 글자가 존재한다면
            answer.append(i-pre_position[s[i]]) # 현재 위치(인덱스)-이전 위치(인덱스)
            pre_position[s[i]] = i # 현재의 위치(인덱스)로 업데이트
        else: # 이전에 같은 글자가 존재하지 않는다면
            answer.append(-1) # 가까운 글자의 위치 리스트에 -1추가
            pre_position[s[i]] = i # 현재 위치로 딕셔너리 업데이트
    
    return answer