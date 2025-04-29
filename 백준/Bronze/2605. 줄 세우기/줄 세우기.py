import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

line = []
for i, n in enumerate(num):
    if n == 0:
        line.append(str(i+1))
    else:
        front = line[:(len(line)-n)]
        back = line[(len(line)-n):]
        line = front + [str(i+1)] + back

print(" ".join(line))