# H-Index

from collections import defaultdict

def solution(citations):
    h_index = defaultdict(int)
    n = len(citations)

    for cnt in citations:
        for c in range(cnt):
            h_index[c] += 1

    # print(h_index)

    for i in range(n,-1,-1):
        if i <= h_index[i]:
            return h_index[i]

print(solution([3,0,6,1,5]))