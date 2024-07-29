# 행렬의 곱셈

def solution(arr1, arr2):
    col = len(arr1[0])
    row = len(arr1)
    m_col = len(arr2[0])

    answer = [[0]*m_col for _ in range(row)]

    for i in range(row):
        for j in range(m_col):
            total = 0
            for k in range(col):
                total += (arr1[i][k] * arr2[k][j])
            answer[i][j] = total

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution([[1, 2, 3], [3, 2, 1]], [[1, 2], [2, 1], [1, 2]])) # [[8,10],[8,10]]
print(solution([[1, 2], [2, 1]], [[1, 1, 1, 1], [2, 2, 2, 2]])) # [[5,5,5,5],[4,4,4,4]]