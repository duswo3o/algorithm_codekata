# N과 M (1)

def perm(arr, n):
    result = []

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            temp = [a for a in arr]
            temp.remove(arr[i]) # 사용한 원소를 제거한 리스트
            for p in perm(temp, n-1):
                result.append([arr[i]]+p)
    return result

# print(perm(["1","2","3"],3))
# print(perm(['1','2','3'],2))

N, M = map(int, input().split())
l = [str(i+1) for i in range(N)]
perms = perm(l, M)

for per in perms:
    print(" ".join(per))