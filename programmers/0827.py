# 숫자 변환하기

def solution(x, y, n):
    ans = -1

    def dfs(x, y, n, cnt):
        nonlocal ans

        if int(y) != y:
            return

        if x >= y:
            if x == y:
                # print(cnt)
                if ans == -1:
                    ans = cnt
                else:
                    ans = min(ans, cnt)
                return
            else:
                # print(-1)
                return

        dfs(x, y-n, n, cnt + 1)
        dfs(x, y/2, n, cnt + 1)
        dfs(x, y/3, n, cnt + 1)

    dfs(x,y,n,0)
    return ans

print(solution(10, 40, 5))
print(solution(10,40,30))
print(solution(2,5,4))
print(solution(38, 40, 2))