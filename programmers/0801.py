# 신고 결과 받기

def solution(id_list, report, k):
    r = { i : set() for i in id_list} # dict( 신고자 : 신고 받은 사람 집합 )
    warned = { i : 0 for i in id_list} # dict(신고 받은 사람 : 신고 받은 횟수)
    report = set(report) # set(신고자 피신고자)

    # 반복문으로 딕셔너리 값 채우기
    for i in report:
        a, b = i.split() # a : 신고자 b :피신고자
        r[a].add(b) # 신고자를 key로 하는 피신고자 집합에 추가
        warned[b] += 1 # 경고 받은 횟수 추가

    answer = [] # 정답 리스트
    for i in id_list:
        cnt = 0 # 신고한 사람이 이용 정지를 당한 횟수
        for j in r[i]: # 피신고자 집합
            if warned[j] >= k: # k번 이상 신고당했다면
                cnt += 1
        answer.append(cnt)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],3))