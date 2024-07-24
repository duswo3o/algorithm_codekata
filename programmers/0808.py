# N개의 최소공배수

# 최대공약수 : 유클리드 호제법 이용
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def solution(arr):
    arr.sort() # 오름차순 정렬
    # 큰 수 부터 차례로 하나씩 추가하며 최소공배수 찾기
    lmc = arr.pop() # 최소공배수
    while arr:
        a = arr.pop()
        if lmc % a != 0: # 현재 최소공배수가 추가된 값의 배수가 아닌 경우
            g = gcd(lmc, a) # 현재 최소공배수와 추가된 수의 최대공약수 찾기
            lmc = g * (lmc//g) * (a//g) # 최소공배수 업데이트
    return lmc

print(solution([2,6,8,14]))
print(solution([1,2,3]))
print(solution([3,4,9,16]))

