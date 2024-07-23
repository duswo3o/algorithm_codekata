# A -> B

A, B = map(int, input().split())

times = 1 # 바꾸는데 필요한 연산의 횟수
while B > A: # B가 A보다 크면 계속 반복
    times += 1 # 시도 횟수 증가
    if B%2==0: # 만약 짝수면
        B //= 2 # 2로 나누가
    elif str(B)[-1] == "1": # 마지막 숫자가 1이라면
        B = B//10 # 마지막 숫자 제거
    else: # 마지막 숫자가 1 이외의 홀수라면 만들 수 없는 경우임
        break # 반복문 탈출

# A를 B로 바꾸는데 필요한 연산의 횟수 출력 만약 바꿀 수 없다면 -1
print(times if A == B else -1)
