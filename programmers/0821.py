# 타깃 넘버

def solution(numbers, target):
    l = []

    def dfs(i, total):
        if i >= len(numbers):
            l.append(total)
            return l

        dfs(i + 1, total + numbers[i])
        dfs(i + 1, total - numbers[i])
        return l


    pm = len(numbers)
    a = dfs(0,0)
    # print(len(a))
    # print(a)

    cnt = 0
    for i in a:
        if i == target:
            cnt+=1
    return cnt

print(solution([1, 1, 1, 1, 1], 3)) # 5
print(solution([4, 1, 2, 1], 4)) # 2