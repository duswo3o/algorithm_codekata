from collections import Counter
N = int(input())
votes = Counter(list(map(int,input().split())))

if votes.get(0, 0) >= N/2:
    print("INVALID")
elif votes.get(1, 0) > votes.get(-1, 0):
    print("APPROVED")
else:
    print("REJECTED")