# 괄호 회전하기

from collections import deque

# 괄호가 올바른 괄호인지 확인
def is_correct(s):
    correct = [("(",")"), ("[", "]"), ("{", "}")] # 올바른 괄호
    stack = [] # 여는 괄호를 담을 스택(리스트)
    for i in s:
        if i in"([{": # 여는 괄호라면
            stack.append(i) # 스택에 추가
        else: # 닫는 괄호인 경우
            if len(stack) == 0: return 0 # 꺼낼 괄호가 없으면 0 반환
            left = stack.pop() # 마지막에 추가된 괄호를 꺼내서
            if (left, i) not in correct: # 닫는 괄호와 일치하는지 확인
                return 0 # 다르면 0 반환

    if len(stack) > 0: return 0 # 반복문이 끝났는데 아직 여는 괄호의 짝이 없다면 0 반환
    return 1 # 올바른 괄호인 경우

def solution(s):
    # 문자열을 큐로 만들어주기
    s = [i for i in s]
    s = deque(s)
    ans = 0 # 회전하며 올바른 괄호의 수 찾기
    for i in range(len(s)): # 문자열의 길이만큼 반복(회전)
        ans += is_correct(s) # 올바른 괄호인지 확인
        s.append(s.popleft()) # 괄호 회전
    return ans

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))