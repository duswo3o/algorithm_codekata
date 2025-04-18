import sys

N, L = map(int, sys.stdin.readline().split())
leak = sorted(map(int, sys.stdin.readline().split()), reverse=True)

cnt = 0
while leak:
    tape = L
    pre = leak.pop()
    tape -= 1
    cnt += 1
    while tape and leak:
        now = leak.pop()
        if (now-pre) <= tape:
            tape = tape-(now-pre)
            pre = now
        else:
            leak.append(now)
            break

print(cnt)