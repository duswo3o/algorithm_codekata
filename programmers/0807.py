# 예상 대진표

def solution(N,A,B):
    cnt = 0
    A, B = A-1, B-1
    while A != B:
        cnt += 1
        A = A//2
        B = B//2
    return cnt

print(solution(8,4,7))