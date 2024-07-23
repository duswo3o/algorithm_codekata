# 카펫

# 약수 구하는 함수
def divisor(n):
    div = [1] # 1은 모든 수의 약수
    for i in range(2,int(n**0.5)+1): # 제곱근의 수 까지
        if n % i == 0: # 나누어떨어지면
            div.append(i) # 약수에 추가
    return div

def solution(brown, yellow):
    y = divisor(yellow) # 노란색 카펫의 세로 길이가 될 수 있는 리스트
    while yellow:
        h = y.pop() # 노란색 카펫의 세로 길이 (긴 것 부터)
        w = yellow//h #노란색 카펫의 가로 길이
        if brown//2 == h+w+2: # 갈색 카펫이 노란색 카펫을 둘러쌀 수 있다면
            return [w+2, h+2] # 카펫의 가로와 세로 길이 반환

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))