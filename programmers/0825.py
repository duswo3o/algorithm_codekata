# 뒤에 있는 큰 수 찾기

import heapq
def solution(numbers):
    answer = [-1]*len(numbers)
    heap = []

    for idx, num in enumerate(numbers):
        # 힙에 값이 있고, 힙의 가장 작은 값이 현재의 값보다 작은 경우
        while heap and heap[0][0]<num:
            value, i = heapq.heappop(heap) # 가장 작은 값 추출
            answer[i] = num # 가장 가까이에 있는 큰 값은 현재 값(num)
        # 현재 값의 큰 값을 찾기 위해 현재 값을 힙에 추가
        heapq.heappush(heap, (num,idx))

    return answer


print(solution([2,3,3,5]))
# print(solution([9,1,5,3,6,2]))