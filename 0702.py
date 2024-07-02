# 최소직사각형

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

width =  []
length = []

for i in sizes:
    width.append(max(i))
    length.append(min(i))

print(max(width) * max(length))