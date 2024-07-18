# 나머지가 1이 되는 수 찾기

def solution(n):
    for x in range(2,n//2+1):
        if n%x == 1:
            return x
    return n-1

print(solution(3))