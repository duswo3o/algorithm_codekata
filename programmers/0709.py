# 푸드 파이트 대회

food = [1,3,4,6]

answer = ""
for i in range(1, len(food)):
    answer += f"{i}"*(food[i]//2)

# print(''.join(list(reversed(answer))))

print(answer+"0"+''.join(list(reversed(answer))))


def solution(food):
    answer = "" # 정답 string

    for i in range(1, len(food)): # food 리스트의 첫 번째 항목부터 마지막 항목까지
        answer += f"{i}"*(food[i]//2) # 음식의 개수를 2개로 나누어 배치

    return answer+"0"+"".join(list(reversed(answer))) # 음식 배치 + 물 + 음식배치 거꾸로
    