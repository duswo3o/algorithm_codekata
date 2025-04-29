import sys

word = sys.stdin.readline()
ans = ""
for w in word:
    ans += w.upper() if w.islower() else w.lower()

print(ans)