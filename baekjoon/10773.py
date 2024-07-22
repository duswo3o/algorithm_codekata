# 제로

import sys

# 노드 생성
class Node:
    def __init__(self, item, pre=None):
        self.item = item
        self.pre = pre

# 스택 클래스
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # 스택에 삽입
    def push(self, value):
        self.top = Node(value, self.top) # 노드 추가
        self.size += 1 # 크기 증가

    # 스택에서 꺼내기
    def pop(self):
        if self.size == 0:
            return 0

        node = self.top.item # 가장 마지막에 들어간 노드 꺼내기
        self.top = self.top.pre # 가장 위에 있는 노드를 하나 이전의 노드로 업데이트
        self.size -= 1 # 크기 감소

        return node

    # 모드 노드의 합
    def total(self):
        t = 0
        for i in range(self.size): # 크기만큼의 반복문 실행
            t += self.pop() # 더하기

        return t


T = int(input()) # 입력받을 정수의 개수
stack = Stack() # 스택 생성
for _ in range(T):
    num = int(sys.stdin.readline().rstrip())

    if num == 0: # 0을 입력받으면
        stack.pop() # 가장 마지막의 요소 꺼내기
    else: # 0이 아닌 숫자를 입력받으면
        stack.push(num) # 스택에 널기

print(stack.total()) # 스택에 들어있는 모든 수의 합