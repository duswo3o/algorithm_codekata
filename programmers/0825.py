def solution(numbers):
    answer = []

    for idx, num in enumerate(numbers):
        temp = -1
        for compare in numbers[idx+1:]:
            if num < compare:
                temp = compare
                break
        answer.append(temp)
    return answer

print(solution([2,3,3,5]))
print(solution([9,1,5,3,6,2]))