# 이진 변환 반복하기

def solution(s):
    cnt_zero = 0
    cnt_binary = 0

    while s != "1":
        length = len(s)
        cnt_binary += 1
        for i in s:
            if i == "0":
                cnt_zero += 1
                length -= 1
        binary = ""
        while length//2 > 0:
            binary += f"{length % 2}"
            length = length//2
        binary += f"{length}"
        binary = binary[::-1]
        s = binary

    return [cnt_binary, cnt_zero]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))