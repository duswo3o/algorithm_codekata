# 행렬 덧셈

A = []
B = []

N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))

# 행렬 덧셈
for n in range(N):
    for m in range(M):
        A[n][m]+=B[n][m]

# 정답 행렬 출력
for i in range(len(A)):
    print(" ".join(map(str,A[i])))