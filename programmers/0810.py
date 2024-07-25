# # 귤 고르기
#
# from collections import defaultdict
#
# def solution(k, tangerine):
#     ans = 0
#
#     cnt_tan = defaultdict(int) # 귤의 크기 : 개수
#     for t in tangerine:
#         cnt_tan[t] += 1
#     # print(cnt_tan)
#
#     cnt_dict = defaultdict(int) # 귤의 개수 : 귤의 개수가 같은게 몇 종류인지
#     cnt_list = cnt_tan.values() # 귤의 개수 리스트
#     for c in cnt_list:
#         cnt_dict[c] += 1
#     # print(cnt_dict)
#
#     cnt_list = sorted(cnt_list, reverse=True) # 내림차순 정렬
#     tang = 0 # 상자에 담은 귤의 개수
#
#
#
#     # 가장 개수가 많은 귤의 종류부터 담기
#     # for i in cnt_list:
#     #     if tang >= k:
#     #         while tang > k:
#     #             tang -= j
#     #             ans -= 1
#     #         if tang == k : return ans
#     #         else: return ans+1
#     #
#     #     ans += cnt_dict[i]
#     #     tang += cnt_dict[i] * i
#     #     j = i
#     # return ans
#
#     for i in cnt_list:
#         if tang < k:
#             tang += cnt_dict[i]*i
#             ans += cnt_dict[i]
#             j = i
#         else:
#             while tang > k:
#                 tang -= j
#                 ans -=1
#             if tang == k: return ans
#             else: return ans+1
#     return ans


###############################################################
###############################################################
###############################################################
###############################################################

from collections import defaultdict

def solution(k, tangerine):
    ans = 0

    cnt_tangerine = defaultdict(int)
    for t in tangerine:
        cnt_tangerine[t] += 1

    sorted_tangerine = sorted(cnt_tangerine.items(), reverse=True,  key = lambda x : x[1])

    tang = 0
    for kind, count in sorted_tangerine:
        if tang >= k:
            return ans
        tang += count
        ans += 1

    return ans







# print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
# print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
# print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1
# print(solution(6, [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # 4
print(solution(3,[1,1,2,2])) # 2
print(solution(2,[1000,2000,2000,1000])) # 1
# print(solution(3,[1,2,5])) # 3
print(solution(1, [1]))