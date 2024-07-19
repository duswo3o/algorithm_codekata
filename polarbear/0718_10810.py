# 공 넣기

N, M = map(int,input().split())
basket = ["0" for _ in range(N)]
for _ in range(M):
    i,j,k = map(int,input().split())
    for b in range(i-1,j):
        basket[b] = str(k)

print(" ".join(basket))