# 두 개 뽑아서 더하기

numbers = [2,1,3,4,1] # return [2,3,4,5,6,7]

a = set()

for i in range(len(numbers)-1):
    for j in numbers[i+1:]:
        a.add(numbers[i] + j)

print(sorted(list(a)))

def solution(numbers):
    a = set()

    for i in range(len(numbers)-1):
        for j in numbers[i+1:]:
            a.add(numbers[i] + j)

    return sorted(list(a))
