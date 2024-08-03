# 숫자 변환하기

def solution(x, y, n):
    ans = []

    def dfs(x, y, n, cnt):
        nonlocal ans
        if x >= y:
            if x == y:
                # print(cnt)
                ans.append(cnt)
                return
            else:
                # print(-1)
                return

        dfs(x + n, y, n, cnt + 1)
        dfs(x * 2, y, n, cnt + 1)
        dfs(x * 3, y, n, cnt + 1)

    dfs(x,y,n,0)
    return min(ans) if ans else -1

print(solution(10, 40, 5))
print(solution(10,40,30))
print(solution(2,5,4))