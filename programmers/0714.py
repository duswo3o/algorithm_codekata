# 과일 장수

def solution(k,m,score):
    score.sort()

    result = 0
    while len(score)>=m:
        apple_box = []
        for i in range(m):
            apple_box.append(score.pop())
        result += apple_box.pop() * m
    return result

print(solution(3,4,[1,2,3,1,2,3,1]))
print(solution(4,3,[4,1,2,2,4,4,4,4,1,2,4,1]))