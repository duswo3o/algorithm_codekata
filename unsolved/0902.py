# 택배상자

def solution(order):
    answer = 0
    sub_container = []

    now = 0

    for i in range(1,len(order)+1):
        if i == order[now]:
            answer += 1
            now += 1
        else:
            if len(sub_container) < 1:
                sub_container.append(i)
            else:
                if sub_container[-1] == order[now]:
                    sub_container.pop()
                    answer += 1
                    now += 1
                else:
                    sub_container.append(i)

    while sub_container:

        if sub_container[-1] == order[now]:
            sub_container.pop()
            answer += 1
            now += 1
        else:
            break

    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))