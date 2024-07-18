# 자릿수 더하기

def solution(N):
    N = str(N)
    answer = 0
    for i in N:
        answer += int(i)
    return answer