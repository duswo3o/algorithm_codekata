# 나무 자르기

import sys

def binary_search(arr, n):
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
    return mid


# 나무의 수, 나무의 길이
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort()
stand = sum(tree)//len(tree)

while True:
    total = 0
    idx = binary_search(tree, stand)
    for i in range(idx, len(tree)):
        total += (tree[i] - stand)
    if total == M:
        break
    if total < M:
        stand -=1
    if total > M:
        stand +=1

print("자른 나무",total)
print("기준 길이", stand)


