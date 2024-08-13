# 균형잡힌 세상


import sys

def is_right(sentence):
    stack = []
    for s in sentence:
        if s in "([": # 여는 괄호인 경우
            stack.append(s)
        elif s in ")]": # 닫는 괄호인 경우
            if len(stack) < 1: # 꺼낼 여는 괄호가 없는 경우
                print("no")
                return
            # 괄호가 일치하지 않는 경우
            if s == ")" and stack.pop() != "(":
                print("no")
                return
            elif s == "]" and stack.pop() != "[":
                print("no")
                return
    # 닫는 괄호가 없는데 여는 괄호가 남아있는지 확인
    if stack:
        print("no")
    else:
        print("yes")
    return


while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    is_right(sentence)