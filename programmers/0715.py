# 모의고사

def solution(answer):
    one = [1,2,3,4,5] # 1번 수포자의 패턴
    two = [2,1,2,3,2,4,2,5] # 2번 수포자의 패턴
    three = [3,3,1,1,2,2,4,4,5,5] # 3번 수포자의 패턴

    correct_cnt = [0,0,0] # 정답을 맞힌 개수
    for i in range(len(answer)): # 정답 리스트의 길이만큼 반복
        ans = answer[i]
        # 정답이면 정답 개수에 1만큼씩 추가
        if ans == one[i%5]:
            correct_cnt[0] += 1
        if ans == two[i%8]:
            correct_cnt[1]+=1
        if ans == three[i%10]:
            correct_cnt[2]+=1
    # 최대 정답 개수와 같은 사람 리스트 만들기
    return [i+1 for i in range(len(correct_cnt)) if correct_cnt[i]==max(correct_cnt)]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))