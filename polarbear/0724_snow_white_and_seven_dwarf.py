# 백설 공주와 일곱 난쟁이

import sys

dwarf = {i+1:0 for i in range(9)} # 난쟁이 번호 : 난쟁이 모자에 있는 숫자

for i in range(9):
    dwarf[i+1] = int(sys.stdin.readline())

a, b = 0, 0 # 백설공주의 일곱난쟁이라고 우기는 난쟁이
no_dwarf = sum(dwarf.values()) - 100 # 우기는 난쟁이의 합

# 우기는 난쟁이 찾기
for i in range(1,10):
    for j in range(i+1, 10):
        if dwarf[i] + dwarf[j] == no_dwarf:
            a, b = i, j
            break
    if dwarf.get(a) is not None and dwarf.get(b) is not None:
        break

# 백설공주의 일곱난쟁이
for i in range(1,10):
    if i not in [a,b]:
        print(dwarf[i])
