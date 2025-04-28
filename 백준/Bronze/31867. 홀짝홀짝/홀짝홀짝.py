N = input()
K = input()

odd = 0
even = 0
for k in K:
    if int(k) % 2 == 0:
        even += 1
    else:
        odd += 1

if odd > even:
    print(1)
elif even > odd:
    print(0)
else:
    print(-1)