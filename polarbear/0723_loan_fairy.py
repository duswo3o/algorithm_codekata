# 대출 요정

import sys

N = int(input()) # 대출 요청의 개수

loan = [] # [대출일자, 반납일자] 리스트를 담는 리스트
# 대출일자와 반납일자 입력받기
for _ in range(N):
    loan.append(list(map(int, sys.stdin.readline().split())))
loan.sort() # 정렬 안넣으면 틀림,,,,,

book = int(input()) # 책의 개수

# borrow = 1
# possible = 1
#
# for i in range(len(loan)-1):
#     if loan[i][1] > loan[i+1][0]:
#         borrow += 1
#         if borrow > book:
#             possible = 0
#             break
# print(possible)

##########################################################################################
##########################################################################################

borrow = [0 for _ in range(book)] # 책의 반납일자를 담을 리스트
possible = 1 # 모든 대출 요청에 대해 가능

for l in loan:
    if l[0] < min(borrow): # 책의 가장 빠른 반납일자가 대출일자보다 크면
        possible = 0 # 대출 불가능
        break # 반복문 종료

    for b in range(book): # 책의 개수만큼 반복
        if l[0] >= borrow[b]: # 현재 책의 반납일자가 대출일자보다 작으면
            borrow[b] = l[1] # 책 대출, 반납일자 업데이트
            break
print(possible)


