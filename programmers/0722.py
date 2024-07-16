# 체육복

def solution(n, lost, reserve):
    students = [i+1 for i in range(n)]
    c = 0

    render = []
    while students:
        now_std = students.pop()
        if now_std not in lost:
            c += 1

        else:
            next = now_std+1
            pre = now_std-1
            if next in reserve and next not in render:
                render.append(next)
                c += 1
            elif pre in reserve and pre not in render:
                render.append(pre)
                c += 1

    return c


print(solution(5,[2,4], [1,3,5]))
print(solution(5, [2,4],[3]))
print(solution(3,[3], [1]))