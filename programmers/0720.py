# 옹알이(2)

def solution(babbling):
    nephew = ["aya", "ye", "woo", "ma"] # 할 수 있는 발음
    possible = 0 # 발음할 수 있는 단어의 개수

    for i in range(len(babbling)): # 주어진 배열에서
        for n in nephew:
            if n*2 not in babbling[i]: # 같은 발음이 두 번 연속으로 나오지 않을 때
                babbling[i] = babbling[i].replace(n, " ") # 할 수 있는 발음을 공백으로 대체
        if babbling[i].isspace(): # 공백으로만 이루어진 문자열 = 할 수 있는 발음
            possible += 1
    return possible

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))