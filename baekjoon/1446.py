# 지름길

import sys

N, D = map(int, sys.stdin.readline().split())
shortcut = {}
node = [0, D]

for _ in range(N):
    st, ed, length = map(int, sys.stdin.readline().split())

    if ed > D:
        continue

    if shortcut.get(st) is None:
        shortcut[st] = [[ed, length]]
    else:
        shortcut[st].append([ed, length])
    if st not in node:
        node.append(st)
    if ed not in node:
        node.append(ed)

node.sort()
dist = {}
for idx, n in enumerate(node):
    if idx == 0:
        dist[0] = 0
    else:
        dist[n] = n - node[idx-1]


# 여기가 문제
for short in shortcut:
   for s in shortcut[short]:
       dist[s[0]] = min(dist[s[0]], s[1])



print("node : ", node)
print("dist : ", dist)
print(shortcut)