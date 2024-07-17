# 수 찾기

'''
5
4 1 5 2 3
5
1 3 7 9 5
'''

import sys

N = sys.stdin.readline()
n_item = set(sys.stdin.readline().split())
M = sys.stdin.readline()
m_item = sys.stdin.readline().split()

for m in m_item:
    print(1) if m in n_item else print(0)
