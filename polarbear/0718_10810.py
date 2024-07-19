# 공 넣기

N, M = map(int,input().split())
basket = ["0" for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1, j): # i번부터 j반까지 바구니들에 대해
        basket[b] = str(k) # 바구니 업데이트

print(" ".join(basket))