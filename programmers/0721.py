# 숫자 짝꿍

# from collections import deque
# def solution(X,Y):
#     X = [i for i in X]
#     Y = deque([i for i in Y])
#     common = []
#
#     while X :
#         x = X.pop()
#         for _ in range(len(Y)):
#             y = Y.popleft()
#             if x == y:
#                 common.append(x)
#                 break
#             else:
#                 Y.append(y)
#
#     return f'{int("".join(sorted(common, reverse=True)))}' if len(common) != 0 else "-1"

#####################시간초과####################################
###############################################################






# def solution(X,Y):
#     X = [i for i in X]
#     Y = [i for i in Y]
#     common = set(X) & set(Y)
#     common_dict = {}
#     for c in common:
#         common_dict[c] = min(X.count(c), Y.count(c))
#
#     l = []
#     for i in common_dict.items():
#         for _ in range(i[1]):
#             l.append(i[0])
#
#     return f"{int(''.join(sorted(l, reverse=True)))}" if len(l)!=0 else "-1"



####################시간초과############################
######################################################


from collections import Counter

def solution(X,Y):
    X, Y = Counter(X), Counter(Y) # 각 문자의 개수 딕셔너리

    common = set(X.keys())&set(Y.keys()) # 공통된 문자 집합

    # 문자를 숫자형으로 변환하고 다시 문자형으로 변환하는 과정에서 시간초과 오류 발생!
    if common == set("0"): # 공통된 문자가 0밖에 없는 경우
        return "0"

    common_dict = {}

    for c in common:
        common_dict[c] = min(X[c], Y[c]) # 공통된 문자의 최소 개수

    l = []
    for i in common_dict.items(): # (공통된 문자, 개수)로 된 튜플에서 리스트에 문자*개수 추가
            l.append(i[0]*i[1])

    return ''.join(sorted(l, reverse=True)) if len(l)!=0 else "-1"









# print(type(solution("100", "2345")))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))


