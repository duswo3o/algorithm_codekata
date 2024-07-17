# x만큼 간격이 있는 n개의 숫자

solution = lambda x,n : [x*(i+1) for i in range(n)]

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))