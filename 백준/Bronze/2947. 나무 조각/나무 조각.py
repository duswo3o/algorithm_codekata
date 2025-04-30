import sys
woods = list(map(int, sys.stdin.readline().split()))

while True:
    if woods == [1, 2, 3, 4, 5]:
        break

    for i in range(5):
        if i < 4:
            if woods[i] > woods [i+1]:
                woods[i], woods[i+1] = woods[i+1], woods[i]
                print(" ".join(list(map(str, woods))))