# 다리를 지나는 트럭

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = deque([0]*(bridge_length-1)) # 다리 위에 있는 트럭
    on_weight = 0 # 다리 위에 있는 트럭 무게의 총 합
    truck_weights = deque(truck_weights) # 다리를 건널 트럭
    # 다리를 건널 트럭이 없을 때까지
    while truck_weights:
        # 트럭이 다리에 들어갈 수 있다면
        if on_weight + truck_weights[0] <= weight:
            out = on_bridge.popleft() # 다리 위에 있는 가장 앞의 값 빼기
            now = truck_weights.popleft() # 다리에 올리갈 트럭
            on_bridge.append(now) # 트럭 다리에 올리기
            on_weight += now # 다리 위에 있는 트럭의 무게 더해주기
            answer += 1 # 시간경과
        # 트럭이 다리에 들어갈 수 없다면
        else:
            # 트럭 한 칸씩 앞으로 당기기
            out = on_bridge.popleft()
            on_bridge.append(0)
            answer += 1 # 시간경과
        # 만약에 트럭이 나온거라면
        if out != 0:
            on_weight -= out # 다리 위에 있는 트럭 값에서 제외

    return answer + bridge_length

print(solution(2, 10, [7,4,5,6]))
print(solution(100,100, [10]))
print(solution(100,100, [10,10,10,10,10,10,10,10,10,10]	))