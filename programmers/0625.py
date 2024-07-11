# 행렬의 덧셈

arr1 = [[1,2,],[2,3]]
arr2 = [[3,4],[5,6]]

# print([x+y for x,y in zip([1,2], [3,4])])
# print([x+y for x,y in zip(arr1, arr2)])


# answer = []
# for i in range(len(arr1)):
#     answer.append([x+y for x,y in zip(arr1[i], arr2[i])])

# print(answer)

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([x+y for x,y in zip(arr1[i], arr2[i])])
    return answer


# 위에거링 똑같지만 가독성을 위해...
# def solution(arr1, arr2):
#     return [[[x+y for x,y in zip(arr1[i], arr2[i])]] for i in range(len(arr1))]