# 나무 자르기

import sys

# 나무의 수 , 필요한 나무의 길이
N, M = map(int, sys.stdin.readline().split())
# 나무의 길이
trees = list(map(int, sys.stdin.readline().split()))
st, ed = 1, max(trees) # 자를 나무의 최소값, 최대값

while st <= ed: # 시작점이 끝점보다 커지면 종료
    get_tree = 0 # 자른 나무의 길이
    mid = (st+ed)//2 # 중간값(평균)의 길이 - 나무를 자를 길이(기준)
    for tree in trees:
        if tree > mid: # 만약 나무가 기준 길이보다 크면
            get_tree += (tree-mid) # 나무를 잘라서 더하기

    if get_tree == M: # 얻은 나무의 길이가 원하는 길이라면
        print(mid) # 기준 길이 출력
        exit() # 프로그램 종료
    if get_tree < M: # 기준 길이보다 얻은 길이가 작다면 : 기준 길이를 낮춰야 함
        ed = mid-1 # 끝값 업데이트
    else: # 기준 길이보다 얻은 길이가 크다면 : 기준 길이를 높여야 함
        st = mid+1 # 시작값 업데이트

# 최대 길이를 반환해야하므로 끝값 출력
print(ed)