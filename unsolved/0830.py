# 가장 큰 수

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    my_number = []
    for number in numbers:
        if len(number) == 1:
            my_number.append((number, number*4))
        elif len(number) == 2:
            my_number.append((number, number+(number[1]*2)))
        elif len(number) == 3:
            my_number.append((number, number+number[2]))
        else:
            my_number.append((number, number))

    my_number.sort(key = lambda x : (x[1], -len(x[0])), reverse=True)
    for num in my_number:
        answer += num[0]

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([1,10,100,1000])) # 1101001000