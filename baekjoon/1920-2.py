# 수 찾기 - ver.binary search

import sys

def binary_search(arr, n):
    start, end = 0,  len(arr)
    while start != end:
        mid = (start + end) // 2
        if n == arr[mid]:
            return 1
        if start == mid:
            return 0
        if mid == end:
            return 0
        elif n > arr[mid]:
            start = mid
        elif n < arr[mid]:
            end = mid

    return 0

N = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
am = list(map(int, sys.stdin.readline().split()))

an.sort()

for i in am:
    sys.stdout.write(str(binary_search(an, i))+"\n")