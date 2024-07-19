# qr code

def solution(q,r,code):
    answer = ""
    for i,c in enumerate(code):
        if i % q == r:
            answer += c
    return answer

# solution = lambda q,r,code : "".join([c for i,c in enumerate(code) if i%q==r ])



print(solution(3,1,"qjnwezgrpirldywt"))
print(solution(1,0,"programmers"))
# print(solution1(3,1,"qjnwezgrpirldywt"))
# print(solution1(1,0,"programmers"))
