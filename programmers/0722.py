# 체육복

def solution(n, lost, reserve):
    no_suit = 0
    common = set(lost)&set(reserve)
    render = [i for i in common]

    while lost:
        now_std = lost.pop()
        if now_std in common:
            continue

        next = now_std + 1
        pre = now_std - 1
        if pre in reserve and pre not in render:
            render.append(pre)
        elif next in reserve and next not in render:
            render.append(next)
        else:
            no_suit += 1

    return n - no_suit



print(solution(5,[2,4], [1,3,5]))
print(solution(5, [2,4],[3]))
print(solution(3,[3], [1]))
print(solution(5,[4,5], [3,4])) # return 4
print(solution(5,[1,2],[2,3])) # return 4