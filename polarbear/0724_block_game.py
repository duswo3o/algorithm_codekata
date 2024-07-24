# 블록 놀이

# n = 가준 인덱스 , 등차 = k, 블록 배열 = block
def change_block(n, k, block):
    c = 0 # 바꾸어야 하는(쌓거나 빼야하는) 블럭의 수
    for b in range(len(block)):
        if b < n: # 기준 인덱스보다 낮은 경우
            if block[b] != block[n]-k*(n-b): c +=1 # 기준 인덱스와의 등차가 일치하지 않는 경우
        else: # 기준 인덱스보다 크커나 같은 경우
            if block[b] != block[n]+k*(b-n): c +=1
    return c

N, K = map(int, input().split()) # 블럭의 수, 블럭의 차
block = list(map(int, input().split())) # 블럭
change = N-1

for n in range(N): # 모든 블럭을 탐색
    if block[n] - K*n < 1: # 첫 번째 항이 1보다 작은 경우
        continue # 해당 블럭을 기준으로 등차를 생성 할 수 없음
    change = min(change, change_block(n, K, block)) # 수정해야 하는 블럭의 최소 개수
print(change)


########################################################
########################################################
########################################################
########################################################
########################################################


# time = 0
# for i in range(N-1):
#     if block[i+1] - block[i] != K:
#         time += 1
#         block[i+1] = block[i] + K
# print(time)


# satisfy = []
# for i in range(N-1):
#     if block[i+1]-block[i] == K:
#         satisfy.append(True)
#     else : satisfy.append(False)
#
# for i in range(N-1):
#     if satisfy[i] == False:
#         if satisfy[i+1] == False:
#             block[i+1] = block[i]+K
#         else:
#             block[i] = block[i+1]-K




""" 
==============================================================================================================
==============================================================================================================
==============================================================================================================
"""




# time = 0
# for i in range(1, N-1):
#     if block[i] - block[i-1] != K:
#         time += 1
#         if block[i] - K > 0:
#             block[i-1] = block[i] - K
#         else: block[i] = block[i-1] + K
#     elif block[i] - block[i-1] == K and block[i+1] - block[i] != K:
#         time += 1
#         block[i+1] = block[i] + K
# print(time)



""" 
==============================================================================================================
==============================================================================================================
==============================================================================================================
"""




# i , j = 0, 0
# good = []
# for n in range(1, N-1):
#     if block[n] - block[n-1] == K and block[n+1]-block[n] == K:
#         j = n+1
#     elif (block[n] - block[n-1] != K) and (block[n+1] - block[n] == K):
#         i = n
#     elif (block[n] - block[n-1] == K) and (block[n+1] - block[n] != K):
#         good.append((i,j))
#
# if len(good)==0:
#     good.append((i,j))
#
# good.sort(key = lambda x : x[1]-x[0])
# # print(good)
# while good:
#     st, ed = good.pop()
#     if block[st] - K*st > 0 and block[ed]+K*j <= 1000:
#         break
#
# time = 0
# for s in range(st, 0, -1):
#     if block[s] - block[s-1] != K:
#         block[s-1] = block[s] - K
#         time += 1
# for e in range(ed, N-1):
#     if block[e+1] - block[e] != K:
#         block[e+1] = block[e] + K
#         time += 1
#
# print(time)