# 햄버거 만들기

def solution(ingredient):
    hamburger = []
    cnt_hamburger =  0
    for i in ingredient:
        # 1. 현재 쌓아야하는 재료기 빵, 2. 현재 쌓인 재료가 3개 이상, 3.고기->야채->빵 순서대로 들어있는 경우
        if i == 1 and len(hamburger) >= 3 and hamburger[-1] == 3 and hamburger[-2] == 2 and hamburger[-3] == 1:
            hamburger.pop() # 재료 꺼내기
            hamburger.pop()
            hamburger.pop()
            cnt_hamburger += 1 # 완성된 햄버거 개수 추가
            continue
        # 행버거 재료 쌓기
        hamburger.append(i)
    return cnt_hamburger

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))