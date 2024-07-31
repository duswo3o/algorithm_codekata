# 피로도

def solution(k, dungeons):
    l = len(dungeons)
    visited = [0] * l
    answer = 0

    def dfs(fati, v):
        nonlocal answer
        for i in range(l):
            d = dungeons[i] # 던전 선택
            if fati >= d[0] and v[i] == 0:
                v[i] = 1
                dfs(fati-d[1], v)
                answer = max(answer, sum(v))
                v[i] = 0
        return max(answer, sum(v))

    # answer = max(answer,dfs(k, visited))
    for j in range(l):
        if dungeons[j][0] <= k:
            visited[j] = 1
            dfs(k-dungeons[j][1], visited)
            visited[j] = 0

    return answer

print(solution(80, [[80,20],[50, 40],[30, 10]]))
print(solution(4, [[4,3],[2,2],[2,2]]))