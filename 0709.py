# 푸드 파이트 대회

food = [1,3,4,6]

answer = ""
for i in range(1, len(food)):
    answer += f"{i}"*(food[i]//2)

# print(''.join(list(reversed(answer))))

print(answer+"0"+''.join(list(reversed(answer))))


def solution(food):
    answer = ""

    for i in range(1, len(food)):
        answer += f"{i}"*(food[i]//2)

    return answer+"0"+"".join(list(reversed(answer)))
    