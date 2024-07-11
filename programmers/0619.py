# 수박수박수박수박수?

def solution(n):
    answer = ['수','박']
    if n%2 == 0:
        return "".join(answer*(n//2))
    return ''.join(answer*(n//2)+["수"])

print(solution(3))
print(solution(4))

# print(["수","박"]*(3//2)+["수"])