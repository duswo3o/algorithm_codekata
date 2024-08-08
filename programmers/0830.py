# 가장 큰 수

def solution(numbers):
    answer = ''

    # 모두 0으로 이루어진 경우
    if sum(numbers) == 0:
        return "0"

    numbers = list(map(str, numbers)) # 숫자를 문자열로 변경
    my_number = [] # 실제 숫자와 비교할 숫자를 담을 리스트
    # 각 자리수에 따라 4자리로 맞추어주기
    for number in numbers:
        if len(number) == 1:
            my_number.append((number, number*4))
        elif len(number) == 2:
            my_number.append((number, number+number))
        elif len(number) == 3:
            my_number.append((number, number+number[2]))
        else:
            my_number.append((number, number))

    # 비교 문자열을 기준으로 정렬, 같은 경우 길이가 짧은 문자열 먼저
    my_number.sort(key = lambda x : (x[1], -len(x[0])), reverse=True)
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
print(solution([1, 10, 100, 1000, 818, 81, 898, 89, 0, 0])) # "8989881881110100100000"
# print(solution([1, 11, 110, 1110])) # ?
print(solution([23, 232, 21, 212])) # 2323221221
print(solution([110, 1]))
print(solution([12,1213]))