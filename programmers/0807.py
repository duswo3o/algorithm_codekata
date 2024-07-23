# 예상 대진표

def solution(N,A,B):
    cnt = 0 # 마주치는 대진 순서
    A, B = A-1, B-1
    while A != B: # A와 B가 다르면
        cnt += 1 # 대진 순서 추가
        A = A//2 # A 업데이트
        B = B//2 # B 업데이트
    return cnt

print(solution(8,4,7))