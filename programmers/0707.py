# 두 개 뽑아서 더하기

numbers = [2,1,3,4,1] # return [2,3,4,5,6,7]

a = set()

for i in range(len(numbers)-1):
    for j in numbers[i+1:]:
        a.add(numbers[i] + j)

print(sorted(list(a)))

def solution(numbers):
    a = set() # 중복제거를 위한 집합

    for i in range(len(numbers)-1): # 첫 번째부터 마지막 전까지 반복
        for j in numbers[i+1:]: # 해당 인덱스 뒤의 리스트
            a.add(numbers[i] + j) # 해당 인덱스의 값과 그 이후에 있는 값들을 하나씩 반복하며 더하여 집합에 추가

    return sorted(list(a)) # 집합을 리스트로 바꾸어주고 오름차순 정렬
