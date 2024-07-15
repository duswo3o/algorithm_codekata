# OX 퀴즈

import sys

def score(s):
    total = 0
    accumulation = 0

    for i in s:
        if i == 'O':
            accumulation += 1
        else:
            accumulation = 0
        total += accumulation
    return total

for _ in range(int(input())):
    tc = sys.stdin.readline().strip()
    print(score(tc))