# # 연산자 끼워넣기
#
#  # 순열 구현하기
# def perm(arr, n):
#     result = []
#
#     if n == 1:
#         for i in arr:
#             result.append([i])
#         return result
#
#     if n > 1:
#         for j in range(len(arr)):
#             temp = [a for a in arr]
#             temp.remove(arr[j])
#             for p in perm(temp,n-1):
#                 result.append([arr[j]]+p)
#     return result
#
# # from itertools import permutations
#
# N = int(input()) # 수의 개수
# num_list = list(map(int,input().split())) # N 개의 수
# operator = ["+", "-", "*", "//"]
# cnt_operator = list(map(int, input().split())) # 각 연산자의 개수
#
# l_operator = [] # 사용할 연산자
# for idx in range(4):
#     for _ in range(cnt_operator[idx]):
#         l_operator.append(operator[idx])
#
#
# # print(l_operator)
# O = list(map(tuple, perm(l_operator, N-1)))
# O = set(O)
# # O = set(permutations(l_operator, N-1)) # 연산자 순열 중복제거
#
# # 최대값, 최소값
# top, lower = -1e9, 1e9
#
# for i in O:
#     # 연산자 우선순위를 무시하고 앞에서부터 진행
#     s = num_list[0]
#     for j in range(N-1):
#
#         # 음수를 양수로 나누는 경우 : 양수로 바꾼 뒤 몫을 취하고 몫을 음수로 바꿈
#         # if i[j] == "//" and int(s) < 0:
#         #     s = -(abs(s)//num_list[j+1])
#         if i[j] == "+": s = s+num_list[j+1]
#         elif i[j] == "-": s = s-num_list[j+1]
#         elif i[j] == "*": s = s * num_list[j + 1]
#         else:
#             if s < 0 : s = -(abs(s)//num_list[j+1])
#             s = s // num_list[j + 1]
#             # s = eval(f"{s}{i[j]}{num_list[j+1]}") # 문자열 연산이므로 eval 사용
#
#     top = max(s, top) # 최대값 업데이트
#     lower = min(s, lower) # 최소값 업데이트
#
# print(top)
# print(lower)
#
# # x = list(map(tuple, perm([1,2,3,4],4)))
# # print(x)



def dfs(i, total, p, m, mu, d):
    global top, lower
    if i >= N: # 마지막 수 까지 연산을 마친 경우
        top = max(top, total) # 최대값
        lower = min(lower, total) # 최소값
        return
    # 덧셈
    if p > 0:
        p -= 1
        dfs(i+1, total+num_list[i], p, m, mu, d)
        p += 1
    # 뺄셈
    if m > 0:
        m -= 1
        dfs(i+1, total-num_list[i], p, m, mu, d)
        m += 1
    # 곱셈
    if mu > 0:
        mu -= 1
        dfs(i+1, total*num_list[i], p, m, mu, d)
        mu += 1
    # 나눗셈 : 음수를 양수로 나눌 때 "//"를 사용하면 다른 값이 나올 수 있기 때문에 "/"계산 후 int를 취함
    if d > 0:
        d -= 1
        dfs(i+1, int(total/num_list[i]), p, m, mu, d)
        d += 1

N = int(input()) # 수의 개수
num_list = list(map(int, input().split())) # N 개의 수
plus, minus, mul, div = map(int, input().split())
# print(plus, minus, mul, div)

top, lower = int(-1e9), int(1e9) # int를 취하지 않으면 float라 실패로 뜸
dfs(1, num_list[0], plus, minus, mul, div)
print(top)
print(lower)


