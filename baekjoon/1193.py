# 분수 찾기

X = int(input())

n = 1
while X > n*(n+1)/2:
    n += 1

p = X - ((n)*(n-1)//2)
q = abs(n-p+1)
if n%2 == 0:
    print(f"{p}/{q}")
else:
    print(f"{q}/{p}")

