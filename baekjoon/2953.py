import sys

top_score = 0
winner = 0
for idx in range(5):
    score = list(map(int,sys.stdin.readline().split()))
    total = sum(score)
    if total > top_score:
        top_score =  total
        winner = idx+1

print(winner, top_score)
