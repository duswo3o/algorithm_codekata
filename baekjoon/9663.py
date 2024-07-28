# n_Queen

# def n_queen(n):
#     """퀸의 위치 확인
#     visited의 인덱스는 행
#     visited의 값은 열
#     visited의 인덱스와 값의 위치에 퀸을 둔다고 가정함
#     """
#     visited = [-1] * n
#     cnt = 0 # 가능한 경우의 수
#
#     # 퀸을 놓을 수 있는 자리인지 확인
#     def is_ok_on(nth_row):
#         for r in range(nth_row):
#             # 행은 언제나 다름 따라서 같은 열인지, 대각선에 위치하는지 확인
#             if visited[r] == visited[nth_row] or nth_row - r == abs(visited[r] - visited[nth_row]):
#                 return False
#         return True
#
#
#     def dfs(row):
#         # 만약 퀸을 마지막행까지 놓았다면
#         if row >= n:
#             nonlocal cnt
#             cnt += 1 # 가능한 경우의 수 추가
#             return
#
#         # n번때 행까지 반복
#         for col in range(n):
#             visited[row] = col # 퀸을 둠
#             if is_ok_on(row): # 만약 퀸을 둘 수 있는 위치라면
#                 dfs(row+1) # 다음 행에 퀸을 둘 자리를 찾기
#
#     dfs(0)
#     return cnt
#
# print(n_queen(int(input())))

###### 시간초과 #######
#####################

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        # 열, 대각선에 퀸이 없는 경우
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1 # 방문표시
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0 # 방문해제


N = int(input())

ans = 0
v1 = [0] * N # 열에 방문 표시
v2 = [0] * (2*N) # / 대각선 방문 표시 (행과 열의 좌표의 합이 동일함)
v3 = [0] * (2*N) # \ 대각선 방문 표시 (행과 열의 좌표의 차가 동일함)

dfs(0)
print(ans)

######### pypy3 통과 #######