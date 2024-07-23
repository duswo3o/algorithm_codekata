# 홀짝홀짝

N = input()
K = input()

odd = 0 # 홀수의 개수
even = 0 # 짝수의 개수

for k in K:
    if int(k) % 2 == 0: # 자리수가 짝수인 경우
        even += 1
    else: # 자리수가 홀수인 경우
        odd += 1

if odd > even: # 홀홀수인 경우
    print(1)
elif even > odd: # 짝짝수인 경우
    print(0)
else: # 둘 다 아닌 경우
    print(-1)