'''
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''

n = 45 # 3진법으로 1200 뒤집어서 0021 출력값은 7

def solution(n):

    triple = [] # 10진법의 수를 3진법으로 표현할 리스트
    
    # 3진법으로 변환
    while n > 0:
        triple.append(n%3)
        n = n//3

    triple.reverse() # 뒤집어진 3진법으로 표현되므로 다시 뒤집어주기

    # 10진법으로 변환
    answer = 0
    for i, r in enumerate(triple):
        answer += 3**i * r

    return answer

''' python int 함수의 기능 중
int(tmp, n)과 같이 사용하면 //tmp는 문자열
n진법을 사용한 문자열을 10진수로 표현해 줌'''