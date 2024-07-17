# 대충 만든 자판

def solution(keymap, targets):
    my_keymap = {} # 대충 만든 자판 딕셔너리

    # 대충만든자판 키맵 저장하기
    for key in keymap:
        for i,k in enumerate(key):
            if k not in my_keymap.keys(): # 키맵에 해당하는 키가 없으면
                my_keymap[k] = i+1 # 키와 눌러야하는 수 추가
            else: # 만약 키맵에 키가 있다면
                my_keymap[k] = min(i+1, my_keymap[k]) # 눌러야하는 최소 횟수로 업데이트

    answer = []

    for t in targets:
        cnt = 0 # 키를 누를 횟수
        for i in t:
            if i not in my_keymap.keys(): # 입력하고자 하는 문자가 키맵에 없다면
                cnt = -1 # 키를 누를 횟수에 -1을 저장
                break # 반복문 탎출
            else: # 입력하고자 하는 문자가 키맵에 있으면
                cnt+=my_keymap[i] # 눌러야하는 횟수 더해주기
        answer.append(cnt) # 타겟의 눌러야하는 횟수 추가

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))
print(solution(["ABCDE","FGHIJ"],["ZABCDE"]))
print(solution(["ABACD", "BCEFD"], ["ABCD", "DG", "AABB"]))