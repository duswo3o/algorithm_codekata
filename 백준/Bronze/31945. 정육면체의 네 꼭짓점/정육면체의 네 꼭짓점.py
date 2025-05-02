import sys
input = sys.stdin.readline

faces = [[0,1,2,3], [0,1,4,5], [0,2,4,6], [1,3,5,7], [2,3,6,7], [4,5,6,7]]

T = int(input())
for _ in range(T):
    f = sorted(list(map(int, input().split())))
    if f in faces:
        print("YES")
    else:
        print("NO")