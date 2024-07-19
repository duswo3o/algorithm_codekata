# 분수 찾기

X = int(input()) # 찾을 번호
'''
등차수열의 합 이용
등차수열의 합 = n(2a+(n+1)d) / 2
d = 등차 a = 첫 번째 항

현재 문제에서 등차는 1 초항은 1이므로
그래서 X가 몇 번째 등차인지 확인하기 위해
아래 반복문을 실행해서 X > n(n-1)/2 를 만족하는 n을 찾는 것
'''
n = 1
while X > n*(n+1)/2:
    n += 1

'''
대각선 방향으로 지그재그로 진행하는데
분모와 분자의 합은 n+1과 같음

n이 짝수일 때는 위에서 아래로 내려오는 대각선 방향
홀수일 땨는 아래에서 위로 올라가는 대각선 방향

둘 중 분모에 들어가는 값은 X - 이전 (n-1)번째 등차의 합
분자에 들어갈 값은 n+1-분모의 값 이므로 아래와 같은 코드를 작성하였다

'''

p = X - ((n)*(n-1)//2)
q = abs(n+1-p)
if n%2 == 0:
    print(f"{p}/{q}")
else:
    print(f"{q}/{p}")

