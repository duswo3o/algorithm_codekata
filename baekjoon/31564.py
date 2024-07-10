# 백준 31564. 육각타일미로 탈출기

from collections import deque

q = "3 4 2\n1 1\n1 2"

def escape_hexagon_maze(q):
    q = q.split("\n") # 엔터키 입력 나누기

    for i in range(len(q)):
        q[i] = q[i].split(" ") # 스페이스 입력 나누기
    # print(q)

    N = int(q[0][0]) # 행 길이
    M = int(q[0][1]) # 열 길이

    # 미로 기본 틀
    # 그냥 곱하기 하면 얕은복사라 안되더라...
    maze = [[1]*M for i in range(N)]
    # print(maze)

    # 미로에 장애물 추가하기
    for i in range(1, int(q[0][2])+1):
        a = int(q[i][0]) # 장애물 행의 위치
        b = int(q[i][1]) # 장애물 영의 위치
        maze[a][b] = 0
    # print(maze)  # 장애물 위치 추가한 미로

    # 방문을 저장할 2차원 배열의 값은 출발지로부터의 거리
    visited = [[0]*int(q[0][1]) for i in range(int(q[0][0]))]  
    # print(visited)

    deq = deque() # 방문할 좌표
    deq.append((0, 0)) # 시작좌표

    # 열 번호가 홀수일 때 이동할 수 있는 방향
    odd_dx = [-1, -1, 0, 0, 1, 1]
    odd_dy = [0, 1, -1, 1, 0, 1]

    # 열 번호가 짝수일 때 이동할 수 있는 방향
    even_dx = [-1, -1, 0, 0, 1, 1]
    even_dy = [-1, 0, -1, 1, -1, 0]

    # 방문할 좌표가 있다면
    while deq:

        # visited[0][0] = 1
        cur_x, cur_y = deq.popleft() # 현재 위치(좌표)

        if (cur_x, cur_y) == (N-1, M-1): # 현재 위치가 미로의 탈출구 위치일 때
            return visited[N-1][M-1]
            # print(visited[cur_x][cur_x])

        for i in range(6): # 육각타일미로 -> 6개의 방향으로 움직일 수 있음
            if cur_x%2 == 0: # 열 번호가 짝수일 때
                next_x, next_y = cur_x+even_dx[i], cur_y+even_dy[i]
            else: # 열 번호가 홀수일 때
                next_x, next_y = cur_x+odd_dx[i], cur_y+odd_dy[i]

            # 미로의 범위내 좌표에 있고, 장애물이 있는 위치가 아니고, 방문한 적이 없으면
            if (next_x >= 0 and next_x < N and next_y >= 0 and next_y < M
                and maze[next_x][next_y]!=0 and visited[next_x][next_y]==0):
                deq.append((next_x, next_y)) # 방문할 곳에 좌표 추가
                visited[next_x][next_y] = visited[cur_x][cur_y] + 1 # 이전 길이에서 +1만큼으로 업데이트

        # print(visited)

    return -1

print(escape_hexagon_maze(q))
print(escape_hexagon_maze("3 4 2\n0 1\n1 0"))
print(escape_hexagon_maze("4 7 12\n0 1\n0 2\n0 6\n1 1\n1 3\n1 5\n1 6\n2 1\n2 3\n2 5\n2 6\n3 2"))

