# 나는야 포켓몬 마스트 이다솜

import sys
N, M = map(int, input().split()) # N : 도감에 수록된 포켓몬 개수
                                 # M : 문제의 수

# 포켓몬 도감
pocketmon = {} # 포켓몬 이름 : 번호
for i in range(N): # 도감에 수록된 포켓몬의 수만큼 반복
    p = sys.stdin.readline().strip() # 입력받은 포켓몬 이름
    pocketmon[p] = i+1

pocketmon_name = list(pocketmon.keys()) # 포켓몬 이름만 있는 리스트

for _ in range(M): # 문제의 수만큼 반복
    p = sys.stdin.readline().strip() # 출력할 포켓몬
    if p.isalpha(): # 입력받은 값이 이름인 경우
        print(pocketmon[p]) # 포켓몬 도감에서 번호 출력
    else: # 입력받은 값이 번호인 경우
        print(pocketmon_name[int(p)-1]) # 포켓몬 이름만 있는 리스트에서 인덱스로 이름 찾기