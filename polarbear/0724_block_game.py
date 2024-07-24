# 블록 놀이


def change_block(n, k, block):
    c = 0
    for b in range(len(block)):
        if b < n:
            if block[b] != block[n]-k*(n-b): c +=1
        else:
            if block[b] != block[n]+k*(b-n): c +=1
    return c

N, K = map(int, input().split())
block = list(map(int, input().split()))
change = N-1

for n in range(N):
    if block[n] - K*n < 1:
        continue
    change = min(change, change_block(n, K, block))
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