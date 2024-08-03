# 숫자 변환하기

from collections import deque

def solution(x, y, n):

    def bfs(x, y, n):
        cnt = 0
        que = deque([(cnt, y)])
        while que:
            idx, now = que.popleft()

            if now > x:
                cnt += 1
                a,b,c = now-n, now/2, now/3
                if x in [now-n, now/2, now/3]:
                    return idx+1
                que.append((cnt, now-n))
                if now/2 == int(now/2):
                    que.append((cnt, now/2))
                if now/3 == int(now/3):
                    que.append((cnt, now/3))
        return -1


    ans = bfs(x,y,n)
    return ans

print(solution(10, 40, 5))
print(solution(10,40,30))
print(solution(2,5,4))
print(solution(38, 40, 2))