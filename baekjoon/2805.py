# 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

st, ed = 1, trees[-1]

while st <= ed:
    get_tree = 0
    mid = (st+ed)//2
    for tree in trees:
        if tree > mid:
            get_tree += (tree-mid)

    if get_tree == M:
        print(mid)
        exit()
    if get_tree < M:
        ed = mid-1
    else:
        st = mid+1

print(ed)