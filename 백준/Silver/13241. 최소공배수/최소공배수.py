def gdc(a, b):
    if b == 0:
        return a
    else:
        return gdc(b, a%b)

nums = list(map(int, input().split()))
a, b = max(nums), min(nums)
g = gdc(a, b)
print((a//g) * (b//g) * g)