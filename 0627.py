# 0627 CodeKata 최대공약수와 최소공배수

def solution (m, n):
    
    # m이 n보다 큰 수가 되도록 설정
    if n > m:
        m, n = n, m
    '''다른 사람의 풀이 중 참고하고싶었던 부분
    조건문을 사용하지 않고
    m, n = max(m,n), min(m,n)으로 작성 할 수 있었음!'''

    # 유클리드 호제법을 이용하여 최대공약수 구하기
    def GCD(m, n):
        a, b = m, n
        r = m % n # m을 n으로 나눈 나머지
        if r != 0: 
            # 나머지가 0이 될 때까지 반복
            while(r!=0):
                a, b = b, r # a, b 업데이트
                r = a % b   # 나머지 업데이트
        return b # 나머지가 0일때의 나누는 수가 최대공약수가 됨
    
    gcd = GCD(m,n)

    return [gcd, gcd*(m//gcd)*(n//gcd)]

print(solution(64,26))