# 카펫

def divisor(n):
    div = [1]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            div.append(i)
    return div

def solution(brown, yellow):
    y = divisor(yellow)
    while yellow:
        h = y.pop()
        w = yellow//h
        if brown//2 == h+w+2:
            return [w+2, h+2]

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))