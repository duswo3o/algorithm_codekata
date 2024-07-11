# 내적

def solution(a,b):
    return sum([0+a[i]*b[i] for i in range(len(a))])

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))