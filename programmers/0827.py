# 숫자 변환하기

from collections import deque

def solution(x, y, n):
    # 넓이 우선 탐색
    def bfs(x, y, n):
        que = deque([(0, y)]) # (변환 횟수, 업데이트된 값)
        while que:
            idx, now = que.popleft()

            if now == x: # x와 y값이 동일하게 주어진 경우
                return idx

            if now > x:
                # 연산 진행
                a,b,c = now-n, now/2, now/3
                # 만약 연산을 했을 때 찾는 값이 있다면
                if x in [a, b, c]:
                    return idx+1 # 변환 횟수 출력
                # 연산을 했을 때 찾는 값이 없다면
                que.append((idx+1, a)) # (연산 횟수 추가, 업데이트된 y값)
                # 나눗셈을 했을 땐 자연수인 경우에만 큐에 추가
                if b == int(b):
                    que.append((idx+1, b))
                if c == int(c):
                    que.append((idx+1, c))
        # x로 변환이 불가능한 경우
        return -1

    ans = bfs(x,y,n)
    return ans

print(solution(10, 40, 5))
print(solution(10,40,30))
print(solution(2,5,4))
print(solution(38, 40, 2)) # 1
print(solution(3,3,3)) # 0
print(solution(15, 50, 5)) # 2
print(solution(8, 144, 32)) # 3
print(solution(8, 134, 32)) # -1