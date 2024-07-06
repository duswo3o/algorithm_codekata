# K번째 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
## [5,6,3]

for i in commands:
    # print(i)
    print(sorted(array[i[0]-1:i[1]])[i[2]-1])