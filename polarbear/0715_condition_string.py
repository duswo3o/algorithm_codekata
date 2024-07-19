# 조건 문자열

def solution(ineq,eq,n,m):
    eq_sign = ineq+eq #[<=,>=,<,>]
    if eq_sign == "<=":
        answer = n <= m
    elif eq_sign == ">=":
        answer = n >= m
    elif eq_sign == "<!":
        answer = n < m
    elif eq_sign == ">!":
        answer = n > m
    return 1 if answer == True else 0


# eval 사용해서 푸는 방법도 있길래...
def solution2(ineq,eq,n,m):
    if eq=="!":
        eq=""
    return 1 if eval(f'{n}{ineq}{eq}{m}') == True else 0

print(solution2(">","!",41,78))
