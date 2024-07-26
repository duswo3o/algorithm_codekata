# 연산자 끼워넣기

#  # 순열 구현하기
# # 순열 구현해서 사용하고 싶었으나 리스트는 집합연산이 불가해서 모듈 사용
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

from itertools import permutations

N = int(input()) # 수의 개수
num_list = input().split() # N 개의 수
operator = ["+", "-", "*", "//"]
cnt_operator = list(map(int, input().split())) # 각 연산자의 개수

l_operator = [] # 사용할 연산자
for idx in range(4):
    for _ in range(cnt_operator[idx]):
        l_operator.append(operator[idx])


# print(l_operator)
# O = set(perm(l_operator, N-1))
O = set(permutations(l_operator, N-1)) # 연산자 순열 중복제거

# 최대값, 최소값
top, lower = -1e9, 1e9

for i in O:
    # 연산자 우선순위를 무시하고 앞에서부터 진행
    s = num_list[0]
    for j in range(N-1):

        # 음수를 양수로 나누는 경우 : 양수로 바꾼 뒤 몫을 취하고 몫을 음수로 바꿈
        if i[j] == "//" and int(s) < 0:
            s = -(abs(s)//int(num_list[j+1]))
        else:
            s = eval(f"{s}{i[j]}{num_list[j+1]}") # 문자열 연산이므로 eval 사용

    top = max(s, top) # 최대값 업데이트
    lower = min(s, lower) # 최소값 업데이트

print(top)
print(lower)