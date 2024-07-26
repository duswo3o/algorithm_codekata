# 연속 부분 수열 합의 개수

def solution(elements):
    answer = set()
    answer.add(sum(elements))
    l = len(elements)
    for i in range(1,l): # 부분 수열의 개수
        for j in range(l): # 리스트를 돌며 부분 수열의 개수만큼 슬라이싱
            # 한 번에 슬라이싱 가능한 경우
            if j+ i < l: temp = elements[j:j+i]
            # 뒤랑 앞이랑 이어지는 경우
            else: temp = elements[j:] + elements[:(j+i)%l]
            answer.add(sum(temp))
    return len(answer)

print(solution([7,9,1,1,4]))