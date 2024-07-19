# 달리기 경주

def solution(players, callings):
    racing = {} # 경주하는 사람들의 등수
    for i, p in enumerate(players):
        racing[p] = i # 사람이들 : 등수

    for c in callings: # c는 추월한 사람의 이름
        back = players[racing[c]-1] # player 리스트에서 추월한 사람의 등수보다 하나 앞에 있는 사람의 이름
        # 추월한 사람과 당한 사람의 자리
        players[racing[c]], players[racing[c]-1] = players[racing[c]-1], players[racing[c]]
        racing[c] -= 1 # 추월한 사람의 등수 업데이트
        racing[back] +=1 # 추월당한 사람의 등수 업데이트

    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))