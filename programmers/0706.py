# K번째 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
## [5,6,3]

# for i in commands:
#     # print(i)
#     print(sorted(array[i[0]-1:i[1]])[i[2]-1])

def solution(array, commands):
    # commands 리스트를 반복해서 돌면서 array를 슬라이싱 한 후 sorted를 사용해서 정렬 -> k번째의 수출력
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]

print(solution(array, commands))