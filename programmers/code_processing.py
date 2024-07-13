# 코드 처리하기

def solution(code):
    mode = True
    answer = ""
    for i,c in enumerate(code):
        if c == "1":
            mode = not mode
            continue
        if mode == True:
            if i%2==0:
                answer+=c
        if mode == False:
            if i%2!=0:
                answer+=c
    return answer

print(solution("abc1abc1abc"))