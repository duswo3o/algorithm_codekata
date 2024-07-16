# 체육복

def solution(n, lost, reserve):
    no_suit = 0 # 체육복 없는 사람
    common = set(lost)&set(reserve) # 도난 당했는데 여분 있는 사람
    render = [i for i in common] # 체육복 여분 빌려준사람
    lost.sort(reverse=True)

    while lost:
        now_std = lost.pop()
        if now_std in common:
            continue

        next = now_std + 1 # 다음 번호
        pre = now_std - 1 # 이전 번호
        if pre in reserve and pre not in render: # 다음 번호가 여분 있고 안빌려준 경우
            render.append(pre) # 빌려준 사람에 추가
        elif next in reserve and next not in render: # 이전 번호가 여분 있고 안빌려준 경우
            render.append(next) # 빌려준 사람에 추가
        else: # 빌릴 수 없는 경우
            no_suit += 1

    # 전체인원 - 체육복 없는 사람
    return n - no_suit



print(solution(5,[2,4], [1,3,5]))
print(solution(5, [2,4],[3]))
print(solution(3,[3], [1]))
print(solution(5,[4,5], [3,4])) # return 4
print(solution(5,[1,2],[2,3])) # return 4
print(solution(5,[4,2], [3,5])) # return 5