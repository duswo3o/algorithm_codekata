# H-Index

from collections import defaultdict

def solution(citations):
    h_index = defaultdict(int)
    n = len(citations)
    # key = 인용된 횟수, value = 인용된 논문의 수
    for cnt in citations:
        for c in range(cnt):
            h_index[c] += 1

    # print(h_index)
    # 인용된 수와 인용된 논문의 수보다 같거나 작아지는 수 == H-Index
    for i in range(n,-1,-1):
        if i <= h_index[i]:
            return h_index[i]

print(solution([3,0,6,1,5]))