# 상근이의 여행

import sys

T = int(input()) # 테스트케이스의 수

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split()) # 국가의 수, 비행기의 종류

    travel ={} # 국가 번호 : [갈 수 있는 국가번호]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split()) # 왕복하는 비행기
        if a in travel.keys(): # 이미 등록된 국가면
            travel[a].append(b) # 갈 수 있는 국가에 추가
        else: # 처음 등장하는 국가인 경우
            travel[a] = [b] # 딕셔너리에 key와 value추가
        if b in travel.keys():
            travel[b].append(a)
        else:
            travel[b] = [a]
    # print(travel)

    visited = [] # 1번국가부터 방문한다고 가정
    # now_country = 1
    # pre_country = None # 이전에 방몬한 국가
    airplane = 0 # 비향기를 탄 횟수
    for n in travel.keys(): # 모든 국가를 방문할 때까지
        if n not in visited:
            visited.append(n)
            airplane += 1
        else:
            # continue

            for t in travel[n]: # 현재 국가에서 방문하지 않은 국가가 있다면
                if t not in visited:
                    visited.append(t) # 방문한 국가에 추가
                    # pre_country = now_country # 이전에 방문한 국가는 현재 국가
                    now_country = t # 현재 국가는 방문 안 한 국가
                    airplane += 1 # 비행기 탑승 횟수 추가
                    break

        # if len(visited) != N:
        #     now_country = pre_country # 반복문을 다 돌았는데 모두 방문한 국가였다면 이전 국가로 돌아가
        #     airplane += 1 # 비행기 탑승 횟수 추가

    print(airplane-1)

