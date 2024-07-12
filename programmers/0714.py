# 과일 장수

def solution(k,m,score):
    score.sort() # 오름차순 정렬
    result = 0 # 최대 이익

    while len(score)>=m: # 담을 개수기 모자라지 않으면
        apple_box = []
        for i in range(m): # 개의 사과를 담기(사과 점수가 높은거부터)
            apple_box.append(score.pop())
        result += apple_box.pop() * m # 박스에 담긴 가장 낮은 점수 * 사과의 개수를 이익에 더해줌
    return result

print(solution(3,4,[1,2,3,1,2,3,1]))
print(solution(4,3,[4,1,2,2,4,4,4,4,1,2,4,1]))