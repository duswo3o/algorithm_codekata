import sys, math

X, Y = map(int, sys.stdin.readline().strip().split())
Z = math.floor(Y*100/X)
# print(Z)
if Z >= 99:
    print(-1)
else:
    a = (X*Z + X - 100*Y)/(99-Z)
    print(math.ceil(a))
