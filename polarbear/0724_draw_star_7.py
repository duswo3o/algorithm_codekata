# 별 찍기 -7

N = int(input())

base = N*2-1
mid = base//2

# 증가하는 별
for i in range(N):
    print(" "*(mid-i) + "*"*(2*i+1))
# 감소하는 별
for i in range(N-2,-1,-1):
    print(" " * (mid - i) + "*" * (2 * i + 1))

