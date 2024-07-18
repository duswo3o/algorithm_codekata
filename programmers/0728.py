# 바탕화면 정리

def solution(wallpaper):
    # 초기값 무한대로 설정
    lux, luy = 1e9, 1e9
    rdx, rdy = -1e9, -1e9

    # 파일이 있는 위치 탐색
    for x, w in enumerate(wallpaper):
        for y, f in enumerate(w):
            if f == "#": # 파일이 있는 위치라면
                # 드래그 시작 위치와 종료 위치 업데이트
                lux = x if x<lux else lux # 가장 왼쪽의 위치
                luy = y if y<luy else luy # 가장 위쪽의 위치
                rdx = x if x>rdx else rdx # 가장 오른쪽의 위치
                rdy = y if y>rdy else rdy # 가장 아래쪽의 위치

    return [lux, luy, rdx+1, rdy+1]

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))