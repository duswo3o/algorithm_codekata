# 덧칠하기

def solution(n,m,section):
    answer = 1 # 무조건 한 번은 칠해야 함
    now = section.pop() # 덧칠할 부분의 가장 오른쪽 구역
    while section: # 덧칠해야 하는 부분이 없을 때까지
        next = section.pop() # 그 다음 오른쪽 구역
        if now-next >= m: # 만약 롤러로 같이 칠해지지 않는다면
            answer += 1 # 덧칠 횟수 추가
            now = next # 현재 구역 초기화
    return answer


print(solution(8,4, [2,3,6]))
print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))