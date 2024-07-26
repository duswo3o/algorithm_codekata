# N과 M (2)

def comb(arr, n):
    result = []

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr)):
            temp = arr[i+1:] # 이전 값들은 이미 사용했으니 무시
            for c in comb(temp, n-1):
                result.append([arr[i]]+c)

    return result

# print(comb(["1","2","3","4"], 2))

N, M = map(int, input().split())
l = [str(i+1) for i in range(N)]
combs = comb(l, M)
for com in combs:
    print(" ".join(com))
