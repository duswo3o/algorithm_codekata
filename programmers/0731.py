# 공원 산책

def solution(park, routes):
    # 시작 좌표 찾기
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == "S":
                now_x, now_y = x ,y
                break
        break

    for r in routes:
        direction, distance = r.split()
        st_x, st_y = now_x, now_y
        if direction == "N":
            if now_x-int(distance) >= 0:
                for i in range(int(distance)):
                    if park[st_x-i-1][st_y] == "X":
                        now_x = st_x
                        break
                    now_x = st_x - int(distance)

        elif direction == "S":
            if now_x+int(distance) < len(park):
                for i in range(int(distance)):
                    if park[st_x+i+1][st_y] == "X":
                        now_x = st_x
                        break
                    now_x = st_x + int(distance)

        elif direction == "E":
            if now_y + int(distance) < len(park[0]):
                for i in range(int(distance)):
                    if park[st_x][st_y + i + 1] == "X":
                        now_y = st_y
                        break
                    now_y = st_y + int(distance)

        elif direction == "W":
            if now_y - int(distance) >= 0:
                for i in range(int(distance)):
                    if park[st_x][st_y- i - 1] == "X":
                        now_y = st_y
                        break
                    now_y = st_y - int(distance)

    return [now_x, now_y]

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))