# 나무 자르기

import sys

# 기준 길이보다 큰 나무의 인덱스 찾기
def binary_search_idx(arr, n):
    start, end = 0, len(arr)
    while start != end:
        mid = (start+end)//2
        if n == arr[mid]:
            return mid+1
        if mid == start:
            return mid+1
        if mid == end:
            return mid+1
        if n > arr[mid]:
            start = mid
        elif n < arr[mid]:
            end = mid

# 자른 나무 길이의 합
def cut_tree(arr, index, std_tree_length):
    get_tree = 0
    for i in range(index,len(arr)):
        get_tree += (arr[i]-std_tree_length)
    return get_tree



# 나무의 수, 나무의 길이
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort()
mid = N//2

while True:
    pre, next = mid - 1, mid + 1

    now_idx = binary_search_idx(tree, tree[mid])
    now_tree = cut_tree(tree, now_idx, tree[mid])

    pre_idx = binary_search_idx(tree, tree[pre])
    pre_tree = cut_tree(tree, pre_idx, tree[pre])

    next_idx = binary_search_idx(tree, tree[next])
    next_tree = cut_tree(tree, next_idx, tree[next])

    if now_tree == M:
        print(tree[mid])
        exit()

    if pre_tree == M:
        print(tree[pre])
        exit()

    if next_tree == M:
        print(tree[next])
        exit()

    if now_tree < M < pre_tree:
        st, ed = tree[pre], tree[mid]
        break

    if next_tree < M < now_tree:
        st, ed = tree[mid], tree[next]
        break

    if M > pre_tree:
        mid = pre
    elif M < next_tree:
        mid = next

while True:
    mid = (st+ed)//2 + 1
    idx = binary_search_idx(tree, mid)
    my_get = cut_tree(tree, idx, mid)
    if my_get == M:
        print(mid)
        break
    elif my_get < M:
        ed = mid
    elif my_get > M:
        st = mid