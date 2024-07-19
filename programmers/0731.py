# 공원 산책

def solution(park, routes):
    # 시작 좌표 찾기
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == "S":
                now_x, now_y = x ,y
                break

    for r in routes:
        direction, distance = r.split() # 방향과 거리
        st_x, st_y = now_x, now_y # 이동 전 좌표

        # 북쪽으로 이동
        if direction == "N":
            # 공원 밖을 벗어나지 않는다면
            if now_x-int(distance) >= 0:
                # 한 칸씩 이동
                for i in range(int(distance)):
                    # 장애물을 만나 이동할 수 없다면
                    if park[st_x-i-1][st_y] == "X":
                        now_x = st_x # 이동 전 좌표로 이동
                        break
                    now_x = st_x - int(distance) # 장애물이 없다면 거리만큼 이동

        # 남쪽으로 이동
        elif direction == "S":
            if now_x+int(distance) < len(park):
                for i in range(int(distance)):
                    if park[st_x+i+1][st_y] == "X":
                        now_x = st_x
                        break
                    now_x = st_x + int(distance)

        # 동쪽으로 이동
        elif direction == "E":
            if now_y + int(distance) < len(park[0]):
                for i in range(int(distance)):
                    if park[st_x][st_y + i + 1] == "X":
                        now_y = st_y
                        break
                    now_y = st_y + int(distance)

        # 서쪽으로 이동
        elif direction == "W":
            if now_y - int(distance) >= 0:
                for i in range(int(distance)):
                    if park[st_x][st_y- i - 1] == "X":
                        now_y = st_y
                        break
                    now_y = st_y - int(distance)

    return [now_x, now_y]

# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
# print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
# print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
print(solution(["OOOOO", "OOOOO", "OOSOO", "OOOOO", "OOOOO"], ["E 3", "W 3", "S 3", "N 3", "E 2", "E 1", "W 4", "W 1", "S 2", "S 1", "N 4", "N 1"]))