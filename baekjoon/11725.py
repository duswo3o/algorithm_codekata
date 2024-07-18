# # 트리의 부모 찾기
#
#
# import sys
# from collections import deque
#
# T = int(input())
#
# my_tree = {1:True}
# waiting = deque([])
#
# for _ in range(T-1):
#     a, b = map(int, sys.stdin.readline().strip().split())
#
#     if my_tree.get(a):
#         my_tree[b] = a
#     elif my_tree.get(b):
#         my_tree[a] = b
#     else:
#         waiting.append((a, b))
#
# while waiting:
#     a, b = waiting.popleft()
#
#     if my_tree.get(a):
#         my_tree[b] = a
#     elif my_tree.get(b):
#         my_tree[a] = b
#     else:
#         waiting.append((a, b))
#
#
# for i in range(2,T+1):
#     print(my_tree[i])



##################### 53% 시간초과 ###########################
############################################################




import sys

def dfs(tree, n, parent):
    # visited.append(n)
    for t in tree[n]:
        if parent[t-1] == 0:
            parent[t-1] = n
            dfs(tree, t, parent)
    return parent


T = int(sys.stdin.readline())
my_tree = {}
parent = [0 for _ in range(T)]
for i in range(T):
    my_tree[i+1] = set()

for _ in range(T-1):
    a, b = map(int, sys.stdin.readline().strip().split())

    my_tree[a].add(b)
    my_tree[b].add(a)


dfs(my_tree, 1,parent)

for i in range(1,len(parent)):
    print(parent[i])