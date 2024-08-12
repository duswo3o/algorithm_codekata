# 택배상자

def solution(order):
    answer = 0 # 트럭에 실은 택배상자의 개수
    sub_container = [] # 보조 컨테이너 벨트

    now = 0 # order의 인덱스 : 현재 넣어야할 상자

    for i in range(1,len(order)+1):
        # 현재 순서의 상자가 넣어야 할 상자라면
        if i == order[now]:
            answer += 1 # 트럭에 싣기
            now += 1 # 다음 넣어야 할 상자로 이동
            continue # 다음 반복문 수행

        # 넣어야 할 상자와 다른 상자라면
        else:
            # 보조 컨테이너벨트에 아무것도 없으면
            if len(sub_container) < 1:
                sub_container.append(i) # 보조 컨테이너 벨트에 보관
            else:
                while sub_container:
                    # 보조 컨테이너 벨트에서 꺼낼 수 있는 상자가 현재 순서라면
                    if sub_container[-1] == order[now]:
                        sub_container.pop() # 상자 꺼내고
                        answer += 1 # 트럭에 싣기
                        now += 1 # 다음 넣어야 할 상자로 이동
                    else:
                        break
                sub_container.append(i) # 현재 순서의 상자는 보조 컨테이너 벨트에 추가하기

    # 보조 컨테이너벨트에 상자가 남아있다면 실을 수 있는지 확인하기
    while sub_container:
        #  실을 수 있는 경우
        if sub_container[-1] == order[now]:
            sub_container.pop() # 상자 꺼내기
            answer += 1 # 트럭에 싣기
            now += 1 # 다음 넣어야 할 상자로 이동
        else:
            break

    return answer

# print(solution([4, 3, 1, 2, 5]))
# print(solution([5, 4, 3, 2, 1]))
# print(solution([3, 5, 4, 2, 1])) # 5
# print(solution([1, 2, 3, 4, 5])) # 5
# print(solution([3, 4, 5, 2, 1])) # 5
# print(solution([2, 1, 4, 3, 6, 5, 8, 7, 10, 9])) # 10
print(solution([2, 1, 6, 7, 5, 8, 4, 9, 3, 10])) # 10