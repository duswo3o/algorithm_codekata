import sys

while True:
    num = sys.stdin.readline().strip()
    if num == "0":
        break

    ans = num
    while len(num) !=1:
        cal = 1
        for n in num:
            cal *= int(n)
        ans = ans + " " + str(cal)
        num = str(cal)

    print(ans)