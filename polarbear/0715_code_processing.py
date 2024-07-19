# 코드 처리하기

def solution(code):
    mode = True # 시작 모드
    answer = ""
    for i, c in enumerate(code):
        if c == "1": # 문자열을 반복하다가 1을 만나면 모드 변경
            mode = not mode
            continue
        if mode == True: # 모드가 0일 때 짝수 인덱스만 추가
            if i%2==0:
                answer+=c
        if mode == False: # 모드가 1일 때 홀수 인덱스만 추가
            if i%2!=0:
                answer+=c
    return answer if len(answer) > 0 else "EMPTY"

print(solution("abc1abc1abc"))