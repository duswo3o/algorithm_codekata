# N개의 최소공배수

def divisor(n):
    div = [1]
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            div.append(i)
    r = len(div)
    for i in range(r):
        div.append(n//div[i])
    return sorted(div, reverse=True)


def gcd(arr):
    mini = min(arr)
    mini_div = divisor(mini)
    for i in mini_div:
        l = []
        for j in arr:
            if j%i != 0:
                break
            else:
                l.append(1)
        if len(l) == len(arr):
            return i
    return 1

def solution(arr):
    g = gcd(arr)
    result = g
    for i in arr:
        result *= i//g
    return result

print(solution([2,6,8,14]))
print(solution([1,2,3]))
print(solution([3,4,9,16]))

