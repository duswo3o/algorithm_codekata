# 달팽이는 올라가고 싶다

import math

A,B,V = map(int, input().split())
print(math.ceil((V-B)/(A-B))) # 소수점 올림