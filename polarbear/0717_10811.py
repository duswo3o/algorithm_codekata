# 바구니 뒤집기

def reverse_basket(basket, i, j):
    re_basket = []
    for a in range(0,i-1):
        re_basket.append(basket[a])
    for a in range(j-1,i-2,-1):
        re_basket.append(basket[a])
    for a in range(j,len(basket)):
        re_basket.append(basket[a])

    return re_basket

N,M = map(int,input().split())
basket = [b+1 for b in range(N)]
for _ in range(M):
    i, j = map(int,input().split())
    basket = reverse_basket(basket, i, j)
    # print(basket)

print(" ".join(map(str, basket)))
