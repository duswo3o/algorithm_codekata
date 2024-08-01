# 틱택토

import sys

def find_winner(TTT):
    if TTT[0][0] == TTT[0][1] == TTT[0][2] and TTT[0][2] in [1,2]:
        return TTT[0][0]
    elif TTT[1][0] == TTT[1][1] == TTT[1][2] and TTT[1][2] in [1,2]:
        return TTT[1][0]
    elif TTT[2][0] == TTT[2][1] == TTT[2][2] and TTT[2][2] in [1,2]:
        return TTT[2][0]
    elif TTT[0][0] == TTT[1][0] == TTT[2][0] and TTT[2][0] in [1,2]:
        return TTT[0][0]
    elif TTT[0][1] == TTT[1][1] == TTT[2][1] and TTT[2][1] in [1,2]:
        return TTT[0][1]
    elif TTT[0][2] == TTT[1][2] == TTT[2][2] and TTT[2][2] in [1,2]:
        return TTT[0][2]
    elif TTT[0][0] == TTT[1][1] == TTT[2][2] and TTT[2][2] in [1,2]:
        return TTT[0][0]
    elif TTT[0][2] == TTT[1][1] == TTT[2][0] and TTT[2][0] in [1,2]:
        return TTT[0][2]
    else:
        return 0

first_player =int(sys.stdin.readline())
if first_player == 1:
    second_player = 2
else:
    second_player = 1


# 틱택토 판 만들기
TTT = [[0]*3 for _ in range(3)]
for i in range(9):
    row, col = map(int, sys.stdin.readline().split())
    if i%2==0:
        TTT[row-1][col-1] = first_player
    else:
        TTT[row-1][col-1] = second_player

    res = find_winner(TTT)
    if res !=0:
        print(res)
        exit()

print(0)



