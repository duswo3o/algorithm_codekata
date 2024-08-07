# 가장 큰 수

def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return "0"

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

    my_number.sort(key = lambda x : (x[1]), reverse=True)
    for num in my_number:
        answer += num[0]

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([1,10,100,1000])) # 1101001000
print(solution([0,0,0])) # 0
print(solution([1000, 111, 110, 101, 100, 11, 10, 1, 0])) # 1111111101011010010000
print(solution([101, 10, 232, 23])) # 2323210110
print(solution([555, 565, 566, 55, 56, 5, 54, 544, 549])) # "5665656555555554954544"