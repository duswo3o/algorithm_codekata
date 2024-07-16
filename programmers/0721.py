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
    X, Y = Counter(X), Counter(Y)

    common = set(X.keys())&set(Y.keys())
    if common == set("0"):
        return "0"

    common_dict = {}

    for c in common:
        common_dict[c] = min(X[c], Y[c])

    l = []
    for i in common_dict.items():
            l.append(i[0]*i[1])

    return ''.join(sorted(l, reverse=True)) if len(l)!=0 else "-1"









# print(type(solution("100", "2345")))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))


