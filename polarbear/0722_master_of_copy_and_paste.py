# 백준 11008 복붙의 달인

for _ in range(int(input())):
    s,p = input().split()
    print(len(s) - s.count(p)*(len(p)-1))