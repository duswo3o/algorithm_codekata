# 이어 붙인 수

def solution(num_list):
    odd = ""
    even = ""
    for i in num_list:
        if i%2==0:
            even += f"{i}"
        else:
            odd += f"{i}"
    return int(odd)+int(even)

print(solution([3,4,5,2,1]))
print(solution([5,7,8,3]))