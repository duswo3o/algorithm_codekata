# 트리의 부모 찾기


# import sys
# from collections import deque
#
# T = int(input()) # 노드의 개수
#
# # 트리 생성
# my_tree = {1:True} # 1은 루트이므로 True로 설정
# waiting = deque([]) # 대기 큐
#
# for _ in range(T-1):
#     a, b = map(int, sys.stdin.readline().strip().split()) # 연결된 두 정점
#
#     if my_tree.get(a): # 만약 트리에 값이 있으면 = 부모 노드가 이미 있는 경우
#         my_tree[b] = a # 노드 b는 a를 부모로 가짐
#     elif my_tree.get(b): # 노드 b의 값에 부모 노드가 있는 경우
#         my_tree[a] = b # 노드 a는 b를 부모로 가짐
#     else: # 두 노드 모두 부모가 정해지지 않은 경우
#         waiting.append((a, b))  # 대기 큐에 추가
#
# while waiting: # 대기 큐가 모두 없어질 때까지
#     a, b = waiting.popleft() # 먼저 들어온 두 정점부터
#
#     if my_tree.get(a): # 노드 a에 부모가 있는 경우
#         my_tree[b] = a # 노드 b는 a를 부모로 함
#     elif my_tree.get(b): # 노드 b에 부모가 있는 경우
#         my_tree[a] = b # 노드 a는 b를 부모로 함
#     else: # 두 노드 모두 부모가 정해지지 않은 경우
#         waiting.append((a, b)) # 다시 대기의 마지막에 저장
#
# # 2번 노드의 부모부터 T번 노드의 부모까지 출력
# for i in range(2,T+1):
#     print(my_tree[i])



##################### 53% 시간초과 ###########################
############################################################




import sys
sys.setrecursionlimit(10**6) # 재귀함수 깊이 제한


# 깊이 우선 탐색
def dfs(tree, n, parent):
    # visited.append(n)
    for t in tree[n]: # 현재 노드에서 이어진 노드들 돌면서
        if parent[t-1] == 0: # 부모노드가 정해지지 않았다면
            parent[t-1] = n # 현재 노드를 부모 노드로 설정
            dfs(tree, t, parent) # 다음 노드 탐색
    return parent


T = int(sys.stdin.readline()) # 노드의 개수
my_tree = {} # 트리 생성
parent = [0 for _ in range(T)] # 인덱스+1 = 노드번호 / 값 = 부모 노드

# 트리생성 : key = 노드번호 value = 연결된 노드(집합)
for i in range(T):
    my_tree[i+1] = set()

for _ in range(T-1):
    a, b = map(int, sys.stdin.readline().strip().split()) # 노드의 정점을 입력받음
    # value에 추가
    my_tree[a].add(b)
    my_tree[b].add(a)

# 깊이 우선 탐색
dfs(my_tree, 1, parent)

# 노드번호 2부터 출력
for i in range(1,len(parent)):
    print(parent[i])