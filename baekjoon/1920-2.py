# 수 찾기 - ver.binary search

from collections import deque

def make_tree(arr):
    tree = [None]*(2**len(arr))
    arr = deque(arr)

    while arr:
        a = arr.popleft()
        idx = 0
        while idx < len(tree):
            if tree[idx] is None:
                tree[idx] = a
                break
            if a > tree[idx]:
                idx = idx*2+2
            elif a < tree[idx]:
                idx = idx*2+1
    return tree

def find_value(tree, value):
    idx = 0
    while idx < len(tree):
        if tree[idx] == value:
            return 1
        if tree[idx] is None:
            return 0
        if tree[idx] < value:
            idx = idx*2+2
        elif tree[idx] > value:
            idx = idx*2+1
    return 0

N = int(input())
an = list(map(int, input().split()))
M = int(input())
am = list(map(int, input().split()))

an = make_tree(an)
print(an)
for i in am:
    print(find_value(an, i))