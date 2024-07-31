# 피로도

def solution(k, dungeons):
    l = len(dungeons) # 던전의 길이
    visited = [0] * l # 던전 방문 표시를 위해 방문 배열 만들어주기
    answer = 0 # 방문한 던전의 개수

    # 깊이 우선 탐색
    def dfs(fati, v):
        nonlocal answer
        for i in range(l):
            d = dungeons[i] # 던전 선택

            # 던전에 필요한 피로도 이상이고 방문한 적이 없다면
            if fati >= d[0] and v[i] == 0:
                v[i] = 1 # 던전 방문
                dfs(fati-d[1], v) # 다음 던전 탐색
                answer = max(answer, sum(v)) # 방문한 던전의 쵀대 개수 리턴
                v[i] = 0 # 방문해제
        return max(answer, sum(v))


    # 시작 던전을 바꾸어가며 던전 탐색
    for j in range(l):
        if dungeons[j][0] <= k:
            visited[j] = 1 # 던전 방문
            dfs(k-dungeons[j][1], visited) # 다음 던전 탐색
            visited[j] = 0 # 던전 방문 해제

    return answer

print(solution(80, [[80,20],[50, 40],[30, 10]]))
print(solution(4, [[4,3],[2,2],[2,2]]))