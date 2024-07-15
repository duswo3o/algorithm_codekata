# 정수 내림차순으로 배치하기

# def solution(n):
#     return int(''.join(sorted([i for i in str(n)], reverse=True)))

solution = lambda x:int(''.join(sorted([i for i in str(x)], reverse=True)))