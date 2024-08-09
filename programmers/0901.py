# 쿼드 압축 후 개수 세기


def solution(arr):
    cnt = [0, 0] # 0의 개수와 1의 개수
    l = len(arr)

    def quard_compression(row, col, l):
        std = arr[row][col] # 기준 (0 혹은 1)
        for row in range(row, row+l):
            for col in range(col, col+l):

                """
                기준과 같지 않다면 압축하고자 하는 영역을 좁혀야 함
                배열이 2^n의 크기로 주어지기 때문에 배열의 길이를 절반으로 나누어서
                나누어진 범위에서 재탐색을 하는 방식을 이용
                하나의 배열에 대해 행과 열로 반으로 나누어서 총 4개의 구역이 생성됨"""

                if arr[row][col] != std:
                    l //= 2
                    quard_compression(row, col, l)
                    quard_compression(row+l, col, l)
                    quard_compression(row, col+l, l)
                    quard_compression(row+l, col+l, l)
                    return

        cnt[std] += 1 # 범위 내에서 같은 경우에 개수를 올려줌

    quard_compression(0,0, l)
    return cnt


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))