# 대지

import sys

N = int(input())

lx,ly,rx,ry = 1e9, 1e9, -1e9, -1e9
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    lx = x if x < lx else lx
    ly = y if y < ly else ly
    rx = x if x > rx else rx
    ry = y if y > ry else ry

print((ry-ly)*(rx-lx))


