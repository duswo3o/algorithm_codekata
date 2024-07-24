# N개의 최소공배수

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def solution(arr):
    arr.sort()
    lmc = arr.pop()
    while arr:
        a = arr.pop()
        if lmc % a != 0:
            g = gcd(lmc, a)
            lmc = g * (lmc//g) * (a//g)
    return lmc

print(solution([2,6,8,14]))
print(solution([1,2,3]))
print(solution([3,4,9,16]))

