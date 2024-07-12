# 팰린드롬인지 확인하기

def is_palindrome(s):
    l = len(s) # 문자열의 길이
    front = [i for i in s[:l//2]] # 절반 나눠서 앞쪽 글자
    if l%2 == 0: # 길이가 짝수일 때
        for i in s[l//2:]:
            if front.pop() != i:
                return 0
    else: # 길이가 홀수일 때
        for i in s[l//2+1:]:
            if front.pop() != i:
                return 0
    return 1

a = input()
print(is_palindrome(a))